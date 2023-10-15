# Guia para o Primeiro Pull Request (PR)

Olá tambureteiro, este guia tem como objetivo fornecer um **passo-a-passo para realizar sua primeira contribuição para este repositório**.

Pull Requests são uma forma de contribuir para projetos de código aberto, permitindo que você proponha alterações para o código existente, documentação ou correção de erros. No nosso caso, servirá para você adicionar, corrigir ou aprimorar conteúdos referentes as disciplinas ofertadas no curso.

## Passos para o seu primeiro Pull Request

**1. Crie/acesse sua conta no GitHub.**

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/login.gif" alt="Acesse o Github" height="320">
</p>
<br />

-----

**2. Fork do repositório:** Faça um fork do repositório do [tamburetei](https://github.com/OpenDevUFCG/Tamburetei/). No canto superior direito do repositório, clique no botão "Fork" para criar sua cópia do repositório.

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/fork.gif" alt="Fork" height="320">
</p>
<br />

-----

**3. Clone fork do repositório para o seu computador usando o seguinte comando no terminal:**

```shell
git clone https://github.com/seu-usuario/tamburetei.git
```

Saída esperada:
```shell
user@machine:~$ git clone https://github.com/seu-usuario/tamburetei.git
Cloning into 'tamburetei'...
remote: Enumerating objects: 7189, done.
remote: Counting objects: 100% (1409/1409), done.
remote: Compressing objects: 100% (794/794), done.
remote: Total 7189 (delta 703), reused 1167 (delta 561), pack-reused 5780
Receiving objects: 100% (7189/7189), 56.74 MiB | 11.94 MiB/s, done.
Resolving deltas: 100% (3969/3969), done.
```

⚠ Substitua `seu-usuario` pelo seu nome de usuário do GitHub.

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/clone.gif" alt="Clone" height="320">
</p>
<br />

-----

**4. Certifique-se de estar na branch correta**

Entre no diretório do projeto e use o seguinte comando para mudar para o branch principal do repositório (`branch:master`):

```shell
cd tamburetei
git branch
```

A saída esperada:

```shell
user@machine:~$ cd tamburetei
user@machine:~/tamburetei$ git branch
* master
```

Caso você esteja em outra branch, execute:

```shell
git checkout master
```

A saída esperada:

```shell
user@machine:~/tamburetei$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
```

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/branch.gif" alt="Branch" height="320">
</p>
<br />

 -----
 
**5. Faça as alterações:** Agora que você está em um branch separado, faça as alterações necessárias nos arquivos do repositório usando um editor de texto ou IDE.

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/code.gif" alt="Code" height="320">
</p>
<br />

-----

**6. Após fazer as alterações**, é hora de fazer o commit para registrar as mudanças que você fez no repositório. Use os seguintes comandos:

```
git add .
git commit -m "Breve descrição das alterações"
```

⚠ Certifique-se de fornecer uma mensagem de commit descritiva, indicando o que foi feito nas alterações.

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/commit.gif" alt="Code" height="320">
</p>
<br />

-----

**7. Antes de enviar o Pull Request, verifique se o seu repositório remoto (no seu GitHub) está atualizado.**

```
git pull origin master
```

-----

**8. Use o seguinte comando para enviar o branch e as alterações para o seu repositório no GitHub:**

```
git push origin master
```

> Caso encontre um erro após o comando acima, mais especificamente após inserir a sua senha, leia o seguinte artigo:<br>
[Tokens - Github](https://www.alura.com.br/artigos/nova-exigencia-do-git-de-autenticacao-por-token-o-que-e-o-que-devo-fazer)

-----

**9. Agora que você enviou o branch com as alterações para o seu repositório no GitHub, você pode criar o Pull Request.**

No seu repositório no GitHub, vá para a página do branch que você enviou e clique no botão "Compare & pull request". Preencha as informações necessárias para o Pull Request e clique em "Create pull request".

<br />
<p align="center">
  <img src="/gifs-primeiro-pr/pr.gif" alt="PR" height="320">
</p>
<br />

-----

**10. Aguarde a revisão e aceitação**

Agora o seu PR foi criado e o core team do OpenDev será notificado sobre a sua contribuição. Aguarde a revisão das suas alterações e, se necessário, faça as correções solicitadas pelos revisores. Se tudo estiver certo, seu PR será aceito e suas alterações serão incorporadas ao projeto.

Parabéns! Você fez o seu primeiro Pull Request!🥳🥳

## Dicas adicionais

- Antes de começar a contribuir para um projeto, verifique as [diretrizes de contribuição](/CONTRIBUTING.md) do projeto.

- Mantenha o seu **Pull Request pequeno** e focado em uma única tarefa. Isso facilitará a revisão e a aceitação das suas alterações.

- Seja cortês e aberto a feedback. A contribuição em projetos de código aberto envolve colaboração com outros desenvolvedores e aprimoramento mútuo.

- Lembre-se de que contribuir para projetos de código aberto é uma jornada de aprendizado e crescimento contínuo. Com o tempo, você se tornará um contribuidor mais experiente e valioso para a comunidade.
