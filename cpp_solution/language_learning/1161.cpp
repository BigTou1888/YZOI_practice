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



int main() {
  while (scanf("%s", input_line) != EOF) {
	  if (input_line[0] == '.')  break;
	  else {
		  int input_len = 0;
		  for (input_len = 0; input_line[input_len]; input_len++)
			  ;
		  getNext(input_line, next, input_len);
		  int result_tmp = input_len/(input_len - next[input_len]);
		  if (  input_len%(input_len - next[input_len]) == 0) {
			  printf("%d\n", result_tmp);

		  } else {
			  printf("1\n");
		  }
	  }
  }
}
