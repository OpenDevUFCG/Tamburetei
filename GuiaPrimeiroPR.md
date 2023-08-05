# Guia para o Primeiro Pull Request (PR)

## Introdução

Olá tambureteiro, este guia tem como objetivo fornecer um passo-a-passo para realizar sua primeira contribuição para este repositório. Pull Requests são uma forma de contribuir para projetos de código aberto, permitindo que você proponha alterações para o código existente, documentação ou correção de erros. No nosso caso, servirá para você adicionar, corrigir ou aprimorar conteúdos referentes as disciplinas ofertadas no curso.

## Passos para o seu primeiro Pull Request

1. Crie/acesse sua conta no GitHub.

![Acesse o Github](/gifs-primeiro-pr/login.gif)

2. Clone do repositório: Faça um fork do repositório do tamburetei. No canto superior direito do repositório, clique no botão "Fork" para criar sua cópia do repositório.

![Fork](/gifs-primeiro-pr/fork.gif)

3. Clone do seu fork: Clone o repositório do seu fork para o seu computador usando o seguinte comando no terminal (substitua seu-usuario pelo seu nome de usuário do GitHub e repositorio pelo nome do repositório que você forkou):

```
git clone https://github.com/seu-usuario/repositorio.git
```

![Clone](/gifs-primeiro-pr/clone.gif)

4. Certifique-se de estar na branch correta: Use o seguinte comando para mudar para o branch principal do repositório:

```
git branch

# caso precise
git checkout master
```

![Branch](/gifs-primeiro-pr/branch.gif)

Agora você está pronto para fazer suas alterações e criar o seu primeiro Pull Request.

5. Faça as alterações: Agora que você está em um branch separado, faça as alterações necessárias nos arquivos do repositório usando um editor de texto ou IDE.

![Code](/gifs-primeiro-pr/code.gif)

6. Após fazer as alterações, é hora de fazer o commit para registrar as mudanças que você fez no repositório. Use os seguintes comandos:

```
git add .
git commit -m "Breve descrição das alterações"
```

Certifique-se de fornecer uma mensagem de commit descritiva, indicando o que foi feito nas alterações.

8. Antes de enviar o Pull Request, verifique se o seu repositório remoto (no seu GitHub) está atualizado. Use o seguinte comando para enviar o branch e as alterações para o seu repositório no GitHub:

```
git push origin main
```

9. Agora que você enviou o branch com as alterações para o seu repositório no GitHub, você pode criar o Pull Request. No seu repositório no GitHub, vá para a página do branch que você enviou e clique no botão "Compare & pull request". Preencha as informações necessárias para o Pull Request e clique em "Create pull request".

![PR](/gifs-primeiro-pr/pr.gif)

10. Aguarde a revisão e aceitação: Agora o seu Pull Request foi criado e o core team do OpenDev será notificado sobre a sua contribuição. Aguarde a revisão das suas alterações e, se necessário, faça as correções solicitadas pelos revisores. Se tudo estiver certo, seu PR será aceito e suas alterações serão incorporadas ao projeto.

Parabéns! Você fez o seu primeiro Pull Request!

## Dicas adicionais

- Antes de começar a contribuir para um projeto, verifique as [diretrizes de contribuição]() do projeto.

- Mantenha o seu Pull Request pequeno e focado em uma única tarefa. Isso facilitará a revisão e a aceitação das suas alterações.

- Seja cortês e aberto a feedback. A contribuição em projetos de código aberto envolve colaboração com outros desenvolvedores e aprimoramento mútuo.

- Lembre-se de que contribuir para projetos de código aberto é uma jornada de aprendizado e crescimento contínuo. Com o tempo, você se tornará um contribuidor mais experiente e valioso para a comunidade.
