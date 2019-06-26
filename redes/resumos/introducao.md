# Introdução

Uma **rede de computadores** é um conjunto de computadores autônomos interconectados por uma mesma tecnologia, esta interconexão permite que os computadores realizem trocas de informações entre si. 

Além disso, é comum que redes de computadores sejam conectadas umas às outras, criando redes de redes de computadores, como a Internet. A gama de **aplicações** das RCs é vasta (sejam domésticas ou comerciais), tais como o compartilhamento de recursos, a transferência de arquivos, o uso de correio eletrônico e muitas outras.

## Histórico

A necessidade de **comunicação** inerente à sociedade humana desde os seus primórdios tem sido um dos principais incentivos para a evolução das redes de computadores, especialmente no cenário atual, marcado pela descentralização e individualização dessas máquinas.

## Classificação

Para a **classificação** das redes de computadores, é comum utilizar como métricas a escalabilidade e o tipo de tecnologia de transmissão utilizado.

#### Escalabilidade

Quanto à escalabilidade, uma rede pode ser de área pessoal (como o Bluetooth), uma rede local (como LAN usando Wi-Fi), uma rede metropolitana (como MAN conectada à central via cabo), uma rede de longa distância (como WAN composta por *hosts*, linhas de transmissão e comutadores) ou uma rede interligada (como *internets* ou redes conectadas via *gateways*).

#### Tecnologia de Transmissão

Existem variadas tecnologias de transmissão utilizadas por redes de computadores, porém, é comum agrupá-las em dois grandes grupos: as de enlace *peer-to-peer* (ponto a ponto) e as de enlace *broadcast*. 

No enlace ***peer-to-peer***, as máquinas encontram-se conectadas aos pares, de modo que os pacotes possam trafegar entre as máquinas intermediárias em seu caminho da origem até o destino. Nesse contexto, a escolha das melhores rotas torna-se uma questão vital. Já no enlace ***broadcast***, todas as máquinas compartilham o mesmo canal de comunicação, de modo que todas elas recebem todos os pacotes, mas enquanto o destinatário processa a informação, os demais computadores apenas a ignoram.

## Arquitetura de Redes de Computadores

Para reduzir a complexidade de seus projetos, as redes de computadores são organizadas como uma pilha de **camadas**. Cada camada oferece determinados serviços à camada imediatamente superior e é servida pela camada imediatamente inferior, mantendo ocultos todos os detalhes de sua própria implementação.