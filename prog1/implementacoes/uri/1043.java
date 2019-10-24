import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
			
		String[] stringsEntradas = teclado.nextLine().split(" ");
		double[] entradas = ConverteEntrada(stringsEntradas);
		String resp;		
		if(isTriangulo(entradas)) {
			resp = calculaTriangulo(entradas);
		} else {
			resp = calculaTrapesio(entradas);
		}
		System.out.println(resp);
	}

	private static double[] ConverteEntrada(String[] stringsEntradas) {
		double[] resp = new double[stringsEntradas.length];
		for (int i = 0; i < stringsEntradas.length; i++) {
			resp[i] = Double.parseDouble(stringsEntradas[i]);
		}
		return resp;
	}

	private static boolean isTriangulo(double[] entradas) {
		boolean resp = false;
		if (entradas[0] + entradas[1] > entradas[2] &&
				entradas[0] + entradas[2] > entradas[1] &&
						entradas[1] + entradas[2] > entradas[0]) {
			resp = true;
		}
		return resp;
	}

	private static String calculaTriangulo(double[] entradas) {
		return String.format("Perimetro = %.1f", (entradas[0]+ entradas[1] + entradas[2]));
	}

	private static String calculaTrapesio(double[] entradas) {
		return String.format("Area = %.1f", ((entradas[0]+ entradas[1])*entradas[2])/2);
	}
}

