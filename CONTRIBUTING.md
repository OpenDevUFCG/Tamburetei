# Contributing

Contribuições sempre serão bem vindas, sejam pequenas ou grandes. Leia o [código de conduta](https://github.com/OpenDevUFCG/Tamburetei/blob/master/CODE_OF_CONDUCT.md) antes de abrir qualquer issue ou pull request.

## Issues

As issues são um espaço aberto para requisitar criação, mudança ou conserto. Também é livre para ser um espaço de discussão sobre as cadeiras ~tamburetes~ de ciência da computação da UFCG. Tenha em mente que o tema sempre deve estar relacionado ao curso.

Nós temos a seguintes tags para issues:

- enhancement - Novas contribuições, informações e funcionalidades que devem ser feitas.
- bug - Alerta algum bug relacionado as implementações de código.
- discussion - Issue aberta com a finalidade de se discutir o assunto, qualquer um pode participar.
- help wanted - Issues que precisam de ajuda
- invalid - Algo que parece inválido.
- question - Pergunta feita para a comunidade.
- good first issue - Issue com dificuldade relativamente simples, um bom começo para começar a contribuir.

## Como ajudar

Se você tem o interesse de contribuir e não sabe como, procure issues com tag `good first issue`. Não tenha medo de perguntar por orientação ou ajuda, acima de tudo seja corajoso e respeitoso. Você também pode participar de discussões para ajudar a comunidade a tomar boas escolhas.

## Como funciona

Cada cadeira do curso vai possuir uma pasta separada, dentro de cada pasta irá existir os seguintes conteúdos:

Arquivo | Finalidade
------- | -----------
**visaoGeralEDicas.md** | Markdown contendo visão geral sobre a disciplina e algumas dicas rápidas para quem vai começar a pagar.
**linksUteis.md** | Contém links ou qualquer tipo de material que possa ser útil.
**dificuldadesComuns.md** | Aqui é permitido relatos e descrever dificuldades comuns na cadeira, e como superar essas dificuldades.
**extras.md** | Se for necessário algum tópico a mais, cabe nesse arquivo.
**leites/** | Pasta que contém leites dos períodos passados. Os mesmos devem estar separados por período em pastas.
**implementacoes/** | Caso a cadeira possibilite, aqui vale colocar algumas implementações úteis, devem ser fáceis de entender e bem documentadas.
**resumos/** | Resumos sobre algum assunto especifício, que seja bem dividido e fácil de entender.

Nós temos um script que cria essa estrutura, você só precisa ter o python instalado na sua máquina. 

Dito isso, navegue até a pasta [scripts](scripts/):

`cd scripts`

E em seguida, execute o comando:

`python create_folder_structure.py`

## Como Contribuir

Se você escolheu uma issue para contribuir, não esqueça de avisar lá que você está trabalhando naquilo. Se é algo que ainda não exista uma issue, crie! É importante notificar o que você está fazendo.

### Clonar o repositório

Após isso, você deve dar um fork do projeto. Existe um botão na página do github para isso. Quando ele terminar de realizar o fork, você deve copiar a url do repositório do fork e clonar na sua máquina. 


Feito no terminal, será algo assim:
```sh
git clone https://github.com/<seu_usuario>/Tamburetei
```

Onde seu usuário ficará no campo **<seu_usuario>**.

Ao terminar de clonar, será criado um repositório *Tamburetei* no seu computador. Agora você tem a liberdade de com seu editor favorito fazer as edições que você achar necessário, ao terminar, você deve commitar suas alterações no seu repositório remoto.

Entre no repositório do *Tamburetei*

```sh
cd Tamburetei/
```

Esse primeiro comando irá adicionar todos seus arquivos do diretório atual para serem commitados.

```sh
git add . 
```

Commita seus arquivos, junto com sua mensagem do commit, é muito importante que você descreva de maneira simples e clara o que você fez.

```sh
git commit -m "<sua_mensagem_de_commit>"
```

Finalmente, você irá enviar para seu repositório remoto todas as alterações feitas.

```sh
git push origin master
```

### Fazendo uma Pull Request

Indo na página do seu fork, você irá visualizar um aviso solicitando que em amarelo você faça uma Pull Request para o repositório original. Ao clicar apareça uma página onde você deve preencher informações sobre sua pull request

- Referencie a issue que você está trabalhando usando #<numero_da_issue>

- Descreva o que você fez

- Esteja aberto a críticas construtivas e elogios :)

[Tutorial mais detalhado](https://blog.da2k.com.br/2015/02/04/git-e-github-do-clone-ao-pull-request/).

*Obs: Caso precise realizar um [rebase ou merge](https://gist.github.com/ravibhure/a7e0918ff4937c9ea1c456698dcd58aa)

## Indicações

- Seja claro nos seus commits.
- Caso vá realizar alguma implementação, respeite os padrões e faça um código legível.
- Sempre que for mudar algo, verifica se é necessário mudar alguma documentação. É importante que tudo esteja atualizado.
- Caso esteja tendo dificuldades de trabalhar com o git, contate alguém da equipe e peça ajuda. 

## Regras

- Respeite o código de conduta.
- Proibido publicar soluções de atividades avaliativas das disciplinas que são as mesmas todos os anos. Como exemplo roteiros de LEDA e laboratórios de LP2.
- Proibido falar mal dos professores. Evitem comentar sobre professores ao máximo.
