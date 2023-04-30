package EDA;

import java.util.Scanner;

class ElementosDuplicados {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        String entrada = sc.nextLine();

        String[] elementos = entrada.split(" ");

        System.out.println(duplicado(elementos));



    }


    public static boolean duplicado(String[] elementos) {
        for (int i = 0; i < elementos.length; i ++) {
            for (int j = i + 1; j < elementos.length; j ++) {
                if (elementos[i].equals(elementos[j])) {
                    return true;
                }

            }
        }
        return false;
    }


}
