import java.util.Arrays;
import java.util.Scanner;

class CountingSortPassoAPasso {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		String[] numeros = entrada.nextLine().split(" ");
		int maiorElemento = entrada.nextInt();
		int[] array = new int[numeros.length];

		for(int i = 0; i < numeros.length; i++) {
			array[i] = Integer.parseInt(numeros[i]);
		}

		countingSort(array, maiorElemento);
	}

	public static String pegaString(int[] array) {
		String stringFrequencia = "";
		stringFrequencia = Arrays.toString(array);
		stringFrequencia = stringFrequencia.substring(1,stringFrequencia.length() - 1).replaceAll(", ", " ");
		return stringFrequencia;
	}
	
	public static void countingSort(int[] array, int k) {
		int[] b = new int[array.length];
		int[] recorrencias = new int[k + 1];
		for(int i = 0; i < array.length; i++) {
			recorrencias[array[i]] += 1; 
			System.out.println(pegaString(recorrencias));
		}
		for(int i = 1; i < recorrencias.length ; i ++) {
			
			recorrencias[i] = recorrencias[i] + recorrencias[i - 1];
		}
		System.out.println("Cumulativa do vetor de contagem - " + pegaString(recorrencias));
		for(int i = array.length - 1; i >= 0; i --) {
			b[recorrencias[array[i]] - 1] = array[i];
			recorrencias[array[i]] -=1;
		}
		System.out.println(pegaString(recorrencias));
		System.out.println(pegaString(b));
	}
}