package EDA;

import java.util.Arrays;
import java.util.Scanner;

class InsereOrdenadoUltimo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] arrayString = sc.nextLine().split(" ");

        int[] array = new int[arrayString.length];

        for (int i = 0; i < arrayString.length; i ++) {
            array[i] = Integer.parseInt(arrayString[i]);
        }

        insereOrdenadoUltimo(array, 1);

    }


    public static void insereOrdenadoUltimo(int[] array, int i) {

        int j = i;
        while (j > 0 && array[j] < array[j - 1]) {
            swap(array, j, j - 1);
            j -= 1;
        }

        if (i + 1 < array.length) {
            insereOrdenadoUltimo(array, i + 1);
            System.out.println(Arrays.toString(array));
        }
    }


    public static void swap(int[] array, int i, int j) {
        int aux = array[i];
        array[i] = array[j];
        array[j] = aux;

    }
}