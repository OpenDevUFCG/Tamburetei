/**
 * Classe que é responsável pela gerenciamento de animais, representando, assim,
 * o controlador do PetShop.
 * 
 * @author Lucas de Medeiros
 */

public class PetShop {
	
	private static int TAMANHO_ARRAY_ANIMAIS = 5;
	private Animal[] animais;
	private int totalAnimaisCadastrados;
	
	/**
	 * Constrói o PetShop, inicializando o array de animais, com tamanho fixo
	 * igual a 5, como definido em alguma especificação.
	 */
	public PetShop () {
		animais = new Animal[TAMANHO_ARRAY_ANIMAIS];
		totalAnimaisCadastrados = 0;
	}
	
	/**
	 * Esse método cadastra um novo animal no sistema. No sistema, só são
	 * permitidos animais com nomes diferentes, independentemente de suas
	 * espécies.
	 * 
	 * @param nome nome do animal.
	 * @param especie espécie do animal.
	 * @param idade idade do animal.
	 * @return <tr>true</tr> se o animal foi cadastrado com sucesso, caso 
	 * contrário, <tr>false</tr>.
	 */
	public boolean cadastrarAnimal(String nome, String especie, int idade) {
		int total = this.totalAnimaisCadastrados();
		boolean cadastrou = false;
		
		if (total < TAMANHO_ARRAY_ANIMAIS && !animalExiste(nome)) {
			this.animais[total] = new Animal(nome, especie, idade);
			cadastrou = true;
			atualizaTotal();
		}
		
		return cadastrou;
	}

	/**
	 * Esse método itera sobre o array de animais para verificar a existência de um
	 * animal com o nome especificado.
	 * 
	 * @param nome nome do animal.
	 * @return <tr>true</tr> se o animal existe, caso contrário, <tr>false</tr>.
	 */
	public boolean animalExiste(String nome) {
		boolean existe = false;
		
		if (nome != null) {
			for (int i = 0; i < TAMANHO_ARRAY_ANIMAIS; i++) {
				if (this.animais[i] != null &&
						this.animais[i].getNome().toLowerCase().equals(nome.toLowerCase())) {
					existe = true;
				}
			}
		}
		
		return existe;
	}
	
	/**
	 * Esse método itera sobre o array de animais para saber a média de idade dos
	 * animais cadastrados no PetShop.
	 * 
	 * @return double que representa a média de idade dos animais cadastrados no 
	 * sistema.
	 */
	public double mediaIdade() {
		double media = 0.0;
		int total = totalAnimaisCadastrados();
		
		if (total > 0) {
			int soma = 0;
			
			for (int i = 0; i < TAMANHO_ARRAY_ANIMAIS; i++) {
				if (this.animais[i] != null) {
					soma += animais[i].getIdade();
				}
			}
			
			media = ((double) soma / total);
		}
		
		return media;
	}
	
	/**
	 * Esse método retorna o número de animais que foram cadastrados no PetShop.
	 * 
	 * @return inteiro que representa o total de animais cadastrados no sistema.
	 */
	public int totalAnimaisCadastrados() {
		return this.totalAnimaisCadastrados;
	}
	
	/**
	 * Esse método atualiza a contagem de animais cadastrados no sistema,
	 * sempre aumentando de um em um.
	 */
	private void atualizaTotal() {
		this.totalAnimaisCadastrados++;
	}

}
