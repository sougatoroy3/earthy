#include <iostream>

using namespace std;

int main(){

    int n;

cin>>n;

     int a[n], b[n], c=5001,d=0,e=0,f=0;

         for(int i=0; i<n; i++)

         { cin>>a[i]; if(a[i]<c) c=a[i]; }    

       for(int i=0; i<n; i++) cin>>b[i];

        

        for (int i = 1; i; i++) // INFINITE LOOP

       {

         for(int k=0; k<n;k++)

         {

               if(a[k]>c) {

                              if(a[k]>=b[k]) { a[k]= a[k] - b[k]; d+=1;}

                            }

               if(c>a[k]) c=a[k];  // MINIMUM VALUE IS UPDATED EACH TIME

         }

        

   for(int j=0; j<n;j++)

        { 

             if(a[j]!=c)

             {    if( a[j]<b[j] )

                 { cout<<-1; return 0 ;}

             }

         }

            

      for(int j=0; j<n-1;j++)

         {

             if(a[j]==a[j+1]) f=1;

             else {f=0; break;}

          }

 

            if(f==1) {cout<<d; return 0;}

        }

}