#include<iostream>
using namespace std;

int main(){

int n;

cout << "Enter a number: ";

cin >> n;

cout << "Number is and it is: ";

if (n % 2 == 0 )
{
    cout << "even";
} 
else{
    cout << "odd";
}
return 0;
}