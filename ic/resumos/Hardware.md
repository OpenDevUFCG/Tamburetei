---
title: Conceitos de Hardware
---
## Sumário
 - [Processador](#Processador)
 - [Memória](#memória)
 - [Entrada e Saída](#entrada-e-saída)
 
## Processador
 Tem como operações básicas: input, processing, output e storage.
  - UCP: Unidade Central de Processamento.
      - Manupula direta ou indiretamente os dados
      - Executa microinstruções
  Dentre as funções do processador está a de controle, e a de processamento.
      - Processamento:
          1. OLA - Operações Lógicas e Aritméticas.
          2. Memória -> CPU; registrador -> memória.
          3. Desvios e operações de Entrada e Saida
  - Barramentos(Bus):
       - Caminhos fisicos que levam os dados. Existem 3 tipos de barramentos, são eles:
            1. Adress Bus: trafega posições de memória.
            2. Data Bus: trafega dados para memória, processador ou perifericos.
            3. Control Bus: trafega sinais de controle.
            - USB - Universal Serial Bus.
   - Relógio (Clock):
   Gerador de pulsos a intervalos regulares para indicar a frequência e a velocidade do processador, mas não é 
   confiavél porque algumas micro-instruções gastam mais de um ciclo para serem realizadas.
   
   - Registradores:
   Memórias ultra rápidas que armazena dados temporários. A quantidade de bits processadores determina o tamanho do registrador.
   
   - Estratégias de Implementação
    - CISC: Complex Instruction Set Computer
        - Um grande conjunto de funções que implica em processador mais complexo e lento.
    - RISC: Reduced Instruction Set Computer
        - Um conjunto menor de instruções que precisa de apenas um ciclo para ser processado.
    - Híbrida:
        - Essencialmente CISC e internamente RISC.

## Memória
 Armazena informações em binário e é constituida de uma quantidade de células(e endereçoes) finita.
  - Endereço: codigo de identificação da localização.
  - Célula: unidade de informação a ser armazenada (1 byte)
 - Operações:
    - Escrita: transferência de informações de outro componente do sistema para a memória.
    - Leitura: transferência de informações da memória para outro componente do sistema.
 - Hierarquia:
    - Custo Alto, Velocidade Alta e Baixa Capacidade -> baixo custo,baixa velocidade e alta capacidade.
        1. Registradores
        2. Cache
        3. Memória Principal
        4. Discos
        5. Memória Secundária
        6. CD-ROM
 - Registradores
  Armazena dados e resultados que serão usdos na ULA.
    - Tempo de acesso: 1 a 5 ns
    - Capacidade: 8 a 64 bits
    - Volátil: Sim
    - Tecnologia: Semicondutores
    - Temporiedade: Armazenamento Temporario.
    - Custo: Altissimo.
  
  - Cache
  Evita gargalo entre registradores e memória principal.
    - Tempo de acesso: 5 a 7 ns
    - Capacidade: Varia
    - Volátil: Sim
    - Tecnologia: Circuitps eletrônicos (SRAM)
    - Temporiedade: Armazenamento Temporario.
    - Custo: Alt.
  
  - Memória Principal
  Memoria básica do PC, onde programas e dados são executados.
    - Tempo de acesso: 7 a 15 ns
    - Capacidade: 4GB a 32GB
    - Volátil: Sim, com exceção da BIOS
    - Tecnologia: Dinâmica (DRAM)
    - Temporiedade: Varia
    - Custo: Acessivel
    
    - Fatores limitantes do tamanho:
        - Endereçamente: depende do adress bus.
        - Chipset: controladore de memória
        - Físico: quantidade máxima de locais de encaixe para a memória.
     - Capacidade da MP:
          - T = N x M
          - T - capacidade em bits
          - N - nº de bits de cada célula
          - M - 2 elevado ao nº de linhas.
    
     - Memória Secundária
    Maior capacidade e permanência.
    - Tempo de acesso: 8 a 15 ns
    - Capacidade: Alta
    - Volátil: Não
    - Tecnologia: Varia
    - Temporiedade: Permanente
    - Custo: Baixo comparada as demais.
 ## Entrada e Saída
  Permitem a comunicação homem - máquina. Cada dispositivo se comunica com o núcleo de forma diferente, tal comunicação chamada de 
 protocolo é feita com a transferência de informações para interfaces (ao invés da UCP).
  - Interfaces: 
      - Compatibiliza com as diferentes características de um periférico e da UCP.
  - Comunicação Paralela:
      - bits transferidos simultâneamente.
      - taxa throughtput é alta.
      - Problema: **skew**, informação chegando fora de ordem.
  - Comunicação Serial:
      - bits transferidos de um a um (para longas distâncias)
  ### Transmições
   - Sincrona de caractere: intervalo de tempo fixo.
   - Assincrona de caractere: não fixo, para após 8 bits. Envia 1s até chegar em uma info(0)
   
   - Simplex:
   Transfere apenas do transmissor para o receptor em uma via única.
   - Half-Duplex: 
   O transmissor também pode assumir o papel de receptor, porém é feita uma transferência por vez.
   - Full-Duplex:
   O transmissor também pode assumir o papel de receptor, mas as transferências podem ser feitas simultaneamente
  
