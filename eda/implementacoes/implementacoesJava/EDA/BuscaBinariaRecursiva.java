package EDA;

import java.util.Scanner;

class BuscaBinariaRecursiva {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String entrada1 = sc.nextLine();
        int num = sc.nextInt();

        String[] aux = entrada1.split(" ");
        int[] sequencia = new int[aux.length];

        for (int i = 0; i < aux.length; i ++) {
            sequencia[i] = Integer.parseInt(aux[i]);
        }

        buscaBinariaRecursiva(sequencia, num, 0, sequencia.length - 1);

    }

    public static int buscaBinariaRecursiva(int[] sequencia, int num, int inicio, int fim){

        if (inicio > fim) {
            System.out.println(-1);
            return -1;
        }

        int media = (inicio + fim)/2;

        int valorMedio = sequencia[media];

        System.out.println(media);


        if(valorMedio == num) {

            return media;

        }
        if(valorMedio < num) {

            return buscaBinariaRecursiva(sequencia, num, media + 1, fim);
        } else {

            return buscaBinariaRecursiva(sequencia, num, inicio, media - 1);
        }
    }
}