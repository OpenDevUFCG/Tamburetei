# Contributing

Contribuições sempre serão bem vindas, sejam pequenas ou grandes. Leia o [código de conduta](https://github.com/OpenDevUFCG/Tamburetei/blob/master/CODE_OF_CONDUCT.md) antes de abrir qualquer issue ou pull request.

## Issues

As issues são um espaço aberto para requisitar criação, mudança ou conserto de material. Também pode ser usada como um espaço de discussão sobre as cadeiras ~tamburetes~ de Ciência da Computação da UFCG. Tenha em mente que o tema sempre deve estar relacionado ao curso.

Atualmente, temos a seguintes tags para issues:

- **Bug** - Alerta sobre algum bug relacionado às implementações de código.
- **Congelado** - A issue está temporariamente inativa, será retomada futuramente.
- **Discussão** - Indica que a issue foi aberta com a finalidade de se discutir um assunto. Qualquer um pode participar.
- **Duplicado** - Alerta de que a issue atual é idêntica (ou muito semelhante) a uma já existente.
- **Em andamento** - Indica que as atividades requisitadas pela issue já estão sendo executadas.
- **Feature** - Indica que a issue está relacionada a uma nova funcionalidade ou nova requisição de material.
- **Good First Issue** - Indica que a issue é de dificuldade relativamente simples, um bom começo para novos contribuintes.
- **Inválido** - Alerta sobre algo que parece inválido.
- **Precisa de ajuda** - Indica que se precisa de ajuda para resolver o tópico da issue.
- **Descontinuado** - Indica que o tópico da issue foi descontinuado e não será retomado.


## Por onde começar?

Se você tem interesse em contribuir e não sabe como, procure issues com a tag `Good First Issue`. Não tenha medo de pedir por orientação ou ajuda, mas, acima de tudo, seja corajoso e respeitoso. Você também pode participar de discussões para ajudar a comunidade a realizar boas escolhas!


## Como funciona?

Cada cadeira do curso vai possuir seu próprio diretório, nele estarão os seguintes conteúdos:

Arquivo | Finalidade
------- | -----------
**resumos/** | Esse diretório se destina a resumos sobre assuntos especifícos da disciplina. Devem ser bem divididos e fáceis de entender.
**implementacoes/** | Esse diretório, que existe apenas para disciplinas em que seja pertinente, se destina a implementações úteis para os aqueles que estejam cursando a disciplina. Devem ser fáceis de entender e bem documentadas.
**dificuldadesComuns.md** | Contém a descrição das dificuldades mais comuns da disciplina e relatos de alunos que já a cursaram.
**extras.md** | Caso necessário, outros tópicos devem ser inseridos nesse arquivo.
**leites/** | Diretório com os leites dos períodos passados, separados por período (em seções do README.md ou em pastas). Preferencialmente, contém apenas provas e listas de exercícios.
**linksUteis.md** | Contém links de qualquer tipo de material que possa ser útil para estudar os assuntos da disciplina.
**visaoGeralEDicas.md** | Esse arquivo contém três seções: *Ementa*, uma lista dos tópicos formalmente abordados na disciplina, *Visão Geral*, uma breve descrição da disciplina e de sua importância para a carreira do cientista da computação, e *Dicas*, uma lista de dicas úteis para aqueles que irão começar a cursar a disciplina.

Para facilitar a criação dessa estrutura, você pode utilizar um *script* que disponibilizamos. Para usá-lo, basta ter Python instalado em sua máquina. Dito isso, navegue até a pasta [scripts](scripts/) em seu terminal:

```sh
cd scripts
```
Dê permissão ao arquivo:
```
chmod +x create_folder_structure
```
E em seguida, execute o comando:

```sh
./create_folder_structure
```

Agora basta informar o nome da disciplina e a nova pasta será criada!


## Regras

- Respeite o código de conduta.
- Proibido falar mal dos professores. Evite, ao máximo, comentar opiniões pessoais de qualquer natureza sobre professores.
- Proibido publicar soluções de atividades avaliativas das disciplinas que se repetem todos os períodos, tais como os roteiros de LEDA e os laboratórios de LP2.


## Indicações

- Seja claro em seus commits.
- Caso esteja tendo dificuldades de trabalhar com o Git, contate alguém da equipe e peça ajuda. 
- Caso vá realizar alguma implementação, respeite os padrões da comunidade e produza um código legível.
- Sempre que for mudar algo, verifique se é necessário alterar algo na documentação. É importante que tudo esteja atualizado!
- Ao produzir materiais textuais (como resumos), dê preferência a arquivos *.md*. Arquivos *.pdf* e *.doc* tornam o nosso repositório muito pesado.


## Restrições de Upload

### Material de Terceiros

#### O que posso referenciar (linkar)?

Qualquer material útil que esteja **publicamente** disponível na internet pode ser referenciado. Se os materiais de uma disciplina são mantidos disponíveis em um site, referencie-o no `linksUteis.md`.
O link de arquivo no Google Drive não é publicamente disponível, tá? (:

#### O que posso upar?

Essa é uma pergunta mais difícil. Prioritariamente, o Tamburetei quer disponibilizar **provas** e **listas de exercícios** de períodos passados. Em alguns casos particulares, outros tipos de materiais, como slides, também são permitidos.

No entanto, por exceção das provas (que se tornam documentos públicos), esses materiais podem estar protegidos por *copyright*. Então, se o material que você deseja upar tem o nome de um professor, precisaremos da autorização dele antes, certo?

**Ainda não tem certeza se pode upar?** Consulte um de nossos membros e esclareceremos sua dúvida!

### Tipos de Arquivo

Visando manter o repositório leve e respeitar as limitações da hospedagem gratuita no GitHub, a equipe do Tamburetei fará o possível para manter apenas **markdowns** *(.md)* e **arquivos de código** *(.py, .java, etc)* em nosso repositório. Por isso, arquivos muito grandes ou com outras extensões serão movidos para nosso Google Drive e referenciados aqui através de links.

`Essa restrição não afeta as contribuições, apenas informa que arquivos aqui hospedados poderão ser transferidos posteriormente.`


## Como contribuir?

### 1. Git e GitHub

O Git e o GitHub são poderosas ferramentas de versionamento de código que utilizamos para hospedagem e manutenção do Tamburetei. Caso você não tenha experiência com essas tecnologias ou tenha dúvidas sobre as seções a seguir, esse [guia](https://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/) pode ser de grande auxílio em sua jornada.

**Ainda restam dúvidas?** Contate um dos membros de nossa equipe! Estaremos sempre dispostos a ajudar!

### 2. Escolha uma *Issue*

O primeiro passo é escolher uma *issue* em que você deseja contribuir. Lembre-se de avisar nessa *issue* que você estará trabalhando nela, é muito importante manter todos notificados sobre o que já está sendo feito. Quer contribuir com algo que ainda não é uma *issue*? Não tem problema! Todos podem criar *issues* que achem pertinentes ao repositório.

### 3. Crie o seu *Fork*

Com a issue escolhida ou criada, é hora de *forkar* o Tamburetei. Vá até a página inicial do [repositório](https://github.com/OpenDevUFCG/Tamburetei) e clique no botão **Fork** que se encontra no topo da página à direita. Ao fim do processo, copie a URL do repositório criado (o "seu" Tamburetei).

**P.S.:** Essa URL seguirá o formato `https://github.com/<seu_usuario>/Tamburetei`, em que `<seu_usuario>` é o seu usuário do GitHub. Por fins didáticos, iremos chamá-la apenas de `<url_do_fork>` a partir daqui.

### 4. Clone o repositório

Com o *fork* criado, é hora de ter nosso repositório em sua máquina através da clonagem de repositório. Essa operação pode ser feita através do terminal com o comando `git clone` e a URL do seu fork. Dito isso, vá até seu terminal e use o seguinte comando:

```sh
git clone <url_do_fork>
```
Ao término da execução do comando, terá sido criado um repositório *Tamburetei* no seu computador.

### 5. Produza conteúdo

Esse momento é todo seu! Com seu repositório local, você tem a liberdade de fazer as alterações que julgar necessárias. Produza ou adicione todo o conteúdo que ache útil para a *issue* que você escolheu, ele será muito bem vindo! 

### 6. Commite as modificações

Ao terminar de adicionar o conteúdo que desejava, chegou a hora de *commitar* suas alterações para o repositório remoto. Em outras palavras, iremos levar essas modificações para o repositório que todos podem visualizar *online*.

Inicialmente, utilizando o comando `cd` no terminal, navegue até o seu repositório local do *Tamburetei*:

```sh
cd Tamburetei/
```
A seguir, adicione os novos arquivos com o comando `git add`. Com o comando abaixo, todos os arquivos modificados (ou criados) serão adicionados de uma só vez.

```sh
git add . 
```

Após adicioná-los, chegou a hora de commitar esses arquivos usando o comando `git commit`. Escolha uma mensagem que descreva bem as modificações que você fez e utilize o comando abaixo para realizar o commit:

```sh
git commit -m "<sua_mensagem_de_commit>"
```

Por fim, envie todos os *commits* para o seu repositório remoto através do `git push`. Utilize o seguinte comando:

```sh
git push origin master
```
Pronto! Agora todas as modificações que você fez localmente estão também disponíveis no seu repositório remoto (*fork*)!

### 7. Crie uma PR

Agora que as modificações estão no repositório remoto do seu *fork*, você pode sugerir a adição delas no repositório do Tamburetei através de uma *Pull Request*. 

Para isto, vá até a página do seu fork e clique no botão **New Pull Request**. Seu navegador será direcionado a uma página que lista todos os commits do seu *fork* que não estão presentes no Tamburetei original. Nela, clique no botão **Create Pull Request** e preencha os campos textuais seguindo as instruções ali presentes. Por fim, confirme a criação da PR e aguarde a avaliação de um dos membros de nossa equipe. 

**Assim que possível alguém irá aprovar sua PR ou requisitar as mudanças necessárias!**
