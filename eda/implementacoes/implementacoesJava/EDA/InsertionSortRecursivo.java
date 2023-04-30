package EDA;

import java.util.Scanner;
import java.util.Arrays;

class InsertionSortRecursivo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String entrada = sc.nextLine();

        String[] arrayString = entrada.split(" ");

        int[] array = new int[arrayString.length];

        for (int i = 0; i < arrayString.length; i ++) {
            array[i] = Integer.parseInt(arrayString[i]);
        }

        insertionRecursive(array, 1);
        System.out.println(Arrays.toString(array));
    }


    public static void insertionRecursive(int[] array, int i) {

        int j = i;
        while (j > 0 && array[j] < array[j - 1]) {
            swap(array, j, j - 1);
            j -= 1;
        }

        if (i + 1 < array.length) {
            System.out.println(Arrays.toString(array));
            insertionRecursive(array, i + 1);
        }
    }


    public static void swap(int[] array, int i, int j) {
        int aux = array[i];
        array[i] = array[j];
        array[j] = aux;

    }

    /**
     * Insertion Sort Iterativo
     * @param array valores a serem ordenados
     */
    public static void insertionSort(int[] array) {

        for (int i = 1; i < array.length; i ++) {
            int j = i;

            while (j > 0 && array[j] < array[j - 1]) {
                swap(array, j, j - 1);
                j -= 1;
            }
        }
    }

}