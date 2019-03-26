# Camada De Rede

## Sumário
- [Camada De Rede](#camada-de-rede)
  - [Sumário](#sumário)
  - [Introdução](#introdução)


## Introdução

**Internet**: Conjunto de redes de escala mundial, ligadas pelo protocolo IP. 

**TCP/IP**: Família de protocolos de comunicação, com serviços e acesso independente de tecnologia. Permite a interconexão de redes físicas diferentes. Interconexão realizada por roteadores.

**Protocolo IP**: Não orientado a conexão, roteamento melhor esforço. Não confiável, sem controle de fluxo e de erros e é simples. Roteamento baseado no endereço da rede de destino.

A camada de rede é responsável por prover conectividade ao computador e selecionar caminhos para que os pacotes de dados possam trafegar. Isso é feito através do roteamento. Um motivo para que a conectividade possa ocorrer tem relação com o IP (Internet Protocol). O endereçamento IP permite que o dispositivo possa se conectar em uma mesma rede ou em redes diferentes.

* **Camada de Rede: Objetivos**
  * Transferência de pacotes da origem para o destino;
  * Vários saltos (hops) intermediários no caminho;
  * Elementos de rede: Roteadores ou Comutadores;
  * incipal função: Roteamento (encaminhamento);
  * Outras funções: Controle de Congestionamento, Negociação de QoS e Interconexão de redes.
* **Camada de Rede: Funcionamento**
  * Transporta segmentos do host transmissor para o receptor;
  * No lado transmissor, encapsula os segmentos em datagramas;
  * No lado receptor, entrega os segmentos à camada de transporte;
  * Protocolos da camada de rede em cada host roteador;
  * Roteador examina campos de cabeçalho em todos os datagramas IP que passam por ele;
* **Roteamento**: Estabelecimento dos melhores caminhos (rotas).
* **Encaminhamento**: Processo de despachar cada pacote ao seu destino ou sistema intermediário.
* **Serviços oferecidos à camada de Transporte:** 
  * Devem ser independentes da tecnologia da sub-rede. 
  * Proteção contra tipo, quantidade e topologia das sub-redes.
  * Endereços devem ter plano de numeração único.
  * **Tipos de Serviço**: Orientado a conexão e Sem conexão.

##Circuitos Virtuais x Datagramas

* **Circuitos Virtuais (CVs)** 
  * Analogia aos circuitos físicos da rede telefônica;
  * Rede complexa e segura;
  * Geralmente orientada a conexões (conexões na camada de rede são geralmente chamadas de circuitos virtuais);
  * Usado para estabelecer, manter e encerrar conexões;
  * Usados em ATM, frame-relay e X-25;
  * Não é usado na Internet atualmente.
* **Datagramas**
  * Analogia com o serviço de “telegramas”; 
  * Rede simples e não confiável;
  * Geralmente é não orientada a conexões (mas pode ser);
  * Não é estabelecida conexão na camada de rede;
  * Roteadores: sem estado sobre conexões fim-a-fim;
  * O conceito “conexão” não existe na camada de rede;
  * Pacotes são encaminhados para o endereço do host de destino;
  * Pacotes para o mesmo destino podem seguir diferentes rotas.

**Questão** | **Datagrama** | **Circuito Virtual (VC)** 
:---: | :---: | :---:
Configuração de Circuito | Não necessária | Requerida
Endereçamento | Cada pacote contém endereços da fonte e do destino | Cada pacote contém um número de CV
Informação de Estado | Subrede não mantém informação de estado | Cada CV requer espaço na tabela da subrede
Roteamento | Cada pacote é roteado independentemente | Rota escolhida quando CV é configurado; todos os pacotes seguem esta rota
Efeito de falhas do roteador | Nenhuma, exceto a perda de pacotes durante a falha | Todos os CVs que passam pelo roteador com falha são Terminados
Controle de congestionamento | Difícil | Fácil, se memória suficiente tiver sido alocada a priori para cada CV

## Roteamento

* **Algoritmo de roteamento**: 
  * Parte da camada de rede responsável pela decisão sobre a linha de saída para a transmissão de um pacote;
  * Pode ser implementado por um protocolo de roteamento, ou executado de maneira estática. 
* **Protocolo de roteamento**:
  * Software utilizado pelos roteadores para que eles estabeleçam tabelas de roteamento consistentes.
  * Qualquer protocolo de roteamento deve comunicar informação da topologia da rede para todos os outros roteadores, para tomar decisões de roteamento.
* **Datagramas**: Decisão de roteamento deve ser tomada a cada pacote. 
* **Circuitos Virtuais**: Decisão de roteamento é tomada somente no estabelecimento da conexão e também chamado de roteamento por sessão.

Existem duas classes de tipos de roteamento: **estático** e **dinâmico**. Não adaptativo (**estático**): Decisão do roteamento não é baseada em estimativas de tráfego atual e da topologia. Adaptativo (**dinâmico**): Muda decisões de roteamento para refletir mudanças na topologia, bem como, no tráfego. Leva em consideração:  custo, caminho, carga e tamanho da fila.
 
## Cabeçalho IP

* **Fragmentação e remontagem**
  * MTU - Maximum Transmit Unit é o tamanho máximo que um pacote pode ter; 
  * MTU é padronizado de acordo com a interface física;
  * Cada roteador deve fragmentar o pacote antes de encaminhá-lo para uma interface, no caso do tamanho original ser maior que o MTU;
  * Cada fragmento pertence a um mesmo pacote original (mesmo valor no campo Fragmentation Identifier)
* **Processo**:
1. O primeiro bit do campo "Flags" deve ser 0 (reservado);
2. Fragmentos não podem novamente ser fragmentados, logo "May Fragment" deve ser 0;
3. O flag "More Fragments" indica se existe mais fragmentos adiante;
4. 1o. fragmento: "Fragment Offset" = 0, tam=1500 (20+1480) bytes;
5. 2o. fragmento: "Fragment Offset" = 185 (1480/8), tam=1500;
6. 3o. fragmento: "Fragment Offset" = 370 ((1480×2)/8), tam=1500;
7. 4o. fragmento: "Fragment Offset" = 555 ((1480×3)/8), tam=24 (20+4).

## Endereçamento IP

**Classe** | **Primeiro octeto** | **Parte da rede (N) <br/> Parte para hosts (H)** | **Máscaras** | **Nº Redes / hosts por rede**
:---: | :---: | :---: | :---: | :---:
A | 1-127| **N.H.H.H** | 255.0.0.0 | **126** redes <br/> **16,777,214** hosts por rede (2^24-2)
B | 128-191 | **N.N.H.H** | 255.255.0.0 | **16,384* redes (2^14) <br/> **65,534** hosts por rede (2^16-2)
C | 192-223 | **N.N.N.H** | 255.255.255.0 | **2,097,150** redes (2^21) <br/> **254** hosts por rede (2^8-2)
D | 224-239 | Multicast | NA | NA
E | 240-255 | Experimental | NA | NA

* **Sub-redes privadas – Não podem ser publicados na Internet**:
  * 10.x.x.x (classe A)
  * 172.16.x.x - 172.31.x.x (classe B)
  * 192.168.x.x (classe C) 
* **Endereços especiais**
  * 0.0.0.0 			este host
  * 0.0.0.124 host 124 	nesta rede 
  * 255.255.255.255 	todos os hosts desta rede 
  * N.N.N.255 		    todos os hosts da rede N.N.N 
  * 127.X.X.X 		    Loopback 
* **Alguns endereços inválidos para hosts** 
  * 10.1.0.0 		IP do host não pode ser 0
  * 10.1.0.255 	    IP do host não pode ser 255 
  * 10.123.255.4 	Subrede não pode ter valor 255 
  * 0.12.16.89 	    Parte do endereço não pode ter valor 0
  * 255.9.56.45 	Parte do endereço não pode ter valor 255
  * 10.34.255.1 	Parte do endereço não pode ter valor 255

## Máscara de sub-rede

* A máscara serve para indicar qual parte do endereço IP identifica o endereço de rede e qual parte identifica o endereço do host 
* Os bits 1 indicam a parte do endereço da rede
* Os bits 0 indicam a parte do endereço do host

### Máscaras default:

Classe A - 255.0.0.0 		11111111.00000000.00000000.00000000 
Classe B - 255.255.0.0 	11111111.11111111.00000000.00000000 
Classe C - 255.255.255.0 	11111111.11111111.11111111.00000000 

### Processo:

    1. Executa-se um AND lógico entre os bits da máscara e endereço IP e obtém o Network Address 
    2. No endereço da rede todos os bits do host são 0
    3. No endereço de broadcast, todos os bits do host são 1

### Exemplo:

10001100.10110011.11110000.11001000 		140.179.240.200 Endereço IP 
11111111.11111111.00000000.00000000 		255.255.000.000 Máscara classe B
------------------------------------------------------------------------------
10001100.10110011.00000000.00000000 	    140.179.000.000 Network Address 
10001100.10110011.11111111.11111111 		140.179.255.255 Network Broadcast

## CIDR: Classless InterDomain Routing

* A porção de endereço de rede tem tamanho arbitrário
* Formato do endereço: a.B.C.D/x, em que x é o número de bits na parte de rede do endereço 
* Inicialmente somente grupos de endereços Classe C foram utilizados
* Como o mesmo procedimento já foi também aplicado às antigas classes A e B, pode-se dizer que de fato o endereçamento em classes está descaracterizado e completamente substituído pelo CIDR (obs.: vários endereços de antigas classes A e B foram progressivamente realocados)

## Como um sistema final pode obter um endereço IP?

* Configuração estática
* DHCP: Dynamic Host Configuration Protocol: obtém dinamicamente endereços IP de um servidor 
  * “plug-and-play”

### Como uma rede obtém a parte de sub-rede do endereço IP ?

* Obtém a porção alocada no espaço de endereço do seu provedor ISP (ICANN: internet corporation for assigned names and numbers)
  * Aloca endereços, gerência DNS, atribui nomes de domínios...

## DHCP

É um protocolo utilizado em redes de computadores que permite às máquinas obterem um endereço IP automaticamente. 

Por meio dele um servidor é capaz de distribuir automaticamente endereços de IP diferentes a todos os computadores à medida que eles fazem a solicitação de conexão com a rede. Essa distribuição dos IPs é feita em um intervalo pré-definido configurado no servidor. Sempre que uma das máquinas for desconectada o IP ficará livre para o uso em outra.

* **Funcionamento**:
  * Quando um cliente conecta-se a uma rede ele envia um pacote com um pedido de configurações DHCP. 
  * O servidor DHCP gerencia uma faixa fixa de IPs disponíveis juntamente com as informações e parâmetros necessários (gateway padrão, nome de domínio, DNS, etc). 
  * Quando este servidor recebe um pedido, ele entrega um destes endereços e configurações para o cliente.
* **Segurança**:
  * Mensagens não são autenticadas 
    * Alguém pode forjar um DHCP server ou um cliente 
  * Cliente não pode confiar no servidor e vice-versa
* **Configuração**:
  * Para redes com mais de um servidor 
    * Servidores na rede não podem trocar informações
    * Não existe um protocolo server-server
    * Devem ter espaços de endereçamento disjuntos para evitar distribuição de IP duplicados 
  * Servidores são configurados manualmente
* **Modos de Operação**:
  * **Automática**, no qual uma quantidade de endereços de IP (dentro de uma faixa) é definida para ser utilizada na rede. Neste caso, sempre que um dos computadores de uma rede solicitar a conexão com ela, um destes IPs será designado para a máquina em questão.
  * Na **dinâmica** o procedimento é bem parecido com o efetuado pela automática, porém a conexão do computador com determinado IP é limitada por um período de tempo pré-configurado que pode variar conforme desejado pelo administrador da rede.
  * No modo **manual** o DHCP aloca um endereço de IP conforme o valor de MAC (Medium Access Control) de cada placa de rede de forma que cada computador utilizará apenas este endereço de IP. Utiliza-se este recurso quando é necessário que uma máquina possua um endereço de IP fixo.

## NAT

**NAT (Network Address Translation)** é uma técnica que consiste em reescrever os endereços IP de origem de um pacote que passam por um routes ou firewall de maneira que um computador de uma redes interna tenha acesso ao exterior (internet).

A motivação para a criação do NAT foi a necessidade das redes internas/privadas se comunicarem com a internet/redes públicas. Como os IPs internos, como 10.0.0.0/8, não podem ser passados para a Internet, pois não são roteador nela, a solução foi fazer um mapeamento baseado no IP interno e na porta local do computador. Com esses dois dados, o NAT gera um número de 16 bits usando a tabela hash, este número é então escrito no campo da porta de origem.
