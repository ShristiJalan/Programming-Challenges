#include <iostream>
using namespace std;

void pythagorian(int x, int y, int z)
{
    if ((x * x) == (y * y) + (z * z))
    {
        cout << "pythagorian triplet" << endl;
    }
    else
    {
        cout << "Not a pythagorian triplet" << endl;
    }
}

int main()
{
    int x, y, z;
    cin >> x >> y >> z;

    pythagorian(x, y, z);

    return 0;
}