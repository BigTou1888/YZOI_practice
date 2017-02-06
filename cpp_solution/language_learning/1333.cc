#include <iostream>
#include <string>
using namespace std;
int main() {
string line_char[4];
/*
cin >>line_char[0];
cin >>line_char[1];
cin >>line_char[2];
cin >>line_char[3];
*/
getline(cin, line_char[0]);
getline(cin, line_char[1]);
getline(cin, line_char[2]);
getline(cin, line_char[3]);
int max = 0;
int i = 0;
int char_sta[26];

while (i < 26) {
  char_sta[i] =0;
  i++;
}

i = 0;
while (i < 4) {
    int j = 0;
    while (j < line_char[i].size()){
        char charactor = line_char[i][j];
        int value = int(charactor-'A');
        if ((value >=0) & (value <26)){
            char_sta[value] = char_sta[value] +1;
            if (char_sta[value] > max){
                max = char_sta[value];
            }
        }
        j++; 
    }
    i++;
}
i = max;
while (i > 0){
    int j =0;
    int last = 0;
    while( j < 26){
        if (char_sta[j] >= i){
            last = j;
        }
        j++;
    }
    j = 0;
    while(  j <= last){
        if (char_sta[j] >= i){
            if (j != last) 
                cout << "* " ;
            else 
                cout << "*" << "\n";
        } else {
            cout << "  ";
        }
        j++;
    }
    i--;
}
i = 0;
while (i < 25){
    cout << char('A'+i) << " ";
    i++;
}
cout << "Z" << "\n";
}
