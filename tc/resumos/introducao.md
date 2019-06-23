# Introdução

O estudo da **Teoria da Computação** preocupa-se com a capacidade do computador independente dos fatores técnicos, como a linguagem de programação e o *hardware* utilizados, portanto, analisa a solubilidade de problemas. Ainda, na impossibilidade de encontrar soluções, procura por respostas sub-ótimas para estes problemas.

Embora o grande objetivo seja compreender os limites da computação, existem muitas aplicações de conceitos de Teoria da Computação como modelar um pedaço de hardware, modelar uma comunicação, descrever padrões, descrever o que é válido em uma linguagem, etc.

Nesse contexto, determinar a **complexidade** e a **solubilidade** de problemas é vital para empregar os recursos necessários para resolvê-los, se for possível.

Um **autômato** é uma máquina (ou modelo computacional) projetada para seguir automaticamente uma sequência predeterminada de operações ou para responder a instruções codificadas. Enquanto um **computador** é uma máquina real que realiza computações, um **modelo computacional** é uma máquina abstrata, simplificada e sob controle.

As **máquinas de estados** são modelos simples de computadores utilizados em muitas aplicações (como sistemas embarcados simples) que reagem às entradas conhecidas, que conhecem sua especificação (ou seja, como funcionam) e que conhecem seu estado atual nesta especificação. Para compreendê-las, é importante entender os seguintes conceitos:

- **Alfabeto:** Conjunto de símbolos que podem ser utilizados como entrada da máquina abstrata.
- **Cadeia:** Também chamada de palavra, é uma concatenação finita de símbolos do alfabeto em uso.
- **Linguagem:** Conjunto de todas as cadeias do alfabeto em uso que levam à aceitação de um autômato.
- **Processar:** Tratar os símbolos que compõem a cadeia de entrada, um a um e conforme a sequência em que estão escritos.
- **Estado:** Representa a situação atual da máquina de estados, sendo a única porção importante de sua "história". O estado inicial é aquele em que a máquina começa o processamento da cadeia.