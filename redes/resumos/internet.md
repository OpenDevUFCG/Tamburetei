# Internet

# O que é?

- “Rede de Redes”
- Milhões de elementos de computação interligados:
    - hospedeiros = sistemas finais
- Executando aplicações distribuídas
- Enlaces de comunicação:
    - fibra, cobre, radiofrequencia
    - largura de banda variável
- Roteadores
    - encaminham pacotes (blocos de dados) para seus destinos finais

## Pontos de Troca de Tráfego (PTTs)

- Plataformas compartilhadas de serviços;
- Local onde muitas organizações se juntam e interligam sua tecnologia de redes;
    - Qualquer organização que necessite de rede
    - Reduzem custo
- A troca de tráfego torna a internet mais rápida e acessível

## Governança da Internet

- Não há autoridade única
- Construção coletiva entre todos que a usam
- Descentralização
- Internet global, mas cada país tem suas leis sobre ela

### Colaboração

- Qualquer um pode participar
- Multistackholder

### Padrões Tecnológicos

- Fundamental para o funcionamento da internet
- Todos os interessados podem participar
- IETF
    - ***Internet Engineering Task Force*** é um grupo internacional aberto que tem como missão identificar e propor soluções a questões/problemas relacionados à utilização da Internet, além de propor padronização das tecnologias e protocolos envolvidos.
    - cooperação com o *[World Wide Web Consortium](https://pt.wikipedia.org/wiki/World_Wide_Web_Consortium) (W3C)*
- W3C
    - principal organização de [padronização](https://pt.wikipedia.org/wiki/Padroniza%C3%A7%C3%A3o) da [World Wide Web](https://pt.wikipedia.org/wiki/World_Wide_Web)

### Distribuição dos endereços

- IP
    - **Internet Protocol address** é um rótulo numérico atribuído a cada dispositivo conectado a uma [rede de computadores](https://pt.wikipedia.org/wiki/Rede_de_computadores) que utiliza o [Protocolo de Internet](https://pt.wikipedia.org/wiki/Protocolo_de_Internet) para comunicação
- ASN
    - Número do sistema autônomo (ASN) é um identificador globalmente exclusivo que define um grupo de um ou mais prefixos IP executados por um ou mais operadores de rede que mantêm uma única política de roteamento claramente definida
- Únicos globalmente
- IANA (Internet Assigned Numbers Authority)
    - Autoridade para Atribuição de Números da Internet é a organização mundial que supervisiona a atribuição global dos números na Internet
        - números das portas
        - os endereços IP
        - sistemas autónomos
        - servidores-raiz de números de domínio DNS
        - outros recursos relativos aos protocolos de Internet.
    - RIR (Registro Regional da Internet)
        - supervisiona a atribuição e registro dos recursos de números Internet dentro de uma determinada região do mundo
        - LACNIC (Registro de Endereços da Internet para a América Latina e o Caribe)
        - NIC.br (Núcleo de Informação e Coordenação do Ponto BR)

### Gestão de domínios

- DNS (Domain Name System)
    - sistema hierárquico e distribuído de gestão de nomes para computadores, serviços ou qualquer máquina conectada à Internet ou a uma rede privada
- ICANN (corporação da internet para atribuição de nomes e números)
    - Servidores raiz
    - Domínios genéricos como .com

# Protocolos de Redes

## O que são?

- conjunto de regras que são utilizadas por computadores para estabelecer a comunicação entre eles

## TCP/IP (**Protocolo de controle de transmissão**)

- Protocolo único para comunicação entre todos os dispositivos na internet
- LAN
    - Local Area Network (Computadores próximos)
- WAN
    - Wide Area Network (Rede de longa distância)
- O TCP/IP surgiu com a DARPA (Defense Advanced Research Projects Agency)
    - Precisava de uma rede de comunicação entre computadores militares
    - Tolerante a falhas
        - Se um computador é atacado, a conexão não pode ser perdida
- ISOC (Internet Society)
    - Sociedade não governamental que é responsável pela internet
    - IAB (Internet Architecture Board)
        - entidade responsável pela alocação do espaço de endereços do Protocolo da Internet (IPv4 e IPv6), pela atribuição de identificadores de protocolo, …
        - IETF (Internet Engineering Task Forces)
            - Dar solução técnica aos problemas
            - Definir padrões da internet
        - IRTF (Internet Research Task Force)
            - Pesquisa a longo prazo
            - Propor mudanças ou soluções para padrões já realizados
        - IANA
            - Distribuição dos endereços e de portas (IP, DNS, FTP, ...)

## Padrão vs Implementação

- Segue o padrão RFC (Request for Comments)
    - Definem os padrões de rede e de protocolos TCP e IP
    - Todas as empresas seguem esse padrão (Windows, Linux, Android)
- Algumas implementações obrigatórias e outras opcionais