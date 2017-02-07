#include<stdio.h>
#include<math.h>
char input_line[200000];
int div [200000];

bool array_compare (int golden_cnt[], int sample_cnt[]) {
	int i =0;
	while (i < 26) {
		if (golden_cnt[i] != sample_cnt[i]) break;
		i++;
	}
	if (i == 26) return true;
	else return false;
}
void letter_cnt(char cal_str[], int start, int end, int letter_count[]) {
	for (int i =0; i<26; i++) letter_count[i]=0;
	int i = start;
	while (i < end) {
		char chr_tmp = cal_str[i];
		int index = chr_tmp-'a';
		letter_count[index]++;
		i++;
	}
}

int divisor (int value ) {
  int i = 1;
  int uppcase = sqrt(value);
  int count = 0;
  int j = 0;
  while (i <= uppcase) {
	  if (value%i == 0) {
          if (value/i ==i) {
  		    div[j] = i;
            j++;
		    count ++;
          } else {
		    div[j] = i;
            div[199999-j] = value/i;
            j++;
		    count +=2;
          }
	  }
	  i++;
  }

  return count;
}

void div_print_debug (int div_num) {
	  int low_part_upper = (div_num+1)/2;
	  int up_part_lower = 199999 - (div_num/2) + 1;
      int i = 0;

      while (i < 199999) {
    	printf("index: %d\n", i);
    	printf("%d \n", div[i]);
	    if (i == (low_part_upper-1)) i = up_part_lower;
        else i++;
      }
}

int main() {
  int i =0;
  int str_length;
  scanf("%s", input_line);
  for(i=0; input_line[i]; i++) ;
  str_length = i;
  int div_num = divisor(str_length);
  int substr_length = 0;
  bool found = 0;
  int low_part_upper = (div_num+1)/2;
  int up_part_lower = 199999 - (div_num/2) + 1;
  i = 0;
  while (i < 199999) {
	  int golden_cnt[26];
	  int sample_cnt[26];
	  int div_tmp = div[i];
	  int start = 0;
	  int end = start+div_tmp;
	  letter_cnt(input_line, start, end, golden_cnt);
	  start = end;
	  end = start+div_tmp;
	  while (end <= str_length) {
		  letter_cnt(input_line, start, end, sample_cnt);
		  bool substr_match = array_compare (golden_cnt, sample_cnt);
		  if (!substr_match) break;
		  start = end;
		  end = start+div_tmp;
	  }
	  if (end>str_length) {
		  substr_length = div_tmp;
		  found = true;
		  break;
	  } else {
          if (i == (low_part_upper-1)) i = up_part_lower;
          else i++;
	  }


  }

  if (found) {
	  for (int i =0; i<substr_length; i++){
		  printf("%c", input_line[i]);

	  }
	  printf("\n");
  } else {
	  printf("-1\n");
  }


}
