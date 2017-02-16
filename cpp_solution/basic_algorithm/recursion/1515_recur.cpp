#include <iostream>
using namespace std;
struct joint {
  long low=0;
  long high=0;
  
};
int x1, x2, y1, y2;
joint path_find (int m,int n) {
  if ((m == 1) & (n==1)) {
    joint result;
    result.low=1;
    result.high=0;
    return result;
  } else {
    joint down;
    joint left;
    if ((((n-1)<=y2) & ((n-1)>=y1) & (m<=x2) & (m>=x1)) | (n==1)) {
      down.low =0;
      down.high =0;
    } else {
       down = path_find(m, (n-1));
    }
    if ((((m-1)<=x2) & ((m-1)>=x1) & (n<=y2) & (n>=y1)) | (m==1)) {
      left.low=0;
      left.high=0;
    } else {
      left = path_find((m-1), n);
    }
    joint result;
    result.low  = (left.low+down.low)%10000000000;
    result.high = (left.high+down.high) + (((left.low+down.low)>=10000000000) ? 1:0);
    return result;
  }
}
    
int main() {
  int m,n;
  cin >> m >> n;
  cin >> x1 >> y1 >> x2 >> y2;
  if (x1 >x2){
    int tmp;
    tmp = x1;
    x1=x2;
    x2=tmp;
  }
  if (y1>y2) {
    int tmp;
    tmp = y1;
    y1=y2;
    y2=tmp;
  }
  joint result ;
  result = path_find (m,n);
  if (result.high >0)
    cout << result.high;
  cout << result.low << '\n';
}

