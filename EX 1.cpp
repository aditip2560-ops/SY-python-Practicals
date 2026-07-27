#include<iostream>
using namespace std;

void test (int&x,int y)
{
x+=5;
y*=2;
cout<<x<<endl;
cout<<y<<endl;
}
int main ()
{
int a=5,b=2;
test(a,b);
cout<<a<<endl;
cout<<b<<endl;
}

