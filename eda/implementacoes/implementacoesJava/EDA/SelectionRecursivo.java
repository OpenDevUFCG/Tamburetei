package EDA;

import java.util.Scanner;
import java.util.Arrays;

class SelectionRecursivo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String entrada = sc.nextLine();

        String[] arrayString = entrada.split(" ");

        int[] array = new int[arrayString.length];

        for (int i = 0; i < arrayString.length; i ++) {
            array[i] = Integer.parseInt(arrayString[i]);
        }

        selectionRecursive(array, 0, array.length);
        System.out.println(Arrays.toString(array));

    }


    public static void selectionRecursive(int[] array, int i, int tam) {
        int min = i;

        for (int j = i + 1; j < tam; j ++) {
            if (array[j] < array[min]) {
                min = j;
            }
        }

        swap(array, min, i);


        if (i + 1 < tam - 1) {
            System.out.println(Arrays.toString(array));
            selectionRecursive(array, i + 1, tam);
        }

    }

    public static void swap(int[] array, int i, int j) {
        int aux = array[i];
        array[i] = array[j];
        array[j] = aux;

    }

    /**
     * Selection Sort Iterativo
     * @param array array a ser ordenado
     */
    public static void selectionSort(int[] array){
        for (int i = 0; i < array.length; i ++) {
            int menorIndice = i;
            for (int j = i + 1; j < array.length; j ++) {
                if (array[j] < array[menorIndice]) {
                    menorIndice = j;
                }
            }
            swap(array, i, menorIndice);
        }
    }
}