/**
 * Classe responsável pela representação de um animal cadastrado no PetShop.
 * 
 * @author Lucas de Medeiros
 */
public class Animal {
	
	private static int IDADE_ZERO = 0;
	
	private String nome;
	private String especie;
	private int idade;
	
	/**
	 * Constrói um novo animal a partir do seu nome, espécie e idade.
	 * 
	 * @param nome nome do animal.
	 * @param especie espécie do animal.
	 * @param idade idade do animal.
	 * @throws IllegalArgumentException.
	 */
	public Animal (String nome, String especie, int idade) throws IllegalArgumentException {
		if (nome == null || nome.trim().isEmpty())
			throw new IllegalArgumentException("Erro ao cadastrar animal: nome inválido.");
		
		if (especie == null || especie.trim().isEmpty())
			throw new IllegalArgumentException("Erro ao cadastrar animal: raça inválida.");
		
		if (idade < IDADE_ZERO)
			throw new IllegalArgumentException("Erro ao cadastrar animal: idade inválida.");
		
		this.nome = nome;
		this.especie = especie;
		this.idade = idade;
	}
	
	// Getters que serão necessários na classe PetShop.

	public String getNome() {
		return nome;
	}
	
	public int getIdade() {
		return idade;
	}
	
	// Sobrescrita dos métodos hashCode() e equals()

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((especie == null) ? 0 : especie.hashCode());
		result = prime * result + ((nome == null) ? 0 : nome.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Animal other = (Animal) obj;
		if (especie == null) {
			if (other.especie != null)
				return false;
		} else if (!especie.equals(other.especie))
			return false;
		if (nome == null) {
			if (other.nome != null)
				return false;
		} else if (!nome.equals(other.nome))
			return false;
		return true;
	}
	
}