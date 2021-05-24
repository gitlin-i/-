#include <iostream>
#include <cstdio>
#include <iomanip>

struct tuple{
    int x;
    int y;
};
class Stack{
    
}
void matrix(int n,int m);
void print_matrix( char **mat ,int n,int m);
using namespace std;

int main() {
    int n,m;

    cin >> n>>m;
    matrix(n,m);

}


void matrix(int n,int m)
{
    char ** mat = new char * [n];
    for(int i=0;i<n;i++ )
    {
        mat[i] = new char [m];
    }
    for (int i = 0; i<n;i++)
    {
        for(int j=0;j<m;j++)
            cin >> mat[i][j];
    }

    print_matrix(mat,n,m);


}
void print_matrix(char **mat ,int n,int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            printf("%c",mat[i][j]);
        }
        cout<<endl;
    }
}
void island()
{
    
}
bool isGround(char c)
{
    if (c == '#')
        return true;
    else
        return false;
}
bool isGround(char * c)
{
    if (*c == '#')
        return true;
    else
        return false;
}