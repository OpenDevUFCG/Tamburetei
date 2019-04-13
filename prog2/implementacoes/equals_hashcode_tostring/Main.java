import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Classe principal para exemplificar os métodos equals, hashCode
 * e toString.
 * 
 * @author Lucas de Medeiros
 */

public class Main {

	public static void main(String[] args) {
		Pessoa pessoa1 = new Pessoa("Lucas", "65314789650", 20);

		// USO DE TOSTRING()

		System.out.println(pessoa1.toString()); 
		// imprime representação em string de uma pessoa.

		System.out.println(pessoa1); 
		// equivalente à de cima, pois aqui o método toString é chamado por padrão.

		// USO DE EQUALS()

		Pessoa pessoa2 = new Pessoa("Lucas", "65314789650", 20);
		Pessoa pessoa3 = new Pessoa("Lucas", "65314789650", 19);
		Pessoa pessoa4 = new Pessoa("Lucas", "57695421507", 20);
		Pessoa pessoa5 = new Pessoa("Aderbaldo", "65314789650", 20);

		System.out.println(pessoa1.equals(pessoa2)); // true
		System.out.println(pessoa1.equals(pessoa3)); // true

		/*
			Note que duas pessoas, mesmo tendo idades diferentes, vão ser
			iguais por causa da implementação do equals na classe Pessoa.
		*/

		System.out.println(pessoa1.equals(pessoa4)); // false
		System.out.println(pessoa1.equals(pessoa5)); // false

		// USO DE HASHCODE

		Set<Pessoa> set = new HashSet<>();
		set.add(pessoa1);
		set.add(pessoa2);
		set.add(pessoa3);
		set.add(pessoa4);
		set.add(pessoa5);

		/*
			Como pessoa1, pessoa2 e pessoa3 são iguais pelo equals(),
			o hashCode delas será igual, então ao adicionar em um
			HashSet, por exemplo, que não tem elementos repetidos e
			internamente faz a checagem pelo hashCode, só serão
			adicionados de fato pessoa1, pessoa4 e pessoa5.
		*/

		System.out.println(set.size()); // 3
		System.out.println(Arrays.toString(set.toArray()));
		// imprime a representação em string o conjunto.
	}
}
