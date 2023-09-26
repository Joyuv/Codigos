#include <iostream>

using namespace std;

namespace Silva
{
    int a;
    int b;
}
namespace Neves
{
    double a;
    double b;
}

int main()
{
    Silva::a = 4;
    Silva::b = 7;
    Neves::a = 5.453;
    Neves::b = 2.13e4;

    cout << "Silva::a = " << Silva::a << endl;
    cout << "Silva::b = " << Silva::b << endl;
    cout << "Neves::a = " << Neves::a << endl;
    cout << "Neves::b = " << Neves::b << endl;

    system("read -p 'Pressione enter para continuar...' var");
    return 0; 

}