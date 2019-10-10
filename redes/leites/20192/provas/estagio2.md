# 1ª Prova

- **Disciplina:** Redes de Computadores
- **Período:** 2019.2

## Aviso!

1. As questões apresentadas a seguir são descrições baseadas em relatos de um ou mais alunos que fizeram tal avaliação. Logo, não há garantia de que os enunciados sejam iguais aos originais, tampouco que estejam livres de erros. Esteja ciente dessas considerações ao utilizar esse material!

2. A prova teve questões discursivas e de múltipla escolha. As questões a seguir são apenas as discursivas.

## Questões

#### Questão 1 

Algumas vezes, durante uma transferência de arquivos (usando HTTP, por exemplo), a taxa de transmissão de dados praticamente chega a zero. Comente algumas razões que podem causar esse comportamento.

#### Questão 2 

Na camada de transporte do modelo TCP/IP pode-se utilizar os protocolos TCP e UDP. Qual a diferença entre eles? Quais as vantagens de um em relação ao outro?

#### Questão 3

O protocolo TCP realiza todo o controle da comunicação, inclusive evitando a sobrecarga da rede através de mecanismos de controle de congestionamento e de fluxo. Considerando a maneira como o TCP implementa esses mecanismos, explique como é a coexistência entre várias aplicações que fazem uso de TCP rodando em paralelo em uma mesma rede.

#### Questão 4

Quais são as duas fases que o protocolo TCP usa dentro de uma conexão para controlar o congestionamento? Como elas se alternam?

### Questão 5

Um aluno resolveu implementar uma variação do mecanismo de controle de congestionamento do TCP fazendo duas alterações:

1. Iniciar a janela de congestionamento com o tamanho de 16 MSS.
2. Ao detectar uma falha por *timeout*, reduzir o tamanho da janela de congestionamento para metade do valor do limiar reajustado.

Ao testar sua implementação, ele identificou que conseguiu uma melhora de desempenho em relação ao que estava tendo anteriormente. Por que isso aconteceu?

### Questão 6

Assuma protocolo TCP com retransmissão rápida e limiar inicial de 100 segmentos. Mostre a evolução da janela e do limiar de congestionamento em função da rodada de transmissão considerando os seguintes eventos (assuma `JANELA = 1` para `RODADA = 1`):

1. Logo após a quinta rodada, a fonte assume a perda de segmento por um esgotamento de temporização (*timeout*).
2. Logo após a décima rodada, a fonte assume a perda de segmento devido a recepção de três confirmações duplicadas.
3. Após a décima quinta rodada, a conexão TCP é encerrada.
