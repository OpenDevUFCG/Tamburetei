---
title: Extras
---

Informações e conteúdos extras sobre a disciplina.

## Sumário

- [Como usar o TST](#como-usar-o-tst)
    - [Instalar](#instalar)
    - [Comandos](#comandos)
    - [Exemplo de Uso](#exemplo-de-uso)
        - [Login](#login)
    - [Checkout](#checkout)
    - [Testando](#testando)
    - [Enviando](#enviando)
    - [Respostas de erro](#respostas-de-erro)

## Como usar o TST

TST é o sistema de submissão das questões resolvidas por alunos nas provas e exercícios. Aqui vai um guia de como usar a ferramenta.

### Instalar
Primeiro, verifique se você já tem o PIP instalado.
```sh
pip3 --version
```
ou
```sh
pip --version
```
Caso você não tenha o PIP instalado, rode o seguinte comando:
```sh
sudo apt install python3-pip
```
 **Observe que pode ser necessário reiniciar o terminal para que ele reconheça o comando 'pip'**


Agora, você poder executar o comando abaixo para instalar o TST.
```sh
pip install --user p1ufcg
```

Após reiniciar o terminal e rodar 'p1', a saída esperada é a seguinte:
```sh
uso: p1 [login | logout | checkout | commit | info]
```
E a do comando 'tst' é:
```sh
No tst tests found
```

### Comandos
** O comando `tst --help` mostra todos os comandos disponíveis do tst. Atualmente, o comando 'tst' só é utilizado para rodar os testes locais das questões.
Todos os outros comandos, como o 'login' e o 'checkout' utilizam o comando 'p1'.

Agora uma lista de todos os comandos:

Comando | Descrição
------- | -----------
**checkout** | Baixa uma questão do TST, cria um objeto e um diretório contendo o nome da questão passada como argumento.
**commit** | Envia a sua resposta para o servidor.
**login** | Faz o login para o tst-online usando um token e seu email. Automaticamente abrirá uma página no seu browser requisitando o token.
**tst** | Valida sua resposta e roda os testes.

### Exemplo de Uso
Nessa seção iremos simular o primeiro uso do TST, fazendo o login, resolvendo uma questão do TST, testando-a e  a submetendo para o servidor.

#### Login
Primeiro você precisar se logar no [TST-ONLINE](http://tst-online.appspot.com/) e, depois, logar-se no seu terminal usando sua conta. Para isso, use:

```sh
p1 login
```

Após isso, você vai ser perguntado se deseja abrir uma janela no navegador padrão. Caso escolha "Não", você receberá um link que deve ser colado e copiado
no seu navegador. Você deve fazer o login social com sua conta Google "@ccc.ufcg.edu.br".

### Checkout
Agora vamos resolver uma questão, copie o checkout código de alguma questão do [TST](http://tst-online.appspot.com/#/) que você queria resolver e rode o seguinte comando:

```sh
p1 checkout <codigo_questao>
```
Esse comando irá criar um novo diretório, vá para o diretório e comece a implementar a sua solução:

```sh
cd <codigo_questao>
```
Caso queira fazer o checkout com um nome mais amigável, como por exemplo o nome da própria questão ao invés de seu código, também é possível fazer diretamente no checkout:

```sh
p1 checkout <codigo_questao> <nome_questao>
```
E em seguida:
```sh
cd <nome_questao>
```

### Testando
Após implementar sua solução, você pode testá-la usando:
```sh
tst <arquivo_da_questao>
```
Onde `<arquivo_da_questao>` é seu arquivo **.py**.

Se você tiver apenas um arquivo **.py** no seu diretório você apenas precisa usar:

```sh
tst
```
Se você recebeu uma saída contendo apenas pontos( Ex: `.`, `...`), vocês passou em todos os testes públicos e agora você pode submeter sua questão para o servidor.

### Enviando
Envie sua questão para o servidor:

```sh
p1 commit <arquivo_da_questao>
```


### Respostas de erro

Comando | Descrição
------- | -----------
**e** | O programa quebra(erro durante execução).
**s** | Erro de sintaxe.
**a** | Erro de atributo.
**o** | EOFError -> O programa possui mais entradas que o TST pede. (Programa possui 3 input's mas o TST pede 2)
**z** | Divisão por zero.
**i** | Erro de indentação.

