# Camada Física

## Sumário
- [Camada Física](#camada-física)
  - [Sumário](#sumário)
  - [Histórico](#histórico)
    - [Evolução na Comunicação e Processamento](#evolução-na-comunicação-e-processamento)
  - [Definições e Conceitos](#definições-e-conceitos)
    - [O que é Internet?](#o-que-é-internet-?)
    - [O que são RFCs e a IETF?](#o-que-são-rfcs-e-a-ietf-?)
    - [Conceito de Redes de Computadores](#conceito-de-edes-de-computadores)
    - [O que é Protocolo?](#o-que-é-protocolo-?)
    - [Serviço Orientado a Conexão](#serviço-orientado-a-conexão)
  - [TCP/IP](#tcp/ip)
    - [Modelo TCP/IP](#modelo-tcp/ip)    


## Histórico

### Evolução na Comunicação e Processamento

A necessidade de comunicação, assim como o instinto de sobrevivência, é inerente aos seres humanos desde seu surgimento. Das pinturas rupestres, pombo-correio, até a popularização da Internet, são mais de 30.000 anos de história evolutiva dos meios de comunicação.

> *“Cada um dos três séculos anteriores foi dominado por um a única tecnologia. O Século XVIII foi a época dos grandes sistemas mecânicos que acompanharam a Revolução Industrial. O Século XIX foi a era das máquinas a vapor. As principais conquistas tecnológicas do Século XX se deram no campo da aquisição, do processamento e da distribuição de informações. Entre outros desenvolvimentos, vimos a instalação das redes de telefonia em escala mundial, a invenção do rádio e da televisão, o nascimento e o crescimento sem precedentes da indústria de informática e o lançamento dos satélites de comunicação.”* (TANENBAUM)

No caso específico do surgimento da Internet, o contexto histórico é o seguinte - Guerra Fria. O mundo ainda está se recuperando dos destroços remanescentes da segunda guerra mundial e o clima de paz é mais falso que a amizade entre USA e a antiga URSS. 

A comunicação entre as bases militares tornou-se algo crucial e assunto de primeira ordem - quem tem mais informação consequentemente ganha a guerra. Assim, fica evidente a necessidade da criação de algo novo, uma nova forma de inter-comunicar essas bases… a internet! Ou pelo menos os primeiros passos dela. A internet surge então, bem como outras incontáveis tecnologias, de forma não-exatamente-intencional. 

Em 1969, a empresa de ARPA (Advanced Research and Projects Agency), resolveu criar a famosa e saudosa (não pelos soviéticos, claro) ARPANet. Ela tinha como principal objetivo interligar as bases militares e os departamentos de pesquisas do governo americano. O projeto nasce com a guerra, mas chegado o seu fim e o sucesso dos americanos, qual o futuro da ARPANet? Depois de ser amplamente utilizada durante os embates, os militares decidiram “passar a guarda” para os cientistas, depois para as grandes universidades e assim foi sendo aprimorada e difundida (dando um grande pulo histórico). 

A tabela abaixo explica um pouco da evolução dos computadores e processamento.

**Geração** | **Computadores** | **Processamento** 
:---: | :---: | :---:
**Primeira Geração (1940-1959)** | Exemplo: ENIAC. Válvulas e circuitos. Ocupava o espaço de um prédio. | Processamento batch: ocorre através de um lote de tarefas enfileiradas. Feito manualmente por uma equipe.
**Segunda Geração (1959-1965)** | Exemplo: IBM 7094. Válvulas foram substituídas por transistores, o que diminuiu o tamanho dos computadores, permitindo o início de seu uso comercial. | Os primeiros terminais interativos surgiram, onde os usuários poderiam acessar o computador central pelas linhas de comunicação.
**Terceira Geração (1965-1975)** | A popularização dos circuitos integrados contribuiu para, além de baratear o custo dos computadores, diminuir ainda mais seu tamanho, sendo agora possível a ideia de computadores pessoais. | Começo da descentralização e individualização no processamento e serviços, a partir da década de 70.
**Quarta Geração (1975-hoje)** | Popularização e crescente dos computadores pessoais. | Sistemas distribuídos e redes locais.

## Definições e Conceitos

### O que é Internet?

Kurose-Ross, no livro Redes de Computadores e a Internet, fala que podemos definir a Internet como “uma infraestrutura de rede que provê serviços para aplicações distribuídas. ” Claro que essa definição é bastante rasa, mas por meio dela é possível entender a ponta do iceberg.

Na Internet, existem dois conceitos essenciais para sua forma de comunicação: hospedeiros e sistemas finais. Um sistema final são todos os computadores interligados na periferia da Internet. Hospedeiros (ou hosts) é um sistema final que, como o nome já adianta, hospeda uma aplicação/serviço.

Segundo Kurose-Ross (vai ter muito ele aqui mesmo), “Sistemas finais não são interligados diretamente por um único enlace de comunicação. Em vez disso, são interconectados indiretamente por equipamentos intermediários de comutação conhecidos como comutadores de pacotes.” Um exemplo de comutador de pacotes são roteadores, que encaminham pacotes (bloco de dados) para seus destinos finais.

Os sistemas finais são conectados entre si por enlaces de comunicação, como por exemplo: fibra óptica (cabeada) e ondas de rádio (sem fio), e acessam a Internet através de ISPs (Internet Service Providers). Cada ISP é uma rede de comutadores de pacotes e enlaces de comunicação.

### O que são RFCs e a IETF?

IETF - Internet Engineering Task Force. Trata-se de um grupo responsável por desenvolver documentos padrões para tecnologias que cercam a Internet, os RFCs.

RFC - Request  for Comments. Elas começaram como solicitações gerais em comentários para resolver problemas que a Internet enfrentava no início. Tendem a ser detalhados e técnicos e existem mais de 7.000.

### Conceito de Redes de Computadores

Segundo Tanenbaum, Redes de Computadores podem ser definidas como **“um conjunto de computadores autônomos interconectados por uma única tecnologia.”**

> *Dois computadores estão interconectados quando podem trocar informações. A conexão não precisa ser feita por um fio de cobre; também podem ser usadas fibras ópticas, micro-ondas, ondas de infravermelho e satélite de comunicações. Existem redes em muitos tamanhos, modelos e formas(...). Embora possa parecer estranho para algumas pessoas, nem a Internet nem a World Wide Web é uma rede de computadores. (...) A resposta simples é que a Internet não é uma única rede, mas uma rede de redes, e a Web é um sistema distribuído que funciona na Internet.”*

### O que é Protocolo?

Protocolo, no âmbito de redes de computadores, pode ser definido como um conjunto de padrões e regras utilizados a fim de possibilitar a comunicação entre dispositivos. Eles controlam o envio e a recepção de mensagens.

Existem diversos tipos de protocolos, cada um focado em um aspecto e funcionalidade diferente. Por exemplo, o protocolo IP (Internet Protocol), que especifica o formato dos pacotes que são enviados e recebidos entre roteadores e sistemas finais; o SMTP (Simple Mail Transfer Protocol) para envio de e-mails e tantos outros.

* Características de Protocolos:
  * Especificação de protocolo: a descrição do protocolo é completa e acurada.
  * Safety: um protocolo faz o que deve fazer sempre.
  *	Liveness: um protocolo é livre de deadlock.
  *	Eficiência: um protocolo utiliza os recursos disponíveis de forma eficiente.
  *	Justiça (fairness): utilização justa ou contratual dos recursos.
  * Simplicidade: é desejável, mas não necessária.
* Desempenho de Protocolos:
  *	Atraso médio: tempo entre a transmissão do primeiro bit e a recepção do mesmo pelo destino.
  *	Vazão ou Capacidade: número total de bits transmitidos dividido pelo tempo total de transmissão.


### Serviço Orientado a Conexão

Trata-se de um modo de comunicação no qual a máquina emissora envia dados sem prevenir a máquina receptora, e a máquina receptora recebe os dados sem avisos de recepção à primeira. Os dados são assim enviados sob a forma de blocos (datagramas). O UDP é um exemplo de protocolo não orientado para a conexão. No caso do UDP, a transferência de dados não é confiável, não tem controle de fluxo e nem controle de congestão. Aplicações que utilizam UDP: Streaming media, teleconferência, DNS, telefonia IP.

## TCP/IP

### Modelo TCP/IP

TCP/IP (Transmission Control Protocol - Protocolo de Controle de Transmissão/ Internet Protocol - Protocolo da Internet), criado em 1969 pela U.S. Department of Defense Advanced Research Projects Agency é um conjunto de protocolos de comunicação em camadas entre computadores em redes. Cada uma dessas camadas é responsável por um determinado grupo de funções e serviços, sendo as camadas mais altas (aplicação) logicamente mais perto dos usuários, e as mais baixas (física) tendo tarefas de menor nível de abstração.

![Modelo OSI / Modelo TCP/IP](https://drive.google.com/open?id=1CDUDR7V5potF-v6NuYLXIgqg6tcUp5Vu)

Apesar de ser considerado um protocolo pesado, o TCP/IP hoje é indispensável. Dentre os seus muitos benefícios estão:
*	Padronização: um padrão, um protocolo roteável que é o mais completo e aceito protocolo disponível atualmente. Todos os sistemas operacionais modernos oferecem suporte para o TCP/IP e a maioria das grandes redes se baseia em TCP/IP para a maior parte de seu tráfego.
*	Interconectividade: uma tecnologia para conectar sistemas não similares. Muitos utilitários padrões de conectividade estão disponíveis para acessar e transferir dados entre esses sistemas não similares, incluindo FTP (File Transfer Protocol) e Telnet (Terminal Emulation Protocol).
*	Roteamento: permite e habilita as tecnologias mais antigas e as novas a se conectarem à Internet. Trabalha com protocolos de linha como PPP (Point to Point Protocol) permitindo conexão remota a partir de linha discada ou dedicada. Trabalha como os mecanismos IPCs e interfaces mais utilizados pelos sistemas operacionais, como sockets do Windows e NetBIOS.
*	Protocolo Robusto: escalável, multiplataforma, com estrutura para ser utilizada em sistemas operacionais cliente/servidor, permitindo a utilização de aplicações desse porte entre dois pontos distantes.
*	Internet: é através da suíte de protocolos TCP/IP que obtemos acesso a Internet. As redes locais distribuem servidores de acesso a Internet (proxy servers) e os hostslocais se conectam a esses servidores para obter o acesso a Internet. Este acesso só pode ser conseguido se os computadores estiverem configurados para utilizar TCP/IP.

O protocolo TCP/IP se divide em quatro grandes camadas com as seguintes funções principais:

**Camada** | **Exemplos** | **Função** 
:---: | :---: | :---:
**Aplicação** | **HTTP, HTTPS, FTP, DNS.** <br/> “Como um web browser deve se comunicar com um servidor da web.” | Faz a comunicação entre os programas e os protocolos de transporte. Contém todos os protocolos para um serviço específico de comunicação de dados em um nível de processo-a-processo.
**Transporte** | **TCP, UDP, SCTP.** | Essa camada tem como função controlar a comunicação host-a-host. Ela recebe os dados enviados pela camada de aplicação, transforma-os em pacotes menores e garante que chegarão sem erros e na ordem certa.
**Internet** | **IP:** endereçamento IP, fragmentação e montagem dos pacotes. <br/> **ARP:** resolução do endereço da camada de internet para o endereço da camada de interface de rede, tais como um endereço de hardware. | Ela é responsável pelo endereçamento e roteamento do pacote, fazendo a conexão entre as redes locais. Adiciona ao pacote o endereço IP de origem e o de destino, para que ele saiba qual o caminho deve percorrer.
**Enlace (Com interface de rede)** | **LLC, MAC.** | Essa camada é responsável pelo envio do datagrama recebido da camada de internet em forma de quadros através da rede física.

![Modelo TCP/IP](https://drive.google.com/open?id=1jU9a0x1KNwelRvM9ZIjWHIq1piIl9Q4M)