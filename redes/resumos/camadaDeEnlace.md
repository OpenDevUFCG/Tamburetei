# Camada De Enlace

## Sumário
- [Camada De Enlace](#camada-de-enlace)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Serviços](#serviços)


## Introdução

A camada de enlace tem como responsabilidade de transferir um datagrama de um nó para o nó adjacente sobre um enlace. Os protocolos e padrões desta camada, diferente das camadas superiores que são baseados em RFCs, estes geralmente são definidos por empresas de comunicações ou organizações de engenharias (Como ANSI, IEEE e ITU). Os serviços e especificações desta camada são geridos por múltiplos padrões de acordo com a tecnologia e o meio físico utilizado e integrado por tais protocolos, sendo alguns deles utilizados para ligar os serviços da camada de enlace com a camada física.

## Serviços

* **Enquadramento de dados**
  * **Encapsula datagramas em quadros acrescentando cabeçalhos e trailer**;
  * **Delimitação dos quadros:**
    *	Contador de caracteres;
    *	Caracteres de inicialização e finalização, com carácter de preenchimento;
    *	Flags de inicialização e finalização, com carácter de enchimento.
*	**Transferência dados da camada de rede da máquina de origem para a camada de rede do destino**
  *	**Não orientados a conexões e sem reconhecimento**
    *	Quadros independentes
    *	Indicado para taxa de erros muito baixa ou tráfego em tempo real
  *	**Não orientados a conexões e com reconhecimento**
    *	Quadros confirmados individualmente
    *	Útil em canais não confiáveis (ex.: sistemas sem fio)
  *	**Orientados a conexões e com reconhecimento**
    *	Estabelecimento de conexão antes da transferência de dados
	  * Quadros confirmados individualmente
	  * Garante que cada quadro será recebido uma única vez e na ordem correta
*	**Detecção e Correção de erros**
  * **Verificação de Paridade**
    *	Paridade com bit único: Detecta erro de um único bit
    *	Paridade bidimensional: Detecta e corrige erro de um único bit
  * **Código de hamming:**
    *	Dada uma palavra código: n = m + r
    *	Os r bits de verificação ocupam as posições que são potências de 2
    *	Os outros (3, 5, 6, 7, 9, etc.) são preenchidos com os m bits de dados.
    *	Os bits de verificação resultam de um XOR das posições de influência
  * **Código Polinomial ou Código de Redundância Cíclica (CRC)**
    *	Transmissor e receptor devem concordar em relação a um polinômio gerador, G(x), antecipadamente. E tanto o bit de mais alta ordem quanto o de mais baixa ordem do polinômio gerador devem ser iguais a 1.
    *	G(x) é usado junto a informação no transmissor gerando uma nova sequência de dados a ser enviado, M(x)
    *	Se M(x) ao chegar no receptor, não for divisível pelo polinômio gerador, significa que houve erro de transmissão.
    *	Algoritmo
      *	Seja G(x) o gerador polinomial de grau r. 
      *	Acrescente r bits 0 ao quadro que será transmitido
      *	Divida o novo quadro pelo gerador G(x)
      *	Subtraia do quadro original o resto da divisão
*	**Controle de fluxo**
  * Limitação da transmissão entre transmissor e receptor
  * O receptor avisa quando o transmissor pode enviar um quadro

## Procolos para controle de fluxo:

### Simplex sem restrições:
* Transmissão de dados em um único sentido;
* Camada de redes sempre pronta;
* Buffer infinito no qual poderão ser armazenados todos os quadros recebidos enquanto eles aguardam para serem processados;
* Não há perda de quadros.

### Simplex Stop-and-wait:
* Os buffers não são infinitos;
* O tempo de processamento não é ignorado;
* O transmissor não envia outra mensagem até que a anterior tenha sido aceita como correta pelo receptor;
* Embora o tráfego de dados seja simplex, há fluxo de quadros em ambos os sentidos.
* **Problema:** impedir que o transmissor inunde o receptor com dados, mais rapidamente do que este é capaz de processá-los.
* **Solução:** fazer o receptor enviar uma resposta para o transmissor, autorizando o envio do próximo quadro.

### Simplex para um Canal com Ruído:
* O transmissor transmite um quadro que é numerado sequencialmente;
* O receptor envia um quadro de reconhecimento se o quadro for recebido corretamente, caso contrário, há um descarte e é aguardada uma retransmissão;
* Quadros não reconhecidos são retransmitidos (timer).

### Protocolos de Janela Deslizante:
* **Piggybacking:** técnica de retardar temporariamente as confirmações de recebimento de um quadro e enviá-las junto com o próximo quadro de dados. 
  * **Como funciona?**
    *	Quando um quadro de dados chega a seu destino, em vez de enviar imediatamente um quadro de controle separado, o receptor se contém e espera até a camada de rede enviar o próximo quadro. A confirmação é acrescentada ao quadro de dados que está sendo enviado (por meio do campo ack do cabeçalho de quadro). Na verdade, a confirmação pega carona no próximo quadro de dados que estiver sendo enviado. 
  * **Vantagens:** 
    *	Melhor utilização da largura de banda disponível para o canal
    *	Menor número de quadros enviados, que implica em menor quantidade de buffers no receptor, dependendo da forma como o software do receptor está organizado
  * **Desvantagem:**
    *	A camada de enlace não sabe quanto tempo deve esperar por um quadro para enviar a confirmação. Se esperar por um tempo maior que o timeout do transmissor, o quadro será transmitido novamente, o que invalidará todo o processo de confirmação.

### Janela Deslizante:
É um protocolo bidirecional, no qual cada quadro enviado contém um número de sequência, variando desde 0 até algum valor máximo. Em geral, o valor máximo e 2n –1, de forma que o número de sequência caiba exatamente em um campo de n bits. 

> ### Janela deslizante de 1 bit:
> Esse tipo de protocolo utiliza o stop-and-wait, pois o transmissor envia um quadro e aguarda sua confirmação antes de enviar o quadro seguinte. 
> O campo de confirmação no quadro contém o número do último quadro recebido sem erro. Se esse número estiver de acordo com o número de sequência do quadro que o transmissor está tentando enviar, o transmissor saberá que já cuidou do quadro armazenado em buffer e poderá buscar o pacote seguinte em sua camada de rede. Se o número de sequência for discordante, o transmissor deve continuar tentando enviar o mesmo quadro. Sempre que um quadro é recebido, um outro quadro também é enviado de volta.

### Pipeline:
Técnica baseada em permitir que o transmissor envie até w quadros antes do bloqueio, e não apenas 1. Com uma escolha apropriada de w, o transmissor será capaz de transmitir quadros continuamente durante um tempo igual ao tempo de trânsito da viagem de ida e volta, sem ocupar a janela toda. 

> “O que fazer se um quadro no meio da janela for danificado ou perdido? ”

> **Estratégias básicas para lidar com erros na presença do pipelining**:
> **Go Back N**
>   * O destino descarta qualquer pacote fora de ordem; portanto, não necessita de um buffer.