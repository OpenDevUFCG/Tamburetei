#include <stdio.h>
#include <stdlib.h>

int main (){
	int n, i, numero;
	i=0;
	
	scanf ("%d", &n);
	
	for (n=n; n>i; i++){
		scanf("%d", &numero);
		
		if (numero % 2 == 0 && numero > 0){
			printf("EVEN POSITIVE\n");
			
		}else if (numero % 2 == 0 && numero < 0){
			printf("EVEN NEGATIVE\n");
			
		}else if (numero % 2 != 0 && numero > 0){
			printf("ODD POSITIVE\n");
			
		}else if (numero % 2 != 0 && numero < 0){
			printf("ODD NEGATIVE\n");
			
		}else if (numero == 0){
			printf("NULL\n");
		}
	}
		
	return 0;
}
