/**
 * Classe que representa um filme, que foi lançado em um ano.
 * 
 * @author Lucas de Medeiros
 */
public class Filme {

    private String nome;
    private int ano;

    /**
     * Construtor a partir do nome a ano do filme.
     * 
     * @param nome nome do filme
     * @param ano ano do filme
     */
    public Filme(String nome, int ano) {
        this.nome = nome;
        this.ano = ano;
    }

    // Getters para ano e nome

    public int getAno() {
        return ano;
    }

    public String getNome() {
        return nome;
    }

    // Reescrevendo toString
    @Override
    public String toString() {
        return this.nome + " - " + this.ano;
    }
}