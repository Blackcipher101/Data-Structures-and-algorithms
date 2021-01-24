#include <iostream>
#include<string>
using namespace std;
int * append(int arr1[100],int ele)
{
    int str_len;
    str_len= sizeof(arr1);
    cout<<str_len;
    arr1[str_len]=ele;

    return arr1;

}
int main()
{
    int *res;
    int arr[]={1};
    res = append(arr, 4);
    int str_len= sizeof(res);
    cout<<str_len-1;
    return 0;

}