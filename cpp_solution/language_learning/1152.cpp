#include<stdio.h>
#include<iostream>


char a[500];
char cur[500];
int next[500];
int length=1;
int cur_digit_pos = 1;

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

void digit_update(){
  int carry = 0;
  int add = 1;
  for (int i = 0; i < length; i++) {
	  cur[i] += carry+add;
	  if ((cur[i] - '0') >=10) {
		  cur[i] = ((cur[i]-'0')%10) + '0';
		  carry = 1;
	  } else {
		  carry = 0;
	  }
	  add = 0;
  }
  if (carry ) {

	  length++;
	  cur[length-1] = '1';
  }

  cur_digit_pos = 1;

}

char cur_update () {

  if (cur_digit_pos == length) {
    digit_update();
  } else {
	  cur_digit_pos++;
  }
  char tmp = cur[length-cur_digit_pos];
  return tmp;
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
	scanf("%s", a);
	int i = 0;
    int a_len;
    for (i = 0; a[i]; i++) ;
    a_len = i;

    for (i = 1; i<500; i++) cur[i] ='0';
    cur[0] = '1';
    getNext(a, next, a_len);

	int total_pos = 0;
	int com_pos = 0;
	char cur_chr = '1';
	while (1) {


	  if ((  cur_chr == a[com_pos]) | (com_pos==-1)) {
	    com_pos++;
	    total_pos++;
        cur_chr = cur_update();



	    if (com_pos == a_len) {
		  printf("%d\n", (total_pos-a_len+1));
		  break;
		}

	  } else {
		com_pos = next[com_pos];
	  }
    }
}


