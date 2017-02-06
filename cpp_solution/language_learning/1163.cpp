#include<stdio.h>

char sample_line[1000001];
char match_line[1000001];
int next[1000001];


void getNext(char input_string[], int result[], int str_len) {
    result[0] = -1;
    int j = 0;
    int k = -1;
    while (j < str_len) {
        if (k == -1){
            k++;
            j++;
            result[j] = k;
        } else if (input_string[j] == input_string[k]) {
            k++;
            j++;
            result[j] = k;
        } else {
            k = result[k];
        }
    }
}

int len(char str[]) {
	int length = 0;
	for (length = 0; str[length]; length++)
		  ;
	return length;
}

int kmp_match(char match_str[], char sample_str[], int m_len, int s_len) {
    int m = 0;
    int s = 0;
    int result = 0;

    while (m < m_len) {
        if ((match_str[m] == sample_str[s]) | (s==-1)) {
            s++;
            m++;
            if (s == s_len) {
                result++;
                s = next[s];
            }

        } else {
            s = next[s];
        }
    }
    return result;
}

int main() {
  int n;
  scanf("%d", &n);
  int i =0;
  while (i < n) {
	  scanf("%s", sample_line);
	  scanf("%s", match_line);
	  int m_len = len(match_line);
	  int s_len = len(sample_line);
	  getNext(sample_line,next,  s_len);
	  int result = kmp_match(match_line, sample_line, m_len, s_len);
	  printf("%d\n", result);
	  i++;
  }
}
