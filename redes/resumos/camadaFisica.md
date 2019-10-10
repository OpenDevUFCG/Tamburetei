---
title: Camada Física
---

A **camada física** é o alicerce sobre o qual são construídas as redes de computadores, sendo responsável pela transmissão de bits por um canal de comunicação. Suas características determinam o desempenho da rede e é dela que se origina a definição de interfaces para o meio físico (como a elétrica e a de sincronização).

## Sumário

- [Transmissão](#transmissão)
  - [Conceitos](#conceitos)
  - [Modos de Transmissão](#modos-de-transmissão)
  - [Ritmos de Transmissão](#ritmos-de-transmissão)
  - [Modos de Operação](#modos-de-operação)
  - [Taxa Máxima de Transmissão](#taxa-máxima-de-transmissão)
- [Meios de Transmissão](#meios-de-transmissão)
  - [Pares Trançados](#pares-trançados)
  - [Cabos Coaxiais](#cabos-coaxiais)
  - [Fibra Ótica](#fibra-ótica)
  - [Sem Fio](#sem-fio)
- [Codificação](#codificação)
- [Multiplexação](#multiplexação)
  - [Divisão por Frequência](#divisão-por-frequência)
  - [Divisão por Tempo](#divisão-por-tempo)
- [Modulação](#modulação)

## Transmissão

A **transmissão de informações** pode ser feita partir da variação de propriedades físicas, tais como a corrente e a tensão. Sendo a análise de *Fourier* vital para a compreensão dos sinais trasmitidos, dado que frequências distintas são afetadas de modo diferente por um mesmo sinal.

### Conceitos

- **Banda Base:** Intervalo entre zero e uma frequência máxima em que os sinais estão localizados.
- **Banda Passante:** Intervalo de frequência para o qual o sinal é deslocado para ser, de fato, transmitido.
- **Largura de Banda:** Faixa de frequência que é transmitida sem forte atenuação (redução de amplitude) em um meio. Essa propriedade do meio de transmissão é definida a partir de suas características físicas, tais como tamanho e espessura do fio.
- **Filtros:** Utilizados para reduzir a largura de banda, aumentando a eficiência e garantindo padrões para a transmissão.

### Modos de Transmissão

- **Paralela:** Transmissão simultânea de vários bits através de várias linhas de comunicação.
- **Serial:** Transmissão bit a bit através de uma única linha de comunicação. Utilizada em redes de computadores.

### Ritmos de Transmissão

- **Síncrona:** Possui cadência fixa para transmissão sequenciada dos bits, necessitando de sincronização entre o transmissor e o receptor.
- **Assíncrona:** O tempo de transmissão entre dois grupos de bits pode variar e não há necessidade de fixação prévia de padrão de tempo. São utilizados *start bits* e *stop bits* para delimitar as transmissões.

### Modos de Operação

- **Simplex:** A comunicação se dá em uma única direção.
- **Half-Duplex:** A comunicação se dá em ambas as direções, mas não simultaneamente.
- **Full-Duplex:** A comunicação se dá em ambas as direções simultaneamente.

### Taxa Máxima de Transmissão

A **taxa máxima** de transmissão em canais sem ruído e com largura de banda finita pode ser calculada através da equação de *Nyquist*. Essa equação define a taxa máxima como **2 H log2(*L*)**, onde **H** é a largura da banda e **L** é o número de níveis discretos do sinal.

De maneira análoga, a equação de *Shannon* descreve a taxa máxima de transmissão em canais com largura de banda finita e ruído aleatório. Essa equação define a taxa máxima como **H log2(*1 + (S/N)*)**, onde **H** é a largura da banda e **S/N** é a proporção sinal/ruído. Para o cálculo dessa proporção, iguala-se o valor de decibéis a **10 *log10(*S/N*)*** e, através de manipulações matemáticas, encontra-se a razão desejada.

Em ambos os casos, o valor resultante das equações encontra-se em *bps* (bits por segundo).

## Meios de Transmissão

### Pares Trançados

Os **pares trançados** são um tipo de meio guiado formado por fios de cobre de pequena espessura, encapados e enrolados de maneira helicoidal para minimizar a interferência entre si. São leves, de fácil manuseio, de fácil instalação e tem baixo custo. Além disso, não precisam ser aterrados, porém, tem limitações referentes à distância e à interferência eletromagnética. Os pares trançados são geralmente utilizados no sistema telefônico.

### Cabos Coaxiais

Os **cabos coaxiais** são um tipo de meio guiado formado quatro camadas: núcleo de cobre, material isolante, condutor externo em malha e capa plástica protetora. Apesar do custo mais elevado que os pares trançados, da necessidade de aterramento e da difícil instalação, esse tipo de meio apresenta uma resistência considerável à interferência eletromagnética e alcança maiores distâncias. Os cabos coaxiais são geralmente utilizados para televisão a cabo.

### Fibra Ótica

A **fibra ótica** é a tecnologia mais recente dos meios guiados, podendo ser de modo único ou multimodo. Com elevado custo e dificuldades de manuseio e instalação, esse tipo de meio guiado apresenta longo alcance, baixa perda, banda passante quase infinita e imunidade a ruídos e interferência eletromagnética.

### Sem Fio

As transmissões **sem fio** são feitas através de meios não-guiados e se popularizaram bastante na última década. A fácil instalação dos meios não-guiados é a principal vantagem desse tipo de transmissão. Entretanto, a constante presença de interferência tornou necessária a criação de uma política para divisão do espectro eletromagnético. Existem várias formas de transmissão sem fio (como rádio e infravermelho), cada uma com tecnologias e alcances distintos.

## Codificação

No contexto das redes de computadores, a **codificação** é o processo de conversão de corrente elétrica para informação digital e vice-versa. Existem diversas estratégias utilizadas para essa tarefa, porém, é comum que os esquemas de conversão bit-sinal mais complexos garantam mais vantagens.

- **Codificação Polar:** Tensão negativa representa o bit 0 e tensão positiva representa o bit 1.
- **Codificação Unipolar:** Tensão neutra representa o bit 0 e tensão positiva representa o bit 1.
- **Codificação Bipolar:** Tensão neutra representa o bit 0 e tensões positivas ou negativas representam o bit 1.
- **Codificação Manchester:** Mudança de tensão "positiva para negativa" representa o bit 0 e mudança de tensão "negativa para positiva" representa o bit 1.

## Multiplexação

O processo de compartilhamento de um mesmo canal por vários sinais é chamado de **multiplexação**. Em geral, a banda passante necessária para transmitir um sinal é menor do que a banda passante dos meios físicos. Mesmo quando isso não ocorre, o compartilhamento do canal permite aproveitar a banda passante não utilizada para trasmissão de outros sinais.

### Divisão por Frequência

A **multiplexação por divisão de frequência** (*Frequency Division Multiplexing* ou FDM) divide o espectro de frequência em várias faixas que serão ocupadas por sinais distintos. Entre essas faixas, adiciona-se faixas "vazias" (chamadas de bandas de proteção) que visam impedir a sobreposição de sinais mesmo em um meio com ruído.

No transmissor, os sinais são filtrados para preservar a faixa relativa à banda passante de cada um e, em seguida, deslocados para que ocupem faixas disjuntas. Consequentemente, o receptor precisará conhecer a faixa de frequência do sinal e o deslocamento dele em relação à faixa original, assim será possível realizar a filtragem para reconstituir o sinal original.

### Divisão por Tempo

A **multiplexação por divisão de tempo** (*Time Division Multiplexing* ou TDM) cria um sistema de rodízio entre os sinais. Desse modo, cada usuário utiliza toda a largura de banda disponível por um curto período de tempo de cada rodada.

Seu uso ocorre principalmente quando não se tem capacidade de transmissão que supra a capacidade de geração de sinais dos equipamentos conectados. Além disso, esse tipo de multiplexação pode ser **síncrona**, criando intervalos que são preenchidos pelos sinais, ou **assíncrona**, cuja implementação é mais complexa, mas elimina desperdícios.

## Modulação

O processo de alteração das características de um sinal a ser transmitido é chamado de **modulação**. Esse termo geralmente se refere ao deslocamento do sinal original para uma nova faixa de frequência. Pode ser por amplitude (AM), por frequência (FM) ou por fase (PM).

Na modulação, o sinal original (chamado de **sinal modulador**) é alterado por uma onda básica gerada pelo modem com esse propósito específico (chamada de **onda portadora**). O sinal resultante (chamado de **onda modular**) será transmitido e precisará ser "descontruído" pelo receptor para que se alcance o sinal modulador novamente.

A modulação **digital** traz diversas vantagens sobre a analógica, especialmente na recuperação do sinal original, visto que evita o acúmulo de ruídos e distorções. Porém, necessita de mais largura de banda que os métodos analógicos correspondentes.