#include <iostream>
using namespace std;
struct joint {
  long low;
  long middle;
  long high;
  
} p[55][55];
int x1, x2, y1, y2;
void path_find (int m,int n) {
  
  for (int i=1; i<=n;i++) {
    for(int j=1;j<=m;j++) {
      if ((i == 1) & (j==1)) {
        p[i][j].low=1;
        p[i][j].middle=0;
        p[i][j].high=0;
      } else {
        joint down;
        joint left;
        if ((((i-1)<=y2) & ((i-1)>=y1) & (j<=x2) & (j>=x1)) | (i==1)) {
          down.low =0;
          down.middle=0;
          down.high =0;
        } else {
          down = p[i-1][j];
        }
        if ((((j-1)<=x2) & ((j-1)>=x1) & (i<=y2) & (i>=y1)) | (j==1)) {
          left.low=0;
          left.middle=0;
          left.high=0;
        } else {
          left = p[i][j-1];
        }
        long low = left.low+down.low;
        long middle = (left.middle+down.middle) + low/10000000000;
        long high = (left.high+down.high) + middle/10000000000;

        p[i][j].low  = low%10000000000;
        p[i][j].middle= middle%10000000000;
        p[i][j].high = high%10000000000;
      }
    }
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
  path_find (m,n);
  //if (p[n][m].high >0)
    //cout << p[n][m].high;
  if (p[n][m].middle>0)
    cout << p[n][m].middle;
  cout << p[n][m].low << '\n';
}

