package EDA;

import java.util.Scanner;
import java.lang.Math;

class TeoremaDoMestre {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String entrada = sc.nextLine();
        String[] aux = entrada.split(" ");

        int a = Integer.parseInt(aux[0]);
        int b = Integer.parseInt(aux[1]);
        int ord = Integer.parseInt(aux[2]);

        double razao = Math.log10(a)/Math.log10(b);

        if(ord < razao) {
            System.out.println("T(n) = theta(n**" + razao + ")");
        } else if (ord == razao) {
            System.out.println("T(n) = theta(n**" + ord + " * log n)");
        } else if (ord > razao) {
            System.out.println("T(n) = theta(n**" + ord + ")");
        }
    }

}