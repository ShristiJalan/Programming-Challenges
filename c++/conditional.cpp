#include <iostream>
using namespace std;

int main()
{

    int savings;
    cin >> savings;

    if (savings > 5000)
    {
        if (savings > 10000)
        {
            cout << "Roadtrip with neha";
        }
        else
        {
            cout << "shopping with neha";
        }
    }
    else if (savings > 2000)
    {
        cout << "Rashmi";
    }
    else
    {
        cout << "Friends";
    }
}