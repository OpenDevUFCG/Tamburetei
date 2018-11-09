/**
 * Classe responsável pela representação de uma pessoa no sistema.
 * 
 * @author Lucas de Medeiros
 */

public class Pessoa {
	
	private String nome;
	private String cpf;
	private int idade;
	
	/**
	 * Constrói uma nova instância de Pessoa no sistema, a partir de um nome, 
	 * CPF e idade.
	 * 
	 * @param nome nome da pessoa.
	 * @param cpf CPF da pessoa.
	 * @param idade idade da pessoa.
	 */
	public Pessoa(String nome, String cpf, int idade) {
		this.nome = nome;
		this.cpf = cpf;
		this.idade = idade;
	}

	/**
	 * Sobrescrita do método hashCode, que vai gerar um número inteiro único a 
	 * partir dos campos CPF e nome.
	 */
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((cpf == null) ? 0 : cpf.hashCode());
		result = prime * result + ((nome == null) ? 0 : nome.hashCode());
		return result;
	}

	/**
	 * Sobrescrita do método equals, que vai comparar uma instância de pessoa
	 * com alguma outra instância. Retorna <tr>true</tr> se as instâncias
	 * forem iguais, <tr>false</tr>, caso contrário.
	 */
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pessoa other = (Pessoa) obj;
		if (cpf == null) {
			if (other.cpf != null)
				return false;
		} else if (!cpf.equals(other.cpf))
			return false;
		if (nome == null) {
			if (other.nome != null)
				return false;
		} else if (!nome.equals(other.nome))
			return false;
		return true;
	}

	/**
	 * Sobrescrita do método toString, que vai retornar uma representação em
	 * String de uma instância de Pessoa, a partir de seus três campos: nome, 
	 * CPF e idade.
	 */
	@Override
	public String toString() {
		return "Nome: " + this.nome + ", CPF: " + this.cpf + ", Idade: " + this.idade + " anos.";
	}
}
