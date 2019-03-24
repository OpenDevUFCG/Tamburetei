/**
 * Classe que representa um filme, que foi lançado em um ano.
 * 
 * Implementa a interface Comparable, pois assim será possível se comparar
 * em relação a outros filmes.
 * 
 * @author Lucas de Medeiros
 */
public class Filme implements Comparable<Filme> {

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
    
    /**
     * Reescrevendo o método compareTo, que será usado para ordenar
     * filmes por ano.
     * 
     * @param filme filme a ser comparado
     * @return inteiro que representa qual dos dois é o maior, ou igual
     */
    @Override
    public int compareTo(Filme filme) {
        return this.ano - filme.ano;
    }

    // Reescrevendo toString
    @Override
    public String toString() {
        return this.nome + " - " + this.ano;
    }
}