#include <iostream>

using namespace std;
// typedef long double precise;
int main(){
    for (long double i = 2; i < 1000; i++)
    {
        cout << (long double)1.0/i << " | " << i << endl;
    }
    
    return 0;
}