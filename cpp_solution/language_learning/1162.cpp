#include<stdio.h>

char input_line[1000001];
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

void trace_next(int len) {
    int repeat_len = next[len];
    if (repeat_len != 0) {
        len = repeat_len;
        trace_next(len);
        printf("%d ", repeat_len);
    } else {
        return;
    }
}


int main() {
  while (scanf("%s", input_line) != EOF) {
	  int input_len = 0;
	  for (input_len = 0; input_line[input_len]; input_len++)
		  ;
	  getNext(input_line, next, input_len);
      trace_next(input_len);
      printf("%d\n", input_len);
  }
}
