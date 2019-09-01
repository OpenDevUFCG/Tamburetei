# Resumo de Condição de Corrida

Neste resumo, será abordada a **Condição de Corrida**, que pode ser inicialmente resumida como uma situação onde os eventos que ocorrem podem influenciar na execução de processos, especialmente quando existem vários fluxos de execução "simultâneos", e também soluções para esse problema.

## Região Crítica

A região crítica de um determinado processo é a parte de seu código que acessa a **Área de Memória Compartilhada**, que, como o próprio nome sugere, é um conjunto de recursos que podem ser compartilhados entre dois ou mais processos, por exemplo, memória, variáveis, arquivos, etc. Essa área depende expressivamente que a parte do processo que a acessa tenha sua execução de forma sequencial, e esse é um dos principais fatores que influenciam para a ocorrência de uma condição de corrida.

Para entender possíveis problemas que podem acontecer com vários processos operando sobre uma mesma Área de Memória Compartilhada, imagine a seguinte situação: um usuário possui uma conta no banco que tem R$ 1.000,00. Ele deseja fazer uma compra de R$ 100,00 com seu cartão de débito e, ao mesmo tempo, ele recebe seu pagamento mensal de R$ 3.500,00. Neste caso, existirão dois processos concorrentes, um que vai retirar 100 reais de sua conta, e outro que vai adicionar 3500.

Como o sistema operacional do banco implementa o pseudo-paralelismo, ele tem que realizar o chaveamento de processos. Imagina que o primeiro processo faz a diferença, verifica que o novo saldo é de 900 reais, e no instante em que ele vai fazer a atualização desse valor, a CPU o interrompe e faz o chaveamento para o outro processo que adiciona 3500 reais em sua conta. Para esse outro processo, o valor ainda é 1000, então quando fizer a soma, vai ficar 4500 reais na conta do usuário. Porém, quando esse segundo processo parar de executar, e o anterior ganhar a CPU novamente, ele não terá a informação da atualização do e vai salvar como 900 reais.

Ou seja, o saldo final desse usuário ficará R$ 900,00. Isso dá a impressão que o sistema "ignorou" o pagamento recebido pelo usuário, já imaginou a confusão que isso causaria?

## Quando acontece?

Para existir uma condição de corrida, é necessário que vários fluxos de execução (processos ou *threads*) operem sobre tais recursos compartilhados e, quando um desses fluxos vai executar pressupondo um estado inicial dos recursos, algo acontece entre a obtenção de tal estado, alterando-o, e a execução final.

É importante ter em mente que a condição de corrida **não é um erro**, e sim inerente a alguns problemas, e não há como fugir. O possível erro ocasionado por uma condição de corrida só ocorre se não for devidamente tratado.

## Soluções para condições de corrida

Para evitar que erros aconteçam devido a vários fluxos de execução operando sobre uma mesma área de memória compartilhada, devemos garantir:

- A exclusão mútua, que é a certeza de que, caso exista um processo executando sua região crítica, nenhum outro processo vai poder executar a sua até que o primeiro termine sua execução.
- A não existência de hipótese sobre a velocidade da CPU. Por exemplo, implementar uma solução que só é possível de funcionar caso a velocidade da CPU na qual estão sendo executados os processos seja X.
- Que nenhum fluxo deve ser impedido de entrar na região crítica, caso outro fluxo não esteja utilizando a sua.
- Que não exista *starvation*, ou seja, que um processo morra porque não ganhou a CPU em nenhum momento.

### Busy wait (espera ocupada)

Uma solução baseada em espera ocupada consiste em: o fluxo de execução, antes de entrar na região crítica, precisa passar por uma verificação para saber se ele pode ou não entrar lá. Caso não possa e já exista outro processo executando sua região crítica, ele fica em loop até que ele possa ganhar essa região.

Um dos exemplos mais conhecidos de solução para condição de corrida que implementa a espera ocupada é a **Solução de Peterson** ou **Algoritmo de Peterson**. O código abaixo exemplifica como essa solução pode ser implementada para resolver esse problema com dois fluxos alternativos de execução:

```c
// suponha que existam dois processos, i = 0 e j = 1

int vez = 0; // indica de quem é a vez
bool interessado[2]; // array que indica quem está interessado em acessar a região crítica

// Código de entrada na região crítica
void entraNaRegiaoCritica(int processo) {
  int other = 1 - processo; // representa o outro processo
  vez = processo;
  interessado[processo] = true;
  while(vez == processo && interessado[other] == true); // fica em loop, caso não possa entrar
}

// Código para saída da região crítica
void saiDaRegiaoCritica(int processo) {
  interessado[processo] = false; // indica que o processo que estava na região crítica terminou sua atividade.
}

// Código que exemplifica o 'main' em um dos fluxos de execução
int main() {
  int ID = 1;

  entraNaRegiaoCritica(ID);
  acessaArquivoCompartilhado(); // código de acesso à região crítica.
  saiDaRegiaoCritica(ID);

  return 0;
}
```

***TODO: Explicar e exemplificar outros códigos para resolução de condição de corrida***
