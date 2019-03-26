# Camada De Enlace

## Sumário
- [Camada De Enlace](#camada-de-enlace)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Serviços](#serviços)
  - [Procolos para controle de fluxo](#protocolos-para-controle-de-fluxo)
    - [Simplex sem restrições](#simplex-sem-restrições)
    - [Simplex Stop-and-wait](#simples-stop)
    - [Simplex para um Canal com Ruído](#simplex-para)
    - [Protocolos de Janela Deslizante](#protocolos-de-janela)
    - [Janela Deslizante](#janela-deslizante)
    - [Janela Deslizante de 1 bit](#janela-deslizante-de-1-bit)
    - [Pipeline](#pipeline)
      - [Estratégias básicas para lidar com erros na presença do pipelining](#estratégias-básicas)
  - [Protocolos de acesso a meio compartilhado](#protocolo-de-acesso)
    - [Protocolos MAC](#protocolos-mac)
    - [Particionamento de canal](#particionamento-de-canal)
    - [Passagem de permissão](#passagem-de-permissão)
    - [Protocolo MAC de acesso aleatório ](#protocolo-mac-de-acesso-aleatório)
    - [ALOHA](#aloha)
    - [Slotted ALOHA](#slotted-aloha)
    - [CSMA](#csma)
    - [CSMA/CD](#csma/cd)
    - [Ethernet](#ethernet)
    - [IEEE 802.11 LAN sem fio](#ieee)
    - [Canais e associação](#canais-e-associação)
    - [O protocolo mac 802.11](#o-protocolo-mac)

## Introdução

A camada de enlace tem como responsabilidade de transferir um datagrama de um nó para o nó adjacente sobre um enlace. Os protocolos e padrões desta camada, diferente das camadas superiores que são baseados em RFCs, estes geralmente são definidos por empresas de comunicações ou organizações de engenharias (Como ANSI, IEEE e ITU). Os serviços e especificações desta camada são geridos por múltiplos padrões de acordo com a tecnologia e o meio físico utilizado e integrado por tais protocolos, sendo alguns deles utilizados para ligar os serviços da camada de enlace com a camada física.

## Serviços

* **Enquadramento de dados**
  * **Encapsula datagramas em quadros acrescentando cabeçalhos e trailer**;
  * **Delimitação dos quadros:**
    *	Contador de caracteres;
    *	Caracteres de inicialização e finalização, com carácter de preenchimento;
    *	Flags de inicialização e finalização, com carácter de enchimento.
* **Transferência dados da camada de rede da máquina de origem para a camada de rede do destino**
  * **Não orientados a conexões e sem reconhecimento**
    * Quadros independentes
    * Indicado para taxa de erros muito baixa ou tráfego em tempo real
  * **Não orientados a conexões e com reconhecimento**
    * Quadros confirmados individualmente
    * Útil em canais não confiáveis (ex.: sistemas sem fio)
  * **Orientados a conexões e com reconhecimento**
    * Estabelecimento de conexão antes da transferência de dados
	  * Quadros confirmados individualmente
	  * Garante que cada quadro será recebido uma única vez e na ordem correta
* **Detecção e Correção de erros**
  * **Verificação de Paridade**
    * Paridade com bit único: Detecta erro de um único bit
    * Paridade bidimensional: Detecta e corrige erro de um único bit
  * **Código de hamming:**
    * Dada uma palavra código: n = m + r
    * Os r bits de verificação ocupam as posições que são potências de 2
    * Os outros (3, 5, 6, 7, 9, etc.) são preenchidos com os m bits de dados.
    * Os bits de verificação resultam de um XOR das posições de influência
  * **Código Polinomial ou Código de Redundância Cíclica (CRC)**
    * Transmissor e receptor devem concordar em relação a um polinômio gerador, G(x), antecipadamente. E tanto o bit de mais alta ordem quanto o de mais baixa ordem do polinômio gerador devem ser iguais a 1.
    * G(x) é usado junto a informação no transmissor gerando uma nova sequência de dados a ser enviado, M(x)
    * Se M(x) ao chegar no receptor, não for divisível pelo polinômio gerador, significa que houve erro de transmissão.
    * Algoritmo
      *	Seja G(x) o gerador polinomial de grau r. 
      *	Acrescente r bits 0 ao quadro que será transmitido
      *	Divida o novo quadro pelo gerador G(x)
      *	Subtraia do quadro original o resto da divisão
* **Controle de fluxo**
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

### Janela deslizante de 1 bit:
Esse tipo de protocolo utiliza o stop-and-wait, pois o transmissor envia um quadro e aguarda sua confirmação antes de enviar o quadro seguinte. 
O campo de confirmação no quadro contém o número do último quadro recebido sem erro. Se esse número estiver de acordo com o número de sequência do quadro que o transmissor está tentando enviar, o transmissor saberá que já cuidou do quadro armazenado em buffer e poderá buscar o pacote seguinte em sua camada de rede. Se o número de sequência for discordante, o transmissor deve continuar tentando enviar o mesmo quadro. Sempre que um quadro é recebido, um outro quadro também é enviado de volta.

### Pipeline:
Técnica baseada em permitir que o transmissor envie até w quadros antes do bloqueio, e não apenas 1. Com uma escolha apropriada de w, o transmissor será capaz de transmitir quadros continuamente durante um tempo igual ao tempo de trânsito da viagem de ida e volta, sem ocupar a janela toda. 

> “O que fazer se um quadro no meio da janela for danificado ou perdido? ”

#### Estratégias básicas para lidar com erros na presença do pipelining:
* **Go Back N**
  * O destino descarta qualquer pacote fora de ordem; portanto, não necessita de um buffer.
  * Destino confirma (i.e., ACK) um pacote recebido corretamente com o número de sequência do último pacote recebido em ordem.
  * A fonte inicializa um tempo de espera para cada pacote transmitido. Caso não receba confirmação dentro deste tempo, a fonte retransmite o pacote expirado e todos os pacotes enviados após aquele pacote
  * A fonte pode ter até W pacotes esperando por confirmação
  * Essa abordagem poderá desperdiçar uma grande quantidade de largura de banda, se a taxa de erros for alta
* **Retransmissão seletiva:**
  * Um quadro incorreto recebido é descartado, mas os quadros sem defeitos recebidos depois dele são inseridos no buffer. 
  * Quando o transmissor chega ao timeout, apenas o quadro não confirmado mais antigo é retransmitido. Se esse quadro chegar corretamente, o receptor poderá entregar à camada de rede, em sequência, todos os quadros que armazenou no buffer. 
  * Com frequência, a retransmissão seletiva é combinada com a ação de fazer o receptor enviar uma confirmação negativa (NAK – negative acknowledgement) ao detectar um erro, por exemplo, quando receber um erro de total de verificação ou um quadro fora de sequência. 
  * As NAKs estimulam a retransmissão antes de expirar o timer correspondente e, desse modo, melhoram o desempenho.
  * A estratégia de retransmissão seletiva corresponde a uma janela receptora maior que 1. 
  * Essa abordagem poderá exigir um volume de memória muito grande da camada de enlace de dados, caso a janela seja muito grande.

## Protocolos de acesso a meio compartilhado

### Protocolos MAC:
* Quando um nó quer transmitir, ele pode enviar a uma taxa R.
* Quando M nós querem transmitir, cada um envia a uma taxa média R/M

### Particionamento de canal:
* Divide o canal em pedaços menores: compartimentos de tempo, frequência, etc. Aloca um pedaço para uso exclusivo de cada nó.
* TDMA: acesso múltiplo por divisão temporal
* Acesso ao canal é feito por turnos. Cada estação controla um compartimento (“slot”) de tamanho fixo em cada turno
* FDMA: acesso múltiplo por divisão de frequência
* O espectro do canal é dividido em bandas de frequência. Cada estação recebe uma banda de frequência
* Em ambos os casos os compartimentos de frequência ou tempo não usados são um desperdício

### Passagem de permissão
* Nós transmitem nos seus turnos (mas com mais volume para enviar podem usar turnos mais longos)

### Protocolo MAC de acesso aleatório 
* Quando o nó tem um quadro a enviar, este transmite com toda a taxa do canal R e não há uma regra de coordenação a priori entre os nós
* Canal não dividido, permite colisões
* Define como detectar e se recuperar de colisões
* ALOHA e slotted ALOHA
  * A ideia básica é aplicável a qualquer sistema em que usuários descoordenados estão competindo pelo uso de um único canal compartilhado.

### ALOHA
* A ideia é permitir que os usuários transmitam sempre que tiverem dados a ser enviados.
* A rede é composta por um grande número de estações que transmitem dados em rajadas.
* O nó central retransmite todos os quadros (tenham sido recebidos corretamente ou não) através de seu canal de downlink.
* A estação não escuta o canal antes de transmitir. Logo, um quadro só não sofrerá colisão se nenhum outro for enviado dentro de um tempo de quadro a partir de seu início.
* Após o envio dos dados, o transmissor espera um período de tempo aleatório pela resposta do nó central.
* Se a resposta for negativa, uma nova transmissão é feita após um período de tempo aleatório.

### Slotted ALOHA
* O tempo é dividido em slots discretos.
* As estações só podem transmitir quadros no início dos slots de tempo
* Ao ter colisão cada nó escolhe um tempo aleatório independente para retransmitir
* A taxa de transmissão nesse caso é o dobro do ALOHA puro.

### CSMA
* Escuta antes de transmitir: 
  * Se o canal parece vazio: transmite o quadro
  * Se o canal está ocupado, adia a transmissão
* **Persistente:**
  * Caso o meio esteja ocupado, o nó persiste escutando e quando o meio ficar livre, transmite com probabilidade p.
  * Com uma probabilidade q = 1 - p, haverá um adiamento até o próximo slot. 
  * Se esse slot também estiver desocupado, haverá uma transmissão ou um novo adiamento, com probabilidades p e q. Esse processo se repete até o quadro ser transmitido ou até que outra estação tenha iniciado uma transmissão
  * No caso do 1-persistente, a estação sempre transmite quando o canal está desocupado.
* Não Persistente
  * Se ninguém mais estiver transmitindo, a estação iniciará a transmissão. 
  * No entanto, se o canal já estiver sendo utilizado, a estação calcula tempo de recuo e permanece inativo pelo tempo estipulado.
  * O tempo de recuo é decrementado enquanto o meio está livre e é congelado enquanto este estiver ocupado.
  * Consequentemente, o meio estará livre quando o contador zerar.

### CSMA/CD
* É a base da conhecida LAN Ethernet
* Colisões podem ocorrer: o atraso de propagação implica que dois nós quaisquer podem não ouvir as transmissões do outro
* Quando duas estações começam a transmitir simultaneamente, ambas detectarão a colisão quase de imediato.
* O hardware da estação deve escutar o cabo durante a transmissão. Se o que leu for diferente do que está transmitindo, a estação saberá que está ocorrendo uma colisão.  
* Após detectar uma colisão, uma estação cancela sua transmissão, espera um intervalo de tempo aleatório e, em seguida, tenta novamente, supondo que nenhuma outra estação tenha começado a transmitir nesse período. 
* A interrupção rápida dos quadros com erros economiza tempo e largura de banda.

### Ethernet
* Sem conexão: não ocorre conexão entre o adaptador transmissor e o receptor.
* Não confiável: adaptador receptor não envia ACKs ou nacks para o adaptador transmissor
  * Isto tornar a Ethernet simples e barata.
  * Mas a sequência de datagramas passada à camada de rede pode ter lacunas

> CSMA/CD do Ethernet
> 1.	Adaptador recebe um datagrama da camada de rede e cria um quadro.
> 2.	Se o adaptador detecta um canal livre, ele começa a transmitir o quadro. Se ele detecta o canal ocupado, espera até ele ficar livre e então transmite.
> 3.	Se o adaptador transmite o quadro todo sem detectar outra transmissão, a transmissão ocorre com sucesso.
> 4.	Se o adaptador detecta outra transmissão enquanto transmite, ele aborta e envia um jam signal
> 5.	Após abortar, o adaptador entra em exponential backoff: após a m-ésima colisão, o adaptador escolhe um K aleatório de {0,1,2,…,2m-1}. O adaptador espera 512.K tempos de bit e retorna ao passo 2.

> **Jam signal**: garante que todos os outros transmissores estão cientes da colisão.

### IEEE 802.11 LAN sem fio

**Padrão** | **Faixa de frequências (EUA)** | **Taxa de dados** 
:---: | :---: | :---:
802.11b | 2,4-2,485 GHz | até 11Mbits/s 
802.11a | 5,1-5,8 GHz | até 54Mbits/s 
802.11g | 2,4-2,485 GHz | até 54Mbits/s 

* Todos os três padrões têm a capacidade de reduzir sua taxa de transmissão para alcançar distâncias maiores. 
* Como LANs sem fio 802.11a podem funcionar a taxas de bits significativamente mais altas, a distância de transmissão dessas LANs é mais curta para determinado nível de potência.
* Um BSS (basic service set) contém uma ou mais estações sem fio e uma estação-base central, conhecida como um ponto de acesso.
* Estações IEEE 802.11 também podem se agrupar e formar uma rede ad hoc (rede formada apenas por hospedeiros”).

### Canais e associação
* O conjunto dos canais 1, 6 e 11 é o único de três canais não sobrepostos.
* O padrão 802.11b requer que um AP envie periodicamente quadros de sinalização, cada qual incluindo o SSID e o endereço MAC do AP.
* A estação sem fio ao tomar conhecimento dos APs disponíveis por meio dos quadros de sinalização, seleciona um desses pontos de acesso para se associar.

### O protocolo mac 802.11
* CSMA/CA: CSMA com prevenção de colisão.
* Ao contrário do protocolo Ethernet 802.3, o protocolo MAC 802.11 não implementa detecção de colisão. Isso se deve a duas razões importantes:
  * Difícil de perceber as colisões, pois o sinal que chega é muito fraco
  * Pode não perceber as colisões: colisão acontece no receptor
* SIFS: período de tempo que o receptor espera antes de enviar um ACK
* DIFS: período de tempo que a estação espera antes de enviar o quadro, após perceber que o canal está ocioso.
* No protocolo de acesso múltiplo CSMA/CD, uma estação começa a transmitir tão logo percebe que o canal está ocioso. 
* Com o CSMA/CA, entretanto, a estação só transmite após um período de tempo DIFS.
* RTS/CTS
  * Permite o transmissor “reservar” o canal em vez de acessar aleatoriamente ao enviar quadros de dados: evita colisões de quadros grandes
  * Transmissor envia primeiro um pequeno quadro chamado request to send (RTS) à estação-base usando CSMA
  * O AP envia em broadcast clear to send CTS em resposta ao RTS, que é ouvido por todos os nós
  * Transmissor envia o quadro de dados
  * Outras estações adiam suas transmissões
  * Após recepção do quadro, destinatário envia confirmação (i.e., ACK).
