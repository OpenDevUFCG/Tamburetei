# Autômatos Finitos

Enquanto as máquinas de estado são capazes apenas de acompanhar os estados do sistema, um **autômato finito (AF)** é uma máquina que resolve algum problema, aceitando ou recusando a cadeia utilizada como entrada. Assume-se que os autômatos finitos são compostos por uma unidade de controle e uma fita na qual realiza a leitura da cadeia de entrada, que será aceita ou rejeitada.

Para que possa alcançar a **aceitação** da cadeia de entrada, é necessário que o autômato possua pelo menos um **estado final**. Se, ao termino do processamento de uma certa cadeia, o autômato tiver um de seus estado finais como estado atual, diz-se que a cadeia foi aceita. Caso contrário, diz-se que a cadeia foi rejeitada (**rejeição**). Dessa forma, um autômato não precisa ter estados finais, porém, sem eles torna-se inútil.

Dá-se o nome de **classe de linguagem** a todas as linguagens que podem ser resolvidas por um mesmo tipo de máquina. A classe que contém todas as linguagens que podem ser resolvidas por autômatos finitos chama-se **classe das linguagens regulares**.

## Autômatos Finitos Determinísticos

A definição formal de um **autômato finito determinístico (AFD)** é uma 5-tupla **<Q, Σ, δ, q0, F>**, tal que:

- **Q** é um conjunto finito e não-vazio, chamado de conjunto de estados.
- **Σ** é um conjunto finito e não-vazio, chamado de alfabeto.
- **δ: Q × Σ → Q** é a função (total) de transição do autômato.
- **q0** ∈ Q é o estado inicial do autômato.
- **F** ∈ Q é o conjunto de estados finais do autômato.

A **função de transição** é responsável por descrever as mudanças de estados a partir do estado atual e do símbolo recebido na entrada. O **diagrama de estados** é a representação gráfica do autômato. É possível gerar o diagrama de estados a partir da definição formal do autômato finito e vice-versa.

Na Teoria da Computação, os objetos de estudo são as **linguagens** e as ferramentas são as operações exclusivas para manipulação de linguagens. As **operações regulares** são a união (∪), a concatenação (•) e a estrela (*), descritas por:

```
- A ∪ B = { x | x ∈ A ou x ∈ B }
- A • B = { xy | x ∈ A e y ∈ B }
- A* = { x1, x2, ..., xk | xi ∈ A e k ≥ 0 }
```

Porém existem outras operações abordadas durante a disciplina como o complemento, a intersecção, a subtração, etc. Se uma operação realizada sobre uma linguagem da classe C sempre gera uma linguagem da mesma classe, diz-se que a classe é **fechada** por esta operação.

O símbolo *lambda* (**λ**) representa a palavra vazia (ou nula), em alguns livros utiliza-se o épsilon (**ε**). Já **Σ*** denota o alfabeto binário.

## Autômatos Finitos Não-Determinísticos

Enquanto nos AFDs os estados e as transições são bem determinadas, em um **autômato finito não-determinístico (AFND)** podem existir múltiplas possibilidades para o próximo estado dado um mesmo símbolo, assim, ele torna-se capaz de explorar diversas possibilidades simultaneamente. Formalmente, difere dos AFDs apenas por sua função da transição, que é da forma **δ: Q × Σε → Q**.

Nos AFNDS, um estado pode ter zero ou mais transições para cada símbolo do alfabeto e zero ou mais transições para o símbolo **ε** (ou **λ** em outras notações). Os arcos rotulados com **ε** indicam que é possível realizar aquela transição sem consumir símbolos da cadeia de entrada. 

É importante compreender que todo autômato determinístico é um autômato não-determinístico e, portanto, o não-determinismo não representa um aumento de capacidade dos autômatos.