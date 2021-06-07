#include <iostream>
#include <math.h>
using namespace std;

int binaryToDecimal(int n)
{
    int ans = 0;
    int x = 1;
    int c = 0;
    int sum = 0;
    while (n > 0)
    {
        int lastDigit = n % 10;
        int temp = lastDigit * pow(2, c);
        sum = sum + temp;
        n = n / 10;
        c++;
    }
    return sum;
}

int main()
{
    int n;
    cin >> n;

    cout << binaryToDecimal(n) << endl;
}