#include <iostream>
#include <Windows.h>
using namespace std;
int main()
{
    float l1, l2, wynik;
    int p;
    cin >> l1;
    cin >> l2;
    cout << endl<< "Co chcesz zrobic?" << endl;
    cout << "1.Dodawanie" << endl << "2.Odejmowanie" << endl << "3.Mnozenie" << endl << "4.Dzielennie" << endl;
    cin >> p;
    system("cls");
    switch (p)
    {
    case 1: cout << "Wynik = " << l1 + l2; break;
    case 2: cout << "Wynik = " << l1 - l2; break;
    case 3: cout << "Wynik = " << l1 * l2; break;
    case 4: cout << "Wynik = " << l1 / l2; break;
    default: cout << "Wybrano nie istniejaca operacje"; break;
    }
    return 0;
}