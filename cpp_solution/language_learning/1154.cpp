#include<stdio.h>
#include<string>
#include <iostream>
using namespace std;
//char com[12000];
string com;
int com_index=0;
int length=0;
int cr=0;
int open_bracket = 0;
int open_comment_bracket = 0;
int waiting_for_star=0;
int waiting_for_comment_right_bracket=0;
int fail = 0;
void parse () { // 0: normal, 1: equal, 2: comment
  char c;
  c=com[com_index];
  while (com_index < length) {
    c=com[com_index];
    com_index++;
    if(open_comment_bracket!=0) {
      if (waiting_for_comment_right_bracket) {
        waiting_for_comment_right_bracket=0;
        if(c==')') {
          open_comment_bracket--;
          continue;
        }
      } 
      waiting_for_comment_right_bracket=0;
      if (c=='*') {
        waiting_for_comment_right_bracket=1;
      }
    } else if(open_bracket != 0) {
       if(waiting_for_star == 1) {
         waiting_for_star=0;
         if(c=='*') {
           open_bracket--;
           open_comment_bracket++;
           continue;
         }
       }
          
       waiting_for_star=0;
       if(c=='(') {
         waiting_for_star=1;
         open_bracket++;
         continue;
       } else if (c==')') {
         open_bracket--;
       } else if (((c>='0') & (c<='9')) | (c=='+') | (c=='-') | (c=='*') | (c=='/') | (c=='=')) {
         continue;
       } else {
         fail = 1;
       }

     } else {
       if (c==')') {
         fail = 1;
       }
       if (c=='(') {
         waiting_for_star=1;
         open_bracket++;
       }
     }
  }
}


int main () {

  //getline(cin, com, '\n');
  while (getline(cin, com)) {
    waiting_for_comment_right_bracket=0;
    waiting_for_star=0;
  //gets(com);
        length=com.size();
	com_index = 0;
	parse();
/*
	  if (fail | (open_comment_bracket !=0) | (open_bracket!=0)) {
            printf("%d %d", open_comment_bracket, open_bracket);
	    printf("NO\n");
	  } else {
	    printf("YES\n");
          }
*/

  }
  if (fail | (open_comment_bracket !=0) | (open_bracket!=0)) {
 //   printf("%d %d ", open_comment_bracket, open_bracket);
    printf("NO\n");
  } else {
    printf("YES\n");
  }
}
