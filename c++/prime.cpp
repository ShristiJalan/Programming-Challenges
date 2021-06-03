#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 0;

    for (int i = 2; i < sqrt(n); i++)
    {
        if (n % i == 0)
        {
            cout << "not a prime number";
            count++;
            break;
        }
    }
    if (count == 0)
    {
        cout << "Prime" << endl;
    }
    return 0;
}