# Metodologia Scrum

## Sumário
- [Introdução](#Introdução)
- [Scrum Team](#Scrum-team)
- [Product Backlog](#Product-backlog)
- [Product Owner](#Product-owner)
- [Release Backlog](#Release-backlog)
- [Scrum Master](#Scrum-master)
- [Sprints](#Sprints)
- [Daily Scrum](#Daily-scrum)
- [Burndown Chart](#Burndown-chart)
- [Sprint Retrospective](#Sprint-retrospective)

## Introdução

Scrum é uma metodologia ágil, desenvolvida no intuito de ser um framework para gestão e planejamento de projetos de software. Também é considerado uma das melhores práticas de desenvolvimento ágil da atualidade.

![Esquematização do Scrum](https://www.desenvolvimentoagil.com.br/images/scrum/ciclo_scrum.gif)

Agora, serão apresentados alguns conceitos importantes do Scrum:

## Scrum Team

O *Scrum Team* consiste na equipe de desenvolvimento do sistema, e é composto idealmente por 6 a 10 pessoas. É importante ressaltar que o Scrum não provê necessariamente uma divisão para o time (programador, designer, analista de testes, etc), embora seja extremamente recomendado a existência desses papéis. Todos os integrantes do time trabalham juntos para completar o conjunto de trabalho com o qual se comprometeram.

## Product Backlog

> "Uma lista que contém todas as coisas que farão com que um projeto seja um sucesso!"

No processo de desenvolvimento de qualquer software, existem requisitos de várias partes: usuários, clientes, executivos ou até mesmo membros do time de desenvolvimento. Dentro de uma abordagem com Scrum, a união de todos os requisitos existentes é chamada de Product Backlog.

## Product Owner

A partir da lista de requisitos gerais (Product Backlog), é hora de começar a planejar e analisar quais serão as funcionalidades específicas (essenciais e desejáveis) para um determinado *release* do produto. É aí que entra o papel do Product Owner: ajudar a ter certeza de quais requisitos do Product Backlog serão necessários, representando os usuários e clientes do produto.

## Release Backlog

> **O Release Backlog pode ser igual ao Product Backlog!**

![Priorização do Product Backlog](https://www.visual-paradigm.com/servlet/editor-content/scrum/scrum-100-points-method/sites/7/2018/11/prioritized-product-backlog.png)

É o resultado final da filtragem do Product Backlog por parte do Product Owner, que contém todos os requisitos que a versão final do *release* que está sendo desenvolvido deve ter. O time, então, deve priorizar os requisitos da Release Backlog e fazer estimativas de quanto tempo de trabalho, esforço e complexidade será necessário para desenvolver cada um deles, para que, ao final, se possa prover uma ideia geral da quantidade de trabalho envolvido para completar todo o release.

Para realizar as estimativas, independentemente da técnica decidida pelo time, é importante que:

- Seja garantido que pelo menos 3 especialistas no assunto estão envolvidos.
- Espaços para prováveis imprevistos que possam vir a ocorrer sejam levados em consideração.

## Scrum Master

O Scrum Master é, em essência, um gerente de projetos. Seu trabalho é garantir que o projeto do produto esteja progredindo, e que cada membro do time de desenvolvimento tenha condições e ferramentas ideais para que realizem seus trabalhos dentro do processo.

Funções de um Scrum Master:

- Organização de reuniões.
- Monitoramento dos trabalhos que estão sendo feitos.
- Facilitar o desenvolvimento de uma *release*.

## Sprints

Com o *Release Backlog* em mãos, agora já se pode começar a planejar as sprints. Sprints representam o intervalo de tempo em que determinada(s) tarefa(s) deve(m) ser realizada(s). É bom lembrar que:

- O tempo de duração de uma Sprint pode variar de 2 a 30 dias, porém o mais comum e recomendado é que esteja na faixa de 15 a 20 dias.
- No início de cada sprint, se faz um ***Sprint Planning Meeting***, uma reunião de planejamento em que o *Product Owner* prioriza os itens do *Release Backlog*.
- Tarefas de uma sprints são transferidas do *Product Backlog* para o ***Sprint Backlog***, que é a lista de tarefas que o time de desenvolvimento se compromete a fazer dentro do período de duração da sprint.

![Sprint Backlog](https://reqtest.com/wp-content/uploads/2015/08/product-backlog.jpg)

- Ao final de cada Sprint, deve-se apresentar um mini-produto completamente testado com todos os requisitos definidos para aquela Sprint 100% implementados.

## Daily Scrum

A cada dia de uma Sprint, a equipe de desenvolvimento faz uma reunião diária, que é a *Daily Scrum*. O objetivo dessa reunião é disseminar conhecimento sobre o que foi feito no dia anterior, identificar impedimentos e priorizar o trabalho a ser realizado no dia que se inicia.

É extremamente importante, pois faz com que a equipe inteira possa ficar a par do estado do projeto.

Importante:

- Daily Scrums normalmente são realizadas no mesmo lugar.
- Todos os membros da equipe devem participar do Daily Scrum.
- É importante que a reunião não seja longa, com um tempo ideal de 15 a 20 minutos.
- Não se deve encarar uma Daily Scrum como uma reunião para **resolução** de problemas, questões do tipo que forem levantadas devem ser levadas para fora da reunião e tratadas por um grupo menor de pessoas envolvidas diretamente com o problema.

Perguntas importantes a serem feitas em uma Daily Scrum:

> O que você fez ontem?

> O que fará hoje?

> Há algum impedimento?

## Burndown Chart

![Burndown Chart](https://upload.wikimedia.org/wikipedia/commons/8/8c/Burn_down_chart.png)

O término tardio de uma Sprint é um grande indicador de que o produto não está no prazo, por isso é extremamente importante monitorar o progresso de cada uma delas.

Um ***Burndown Chart*** é uma ferramenta de visualização de projeto que assegura que o projeto esteja progredindo dentro do que foi programado.

Este gráfico provê valores diários para a quantidade de trabalho restante para liberar a Sprint para *release*, com a quantidade de tarefas restantes variando de cima para baixo ao decorrer dos dias.

Importante:

- O eixo horizontal de um Release Burndown Chart mostra os Sprints.
- O eixo vertical mostra a quantidade de trabalho que ainda precisa ser feita no início de cada Sprint.
- É comum que o eixo vertical esteja divido em: número ideal de tarefas que ainda precisariam ser feitas ao decorrer da sprint e número real de tarefas restantes.
- O trabalho que ainda resta pode ser mostrado na unidade preferencial da equipe: story points, dias ideais, team days e assim por diante.

A principal vantagem de se ter burndown charts é que a equipe pode comparar a velocidade ideal com que a equipe deveria desenvolver o projeto com a verdadeira velocidade e, assim, projetar uma data de entrega do projeto completo e ver se é uma estimativa realista.

## Sprint Retrospective

O *Sprint Retrospective* é um encontro que ocorre ao final de um Sprint, que serve para identificar o que funcionou bem, o que pode ser melhorado e que ações serão tomadas para melhorar o rendimento da equipe para as próximas Sprints.