#include <iostream>
using namespace std;

int main()
{
    char button;
    cout << "Input a character" << endl;
    cin >> button;

    switch (button)
    {
    case 'a':
        cout << "Hello" << endl;
        break;

    case 'b':
        cout << "Namaste" << endl;
        break;

    default:
        cout << "I am still learning more!" << endl;
        break;
    }
    return 0;
}