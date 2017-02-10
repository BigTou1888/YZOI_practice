#include<stdio.h>
int c_index=0;
int open_bracket_cnt=0;
char c[110000];
double r[15];
int offset;

double r_cal (int type) { //type: 0,unknow, 1,serial, 2,parallen
  double result = 0;
  double r_tmp = 0;
  while (c[c_index]) {
    if (c[c_index] == '(') {
      open_bracket_cnt++;
      c_index++;
      r_tmp = r_cal(0);
      if (type == 2) {
        result = result+1/r_tmp;
      } else {
        result = result+r_tmp;
      }
    } else if (c[c_index] == ')') {
      open_bracket_cnt--;
      c_index++;
      if(type == 2) {
        return 1/result;
      } else { 
        return result;
      }
    } else if (c[c_index] == 'R') {
      c_index++;
      int r_index = c[c_index] - '1';
      r_tmp = r[r_index];
      c_index++;
      if (type == 0) {
        result = r_tmp;
      } else if(type == 1) {
        result = result+r_tmp;
      } else {
        result = result+1/r_tmp;
      }
    } else if (c[c_index] == '|') {
      if (type != 2) result = (result==0) ? 0: 1/result;
      type = 2;
      c_index++;
    } else if (c[c_index] == '-') {
      if (type == 2) result = (result==0) ? 0 : 1/result;
      type = 1;
      c_index++;
    } else {
      c_index++;
    }
    if (!(c[c_index])) {
      if (open_bracket_cnt) {
        scanf("%s", c+c_index);
      }
    }
  }
  if(type == 2) return 1/result;
  else return result;
  
}


int main() {
  int n =0;
    scanf("%d", &n);
  int offset = 0;
  for(int i=0; i<n; i++) {
    scanf("%lf", &r[i]);
  }
  scanf("%s", c);
  printf("%.5f\n", r_cal(0));
}
