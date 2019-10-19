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
O script abaixo baixa e configura o tst de maneira automática. Não use a permissão root nele.

```sh
bash -c "$(curl -q -sSL http://bit.ly/tst084)"
```

### Comandos
** O comando `tst --help` mostra todos os comandos disponíveis do tst. Além disso, o `tst <command> -- help` vai mostrar mais detalhes sobre o comando específico.

Agora uma lista de todos os comandos:

Comando | Descrição
------- | -----------
**checkout** | Baixa uma questão do TST, cria um objeto e um diretório contendo o nome da questão passada como argumento.
**commit** | Envia a sua resposta para o servidor.
**login** | Faz o login para o tst-online usando um token e seu email. Automaticamente abrirá uma página no seu browser requisitando o token.
**ls** | Lista todos os objetos do TST disponíveis.
**test** | Valida sua resposta e roda os testes.
**update** | Atualiza o TST para a última versão estável.

### Exemplo de Uso
Nessa seção iremos simular o primeiro uso do TST, fazendo o login, resolvendo uma questão do TST, testando-a e  a submetendo para o servidor.

#### Login
Primeiro você precisar se logar no [TST-ONLINE](http://tst-online.appspot.com/) e, depois, logar-se no seu terminal usando sua conta. Para isso, use:

```sh
tst login
```

Esse comando irá abrir uma nova aba no seu browser mostrando o token necessário para realizar o login e seu e-mail usado no TST-Online. Copie o Token e cole no terminal como indicado.

Além dessa maneira, você pode fazer o seguinte:

Logar no [TST-ONLINE](http://tst-online.appspot.com/) e depois acessar diretamente o [LINK PARA GERAR O TOKEN](http://tst-online.appspot.com/activate). Por último logar no terminal usando:
```sh
tst login <token>
```

### Checkout
Agora vamos resolver uma questão, copie o checkout código de alguma questão do [TST](http://tst-online.appspot.com/#/) que você queria resolver e rode o seguinte comando:

```sh
tst checkout <codigo_questao>
```
Esse comando irá criar um novo diretório, vá para o diretório e comece a implementar a sua solução:

```sh
cd <codigo_questao>
```
Caso queira fazer o checkout com um nome mais amigável, como por exemplo o nome da própria questão ao invés de seu código, também é possível fazer diretamente no checkout:

```sh
tst checkout <codigo_questao> <nome_questao>
```
E em seguida:
```sh
cd <nome_questao>
```

### Testando
Após implementar sua solução, você pode testá-la usando:
```sh
tst test <arquivo_da_questao>
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
tst commit <arquivo_da_questao>
```
Para verificar se você passou em todos os testes do servidor e sua resposta foi aceita use:

```sh
tst -s
```

### Respostas de erro

Comando | Descrição
------- | -----------
**e** | O programa quebra(erro durante execução).
**s** | Erro de sintaxe.
**a** | Erro de atributo.
**o** | EOFError -> O programa possui mais entradas que o sistema pede. (Programa possui 3 input's mas o sistema espera por 2)
**z** | Divisão por zero.
**i** | Erro de indentação.

