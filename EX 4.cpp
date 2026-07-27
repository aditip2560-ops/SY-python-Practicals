#include<iostream>
using namespace std;

int main ()
{
int mark[5];
int*ptr;

cout<<"enter mark of student:";
for(int i=0;i<5;i++)
{
cin>>mark[i];
}

ptr=mark;

cout<<"\n enter mark of student are:";
   for(int i=0;i<5;i++)
   {
	cout<<"student :"<<i+1<<"i"<<*(ptr+i)<<endl;
   }
}

