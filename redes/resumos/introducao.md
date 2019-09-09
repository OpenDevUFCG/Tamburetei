# Introdução

Uma **rede de computadores** é um conjunto de computadores autônomos interconectados por uma mesma tecnologia, esta interconexão permite que os computadores realizem trocas de informações entre si. 

Além disso, é comum que redes de computadores sejam conectadas umas às outras, criando redes de redes de computadores, como a Internet. A gama de **aplicações** das RCs é vasta (sejam domésticas ou comerciais), tais como o compartilhamento de recursos, a transferência de arquivos, o uso de correio eletrônico e muitas outras.

## Sumário

- [Histórico](#histórico)
- [Classificação](#classificação)
  - [Escalabilidade](#escalabilidade)
  - [Tecnologia de Transmissão](#tecnologia-de-transmissão)
- [Arquitetura de Redes de Computadores](#arquitetura-de-redes-de-computadores)
- [Tipos de Serviços](#tipos-de-serviços)
- [Comutação](#comutação)
  - [Comutação de Circuitos](#comutação-de-circuitos)
  - [Comutação de Pacotes](#comutação-de-pacotes)
- [Topologia](#topologia)
  - [Barramento](#barramento)
  - [Anel](#anel)
  - [Estrela](#estrela)
- [Modelo OSI](#modelo-osi)


## Histórico

A necessidade de **comunicação** inerente à sociedade humana desde os seus primórdios tem sido um dos principais incentivos para a evolução das redes de computadores, especialmente no cenário atual, marcado pela descentralização e individualização dessas máquinas.

No caso específico do surgimento das redes de computadores e da Internet, o contexto histórico é a Guerra Fria. O mundo ainda está se recuperando da Segunda Guerra Mundial e a paz vigente é tão instável quando a relação entre EUA e a antiga URSS. A comunicação entre as bases militares torna-se algo crucial e assunto de primeira ordem, evidenciando a necessidade da criação de uma nova forma de intercomunicar essas bases.

Como uma série de outras tecnologias, a Internet surgiria de forma *não-exatamente-intencional*. Em 1969, a ARPA (*Advanced Research and Projects Agency*) criou a famosa e saudosa ARPANet. Seu principal objetivo era interligar as bases militares e os departamentos de pesquisas do governo americano.

O projeto nasceu com a Guerra Fria, mas não morreu junto a ela. Depois de utilizá-la amplamente, os militares decidiram “passar a guarda” da Internet para os cientistas, depois para as grandes universidades e, aos poucos, ela foi aprimorada e difundida dentre a população. 

## Classificação

Para a **classificação** das redes de computadores, é comum utilizar como métricas a escalabilidade e o tipo de tecnologia de transmissão utilizado.

#### Escalabilidade

Quanto à escalabilidade, uma rede pode ser de área pessoal (como o Bluetooth), uma rede local (como LAN usando Wi-Fi), uma rede metropolitana (como MAN conectada à central via cabo), uma rede de longa distância (como WAN composta por *hosts*, linhas de transmissão e comutadores) ou uma rede interligada (como *internets* ou redes conectadas via *gateways*).

#### Tecnologia de Transmissão

Existem variadas tecnologias de transmissão utilizadas por redes de computadores, porém, é comum agrupá-las em dois grandes grupos: as de enlace *peer-to-peer* (ponto a ponto) e as de enlace *broadcast*. 

No enlace ***peer-to-peer***, as máquinas encontram-se conectadas aos pares, de modo que os pacotes possam trafegar entre as máquinas intermediárias em seu caminho da origem até o destino. Nesse contexto, a escolha das melhores rotas torna-se uma questão vital. Já no enlace ***broadcast***, todas as máquinas compartilham o mesmo canal de comunicação, de modo que todas elas recebem todos os pacotes, mas enquanto o destinatário processa a informação, os demais computadores apenas a ignoram.

## Arquitetura de Redes de Computadores

Para reduzir a complexidade de seus projetos, as redes de computadores são organizadas em uma pilha de **camadas**, tal que cada camada oferece serviços à camada imediatamente superior e é servida pela camada imediatamente inferior, ocultando os detalhes de implementação.

A camada **N** de uma máquina utiliza um protocolo para se comunicar com a camada **N** de outra máquina. No entanto, as informações não são trocadas diretamente, mas transferidas para camadas mais baixas até alcançar o meio físico, onde se dará a comunicação em si.

No âmbito de redes de computadores, um **protocolo** pode ser definido como um conjunto de padrões e regras utilizados a fim de possibilitar a comunicação entre dispositivos, controlando o envio e a recepção de mensagens. Existem diversos tipos de protocolos, com foco em aspectos e funcionalidades também distintas, como os protocolos **IP** (*Internet Protocol*) e **SMTP** (*Simple Mail Transfer Protocol*).

- **Características de Protocolos:**
  - **Especificação:** A descrição do protocolo é completa e precisa.
  - ***Safety*:** Um protocolo sempre faz o que deve fazer.
  -	***Liveness*:** Um protocolo é livre de *deadlock*.
  -	**Eficiência:** Um protocolo utiliza os recursos disponíveis de forma eficiente.
  -	***Fairness*:** A utilização dos recursos é justa ou contratual.
  - **Simplicidade:** Um protocolo é preferencial, mas não obigatoriamente, simples.

O desempenho dos protocolos pode ser dado a partir duas características: seu **atraso médio** (tempo entre a transmissão do primeiro bit e sua recepção no destino) e sua **vazão** (razão entre o número total de bits transmitidos e o tempo total de transmissão).

Já a comunicação entre camadas adjacentes se dá através de **interfaces**, que permitem a ocultação da implementação e, consequentemente, facilitam a substituição de camadas e protocolos. Ao conjunto de camadas e protocolos dá-se o nome de **arquitetura de rede de computadores**, não incluindo os detalhes de implementação ou de interfaces.  As principais questões dessa área são a confiabilidade, a evolução e a alocação de recursos.

## Tipos de Serviços

Um **serviço** é especificado formalmente por um conjunto de **primitivas** (operações) disponíveis para que o usuário o acesse. As camadas das redes de computadores podem oferecer dois tipos de serviços: **orientados a conexão** e **não-orientados a conexão**.

Os serviços **orientados a conexão** utilizam protocolos que operam o controle de transmissão de dados durante uma comunicação estabelecida entre duas máquinas. Neste esquema, a máquina receptora envia avisos de recepção durante a comunicação, de modo que a máquina emissora é responsável pela validade dos dados que envia. Logo, os dados são enviados sob a forma de fluxo. O **TCP** é um protocolo orientado para a conexão.

Já os serviços **não orientados a conexão** utilizam um modo de comunicação no qual a máquina emissora envia dados sem prevenir a máquina receptora, de modo que a máquina receptora recebe os dados sem emitir avisos de recepção. Os dados são enviados sob a forma de blocos (datagramas). O **UDP** é um protocolo não orientado para a conexão. Nele, a transferência de dados não é confiável, não tem controle de fluxo e nem controle de congestão, sendo utilizado em aplicações como *streaming media* e DNS.

## Comutação

A **comutação** de redes de computadores é o modo como são alocados os recursos disponíveis para a transmissão de informações, visando interligar dois (ou mais) pontos para realizar a transmissão de dados entre eles. Existem dois tipos de comutação: a comutação de circuitos e a comutação de pacotes.

### Comutação de Circuitos

A **comutação de circuitos** é um serviço orientado a conexão em que todos os recursos que serão utilizados para uma transmissão são reservados (exclusivos) para ela durante toda sua duração. Esse tipo de comutação é utilizada em situações nas quais há necessidade de transmissão contínua de informação, como na comunicação por voz nas linhas telefônicas. Seu uso garante qualidade, porém, a ausência de compartilhamento de recursos causa desperdício dos mesmos.

Buscando evitar ou diminuir o desperdício é feito o processo de **multiplexação**, que tem como um dos principais objetivos evitar que haja ruído na comunicação. Esse processo pode ser de dois tipos: **multiplexação por divisão de tempo (TDM)** e **multiplexação por divisão de frequência (FDM)**.

Na **multiplexação por divisão de tempo** há uma reserva dos slots de tempo para cada usuário, pode ser de dois tipos: síncrona e assíncrona.
**Síncrona**: quando um usuário entra na rede um slot de tempo já é reservado para ele, funciona como uma fila circular, assim, há uma diminuição no despercício mas ainda não resolve o problema, pois cada vez que o usuário destinado àquele slot de tempo não for transmitir ainda ocorrerá desperdício.
**Assíncrona**: neste caso os slots de tempo são alocados de acordo com as solicitações, ou seja, os slots não são permanentemente alocados à um usuário, assim, usuários que não desejam transmitir não entrarão na fila fazendo com que haja uma maior flexibilidade e diminuição no despercídio.

Na **multiplexação por frequência** o sinal único que eu tinha antes será dividido em subfaixas, fazendo com que cada usuário transmita em faixas de frequência diferentes.

### Comutação de Pacotes

A **comutação de pacotes** é um serviço não orientado a conexão em que todos os recursos são compartilhados, não havendo necessidade de reservá-los previamente. Os dados são divididos em pacotes e transmitidos conforme estiverem disponíveis os recursos da rede. Esse tipo de comutação é utilizada em situações nas quais vários usuários utilizarão a mesma rede e/ou de maneira esporádica. Ainda que o sistema se torne flexível e livre de desperdícios, não há garantia de entrega dos dados e a utilização dos recursos da rede sob demanda pode causar congestionamentos.

## Topologia

A **topologia** de uma rede de computadores é o modo como o meio de rede está conectado aos computadores (e outros componentes), podendo ser descrita física ou logicamente. A topologia **física** descreve a maneira como os cabos se conectam fisicamente aos computadores, enquanto a topologia **lógica** descreve a maneira como os dados trafegam através dos cabos e placas de rede. 

A comparação entre diferentes topologias se dá a partir de fatores como a confiabilidade, o desempenho, o custo e o retardo de transferência.

### Barramento

Na **topologia em barramento**, todos os computadores estão ligados em um mesmo barramento físico de dados, assim, quando um computador está transmitindo um sinal, toda a rede fica ocupada. Esse tipo de topologia apresenta baixo custo, minimiza a quantidade de cabos utilizados e a falha de um dos computadores não afetará os demais. Apesar de sua instalação ser simples, uma falha no cabo principal derrubará toda a rede.

### Anel

Na **topologia em anel**, os computadores são conectados em série para formar um circuito fechado (anel). Esse tipo de topologia apresenta baixo custo, tem um único sentido de transmissão e a permissão para envio/recepção de informações é feita através de um *token*. Sua principal desvantagem é a baixa tolerância a falhas, visto que a falha de um computador pode tornar outros computadores inalcançáveis na rede.

### Estrela

Na **topologia em estrela**, um elemento central está diretamente conectado a cada um dos computadores da rede, sendo o responsável por gerenciar e garantir o fluxo de dados entre as máquinas. Utiliza um número relativamente alto de cabos, aumentando seu custo. Além disso, o limite de conexões do nó central, também limita a capacidade de expansão desse tipo de topologia. Tem uma alta tolerância a falhas, dado que um computador falho não afetará as demais conexões.

## Modelo OSI

O **modelo OSI** de arquitetura de redes é constituído por 7 camadas. Cada uma dessas camadas é responsável por um determinado conjunto de funções e serviços, tal que as camadas mais altas estão mais próximas do usuário final, enquanto as camadas mais baixas tem tarefas com menor nível de abstração.

É importante salientar que o modelo **TCP/IP** é hoje indispensável dada sua majoritária utilização, mesmo sendo considerado "pesado". Ele conta com apenas 4 camadas (aplicação, transporte, internet e enlace) que podem ser mapeadas para as camadas do modelo OSI, adotado na disciplina por questões didáticas e cujas funções estão descritas abaixo (da mais baixa à mais alta).

- **Camada Física:** Responsável pela transmissão de bits por um canal de comunicação, essa camada lida com interfaces mecânicas, elétricas e de sincronização, mas também com o meio físico.

- **Camada de Enlace:** Responsável por transformar um canal de transmissão comum em uma linha que se aproxime de estar livre de erros de transmissão. Essa camada oculta erros para a camada de rede, mas também controla a velocidade de transmissão (conforme a velocidade suportada pelo receptor).

- **Camada de Rede:** Responsável pelo controle da sub-rede, determinando como os pacotes devem ser roteados da origem até o destino. Esse roteamento pode ser feito de modo estático ou dinâmico. Além disso, também é responsabilidade desta camada gerenciar os gargalos e lidar com problemas de congestionamento.

- **Camada de Transporte:** Responsável por dividir os dados provenientes da camada de sessão em unidades menores para a camada de rede, mas também por garantir que todos os fragmentos cheguem corretamente à outra extremidade da transmissão.

- **Camada de Sessão:** Responsável por garantir que usuários de máquinas distintas estabeleçam diálogo através de sessões de comunicação, essa camada fornece serviços como o controle de diálogo, o gerenciamento de *tokens* e a sincronização.

- **Camada de Apresentação:** Responsável por tornar possível a comunicação entre computadores com diferentes representações internas dos dados, essa camada está intimamente relacionada à sintaxe e à semântica das informações que são transmitidas.

- **Camada de Aplicação:** Responsável pela interação direta com o usuário final. É nessa camada que constam os protocolos comumente necessários para os usuários, tais como o HTTP, o HTTPS e o DNS.
