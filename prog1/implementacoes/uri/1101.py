num_aux = mai = men = 0
trava = True

while trava:
        n1, n2 = map(int, input().split())
        if(n1 <= 0 or n2 <= 0):
             break

        mai = n1 if n1 > n2 else n2
        men = n2 if n2 < n1 else n1
   
        if mai > men :
                num_aux = mai
                mai = men
                men = num_aux
               
        soma = 0
       
        while mai <= men :
         print(mai, end=' ')
         soma += mai
         mai+=1
        print(f"Sum={soma}")
