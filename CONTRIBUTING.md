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

## Como ajudar?

Se você tem interesse em contribuir e não sabe como, procure issues com a tag `Good First Issue`. Não tenha medo de pedir por orientação ou ajuda, mas, acima de tudo, seja corajoso e respeitoso. Você também pode participar de discussões para ajudar a comunidade a realizar boas escolhas!

## Como funciona?

Cada cadeira do curso vai possuir seu próprio diretório, nele estarão os seguintes conteúdos:

Arquivo | Finalidade
------- | -----------
**visaoGeralEDicas.md** | Contém a ementa, uma visão geral sobre a disciplina e algumas dicas rápidas para quem vai começar a cursá-la.
**linksUteis.md** | Contém links de qualquer tipo de material que possa ser útil para estudar o assunto da disciplina.
**dificuldadesComuns.md** | Contém a descrição das dificuldades mais comuns da disciplina, assim como dicas para superá-las e relatos de alunos que já a cursaram.
**extras.md** | Caso necessário, outros tópicos devem ser inseridos nesse arquivo.
**leites/** | Diretório com os leites dos períodos passados, separados por período (em seções do README.md ou em pastas). Preferencialmente contém apenas provas e listas de exercícios.
**implementacoes/** | Caso a disciplina possibilite, esse diretório se destina a implementações úteis, fáceis de entender e bem documentadas.
**resumos/** | Esse diretório se destina a resumos sobre assuntos especifícos da disciplina. Devem ser bem divididos e fáceis de entender.

## Regras
- Respeite o código de conduta.
- Proibido falar mal dos professores. Evite, ao máximo, comentar opiniões pessoais de qualquer natureza sobre professores.
- Proibido publicar soluções de atividades avaliativas das disciplinas que se repetem todos os períodos, tais como os roteiros de LEDA e os laboratórios de LP2.

## Indicações

- Seja claro nos seus commits.
- Caso esteja tendo dificuldades de trabalhar com o Git, contate alguém da equipe e peça ajuda. 
- Caso vá realizar alguma implementação, respeite os padrões da comunidade e produza um código legível.
- Sempre que for mudar algo, verifique se é necessário alterar algo na documentação. É importante que tudo esteja atualizado.
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

Se você escolheu uma issue para contribuir, não esqueça de avisar lá que você está trabalhando nela. Se que contribuir com algo que ainda não foi citado em uma issue, crie-a! É importante notificar o que você está fazendo.

### Clone o repositório

Com a issue criada, o primeiro passo é criar um fork do nosso repositório. Existe um botão na página do GitHub para isso. Quando a criação dele for concluída, copie a url do repositório do fork e clone-o para a sua máquina. 

Caso queira fazer o clone através do terminal, o comando utilizado terá o seguinte formato:
```sh
git clone https://github.com/<seu_usuario>/Tamburetei
```

Onde seu usuário do GitHub ficará no campo **<seu_usuario>**.

Ao terminar de clonar, será criado um repositório *Tamburetei* no seu computador. Agora você tem a liberdade de, com seu editor favorito, fazer as alterações que achar necessário. Ao terminar, você deverá commitar suas alterações para o seu repositório remoto.

Usando o terminal, navegue até o seu repositório local do *Tamburetei*:
```sh
cd Tamburetei/
```

A seguir, adicione os arquivos a serem commitados. O comando abaixo irá adicionar todos os arquivos modificados de uma só vez para que sejam commitados.
```sh
git add . 
```

Após adicioná-los, chegou a hora de commitar os arquivos. Escolha uma mensagem que descreva bem as modificações que você fez e utilize o comando abaixo para realizar o commit:
```sh
git commit -m "<sua_mensagem_de_commit>"
```

Por fim, chegou de enviar todas as modificações feitas para o seu repositório remoto. Utilize o seguinte comando:
```sh
git push origin master
```

### Fazendo uma Pull Request

Indo na página do seu fork, você irá visualizar um aviso (em amarelo) solicitando que você faça uma Pull Request para o repositório original. Ao clicar nele, aparecerá uma página em que você deve preencher algumas informações sobre sua Pull Request.

- Referencie a issue que você está trabalhando usando **#<numero_da_issue>**.
- Descreva o que você fez.
- Esteja aberto a críticas construtivas e elogios! :)


## Extras

- [Tutorial mais detalhado](https://blog.da2k.com.br/2015/02/04/git-e-github-do-clone-ao-pull-request/).
- Caso precise realizar um [rebase ou merge](https://gist.github.com/ravibhure/a7e0918ff4937c9ea1c456698dcd58aa).
