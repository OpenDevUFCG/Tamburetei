
#include <stdio.h>

int main(){

    float a, b, c, md;
    
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    
    md = (a * 2 + b * 3 + c * 5) / 10;
    
    printf("MEDIA = %.1f\n", md);

    return 0;    
}
