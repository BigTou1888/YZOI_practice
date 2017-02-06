#include<stdio.h>

char input_line[1000];
char match_line[1000];
char digit[1000][1000];
int  length[1000];

void letter2digit(char input_string[], int num) {
	int str_length;
	int i;
	for(i=0; input_string[i]; i++) ;
	str_length = i;
	length[num] = i;
	i = 0;
	while (i < str_length) {
		switch (input_string[i]) {
		  case 'a': digit[num][i] = '2'; break;
		  case 'b': digit[num][i] = '2'; break;
		  case 'c': digit[num][i] = '2'; break;
		  case 'd': digit[num][i] = '3'; break;
		  case 'e': digit[num][i] = '3'; break;
		  case 'f': digit[num][i] = '3'; break;
		  case 'g': digit[num][i] = '4'; break;
		  case 'h': digit[num][i] = '4'; break;
		  case 'i': digit[num][i] = '4'; break;
		  case 'j': digit[num][i] = '5'; break;
		  case 'k': digit[num][i] = '5'; break;
		  case 'l': digit[num][i] = '5'; break;
		  case 'm': digit[num][i] = '6'; break;
		  case 'n': digit[num][i] = '6'; break;
		  case 'o': digit[num][i] = '6'; break;
		  case 'p': digit[num][i] = '7'; break;
		  case 'q': digit[num][i] = '7'; break;
		  case 'r': digit[num][i] = '7'; break;
		  case 's': digit[num][i] = '7'; break;
		  case 't': digit[num][i] = '8'; break;
		  case 'u': digit[num][i] = '8'; break;
		  case 'v': digit[num][i] = '8'; break;
		  case 'w': digit[num][i] = '9'; break;
		  case 'x': digit[num][i] = '9'; break;
		  case 'y': digit[num][i] = '9'; break;
		  case 'z': digit[num][i] = '9'; break;
		}
	    i++;
	}
}

void compare_digit (char match_string[], int total_num) {
	int i =0;
	int str_length;
	for(i=0; match_string[i]; i++) ;
	str_length = i;
	int result = 0;
	i = 0;
	while (i < total_num) {
		if (str_length != length[i]) { i++; continue;}
		int j =0;
		while (j < str_length) {
			if (match_string[j]!=digit[i][j]) break;
			j++;
		}
		if (j == str_length) result++;
		i++;
	}
	printf("%d\n", result);
}

int main() {
  int n;
  scanf("%d", &n);
  int i =0;
  while (i < n) {
	  scanf("%s", input_line);
	  letter2digit(input_line, i);
	  i++;
  }
  scanf("%s", match_line);
  compare_digit (match_line, n);

}
