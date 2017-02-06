#include <iostream>
#include <math.h>
using namespace std;
int SumOfDivisors(int num){
    int i=1;
    int test_num = sqrt(num);
    int sum=0;
    if (num == 1) {
      return 0;
    }else {
    while (i <=  test_num){
        if (num%i == 0){
            sum = sum+i;
            if ((num/i != i) & (num/i !=num)){
                sum = sum+num/i;
            }
            if (num/i < test_num){
                test_num = num/i;
            }
        }
        i = i+1;
    }
    return sum;
    }
}
            
int main(){
    int index = 1;
    while (index <= 100000){
        int a=index;
        int a_sum = SumOfDivisors(a);
        if ( (a_sum != a) & (a_sum<=100000) ){
            int b = a_sum;
            int b_sum = SumOfDivisors(b);
            if (b_sum == a ){
               cout << a << ' ' << b << '\n';
            }
        }
        index = index+1;

    }
    return 0;

}
