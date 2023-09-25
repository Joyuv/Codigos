#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    int num1;
    num1 = 44;

    int num2;
    num2 = num1 + 20;

    cout << "\nO primeiro número é " << num1;
    cout << "\nO segundo número é " << num1 << " + 20 = " << num2 << endl;
    system("read -p 'Pressione enter para continuar...' var");
    return 0;
}

