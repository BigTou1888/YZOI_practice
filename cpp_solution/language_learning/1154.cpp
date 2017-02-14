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
int open_bracket_line = 0;
int open_comment_bracket_line = 0;
int finish = 0;
int waiting_for_star=0;
int waiting_for_comment_right_bracket=0;
int fail = 0;
void parse(int type) { // 0: normal, 1: equal, 2: comment

    char c;
  c=com[com_index];
  while (com_index <= length) {
    if (finish) return;
    if (com_index >= length)  return;
    c=com[com_index];
    com_index++;
    if (c == '\n'){
      finish=1;
      return;
    } else {
      if (c=='\r') {
    	  if(com_index == (length-1)) {
            finish=1;
            return;
    	  } else {
    		  open_bracket -=open_bracket_line;
    		  open_comment_bracket-=open_comment_bracket_line;
    		  open_bracket_line = 0;
    		  open_comment_bracket_line = 0;
    	  }
      } else {
        if (type == 0) {
          if (c==')') {
            fail = 1;
            return;
          }
          if (c=='(') {
            waiting_for_star=1;
            open_bracket++;
            open_bracket_line++;
            parse(1);
          } 
        } else if(type == 1) {
          if(waiting_for_star == 1) {
            waiting_for_star=0;
            if(c=='*') {
              open_bracket--;
              open_bracket_line--;
              open_comment_bracket++;
              open_comment_bracket_line++;
              parse(2);
              return;
            }
          }
          
          waiting_for_star=0;
          if(c=='(') {
            waiting_for_star=1;
            open_bracket++;
            open_bracket_line++;
            parse(1);
          } else if (c==')') {
            open_bracket--;
            open_bracket_line--;
            return;
          } else if ((c>='0' & c<='9') | c=='+' | c=='-' | c=='*' | c=='/' | c=='=' | c=='\r') {
            continue;
          } else {
            fail = 1;
            return;
          }

        } else if (type == 2) {
          if (waiting_for_comment_right_bracket) {
            waiting_for_comment_right_bracket=0;
            if(c==')') {
              open_comment_bracket--;
              open_comment_bracket_line--;
              return;
            }
          } 
          waiting_for_comment_right_bracket=0;
          if (c=='*') {
            waiting_for_comment_right_bracket=1;
          }
        }
      }
    }
  }
  
}


int main () {

  //getline(cin, com, '\n');
  while (getline(cin, com)) {
  //gets(com);
	finish=0;
    length=com.size();
	com_index = 0;
	if (open_comment_bracket !=0) {
		parse(2);
	} else if (open_bracket!=0) {
		parse(1);
	} else {
		parse(0);
	}
	/*
	  if (fail | (open_comment_bracket !=0) | (open_bracket!=0))
	    printf("NO\n");
	  else
	    printf("YES\n");
  */
  }
  if (fail | (open_comment_bracket !=0) | (open_bracket!=0))
    printf("NO\n");
  else
    printf("YES\n");
}
