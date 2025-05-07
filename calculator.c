#include<conio.h>
#include<stedio.h>
int main (){
    int a,b,option;
       
    prinyf ("Enter first number..");
    scanf ("%d",&a);
    printf ("Enter second number");
    scanf ("%d",&b);
    printf ("\npress 1 for addition..");
    printf ("\nprint 2 for substration..");
    printf ("\npress 2 for multiplication..");
    printf ("\nEnter your choice....");
    scanf ("%d",&option);
    switch ( option)
    {
        case 1:
            printf("sum = %d",a+b);
            break;
            case 2:
            printf ("substration=%d", a-b);
            break;
            case 3: 
            printf ("multiplication = %d",a+b);
            break;
            default:
            printf ("Enter a valid value");
    }

    return 0;
}
