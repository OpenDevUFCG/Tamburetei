import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
    Scanner entrada = new Scanner(System.in);
    String[] entradas = entrada.nextLine().split(" ");
    int[] entradasInteiros = new int[3];
    entradasInteiros[0] = Integer.parseInt(entradas[0]);
    entradasInteiros[1] = Integer.parseInt(entradas[1]);
    entradasInteiros[2] = Integer.parseInt(entradas[2]);

    Arrays.sort(entradasInteiros);

    for (int i: entradasInteiros) {
      System.out.println(i);
    }
    System.out.println("");
    for (String i: entradas) {
      System.out.println(i);
    }
    }
 
}
