# Guia de Conversão dos PDFs para Markdown
Olá, bom te ver por aqui engajado com o Open Source! Esse guia foi feito para te ajudar no processo de conversão dos PDFs do nosso site para Markdown, tentamos resumir e deixar bem explicado o básico de como fazer uma boa conversão. Sinta-se à vontade para falar com alguém do Core Team se surgir alguma dúvida durante o processo. Ah, não esquece de conferir nosso [Minicurso de Markdown - Hacktoberfest 2021](https://youtube.com/playlist?list=PLpRSAQI4X2czC1gDm_PoNJULIWpE2eO56) feito por [Leandra](https://github.com/LeandraOS).

## Provas e Listas de Exercícios

1.  No topo do arquivo inclua as informações sobre o PDF na seguinte ordem:
	- Nome da disciplina (Obrigatório)
	- Período da realização da atividade, ex: 2021.1, 2019.2. (Se for informado)
	 - Estágio da avaliação, ex: 1⁰/2⁰/3⁰ estágio. (Se for informado)
    
2.  Inclua uma seção “Questões” com as questões na mesma ordem do PDF e usando o mesmo estilo de numeração. Use o [Heading Level 3](https://www.markdownguide.org/basic-syntax/) do MD para o título “Questões” e um parágrafo comum para o enunciado das questões.
    
3.  Caso a prova/lista de exercícios tenha resolução, inclua uma seção "Resolução" ao final do arquivo MD, seguindo a mesma ordem das questões feita anteriormente. Aqui também é interessante usar o [Heading Level 3](https://www.markdownguide.org/basic-syntax/) do MD para o título “Resolução” e um parágrafo comum para o desenvolvimento da questão (fique à vontade para incluir bullet points ou outros elementos do MD se isso melhorar a visualização/entendimento da resolução).
    
4.  Por questões de acessibilidade, inclua tudo que for possível com MD, como [fórmulas](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions), [tabelas](https://www.markdownguide.org/extended-syntax/), etc. Só dê preferência a usar imagens quando for realmente necessário.

## Resumos
1.  No topo do arquivo inclua o nome da disciplina do resumo e o conteúdo que será resumido.
    -  Caso o resumo seja de todo o conteúdo da cadeira, você pode omitir o nome do conteúdo.
    
2.  Para cada tópico abordado, crie uma seção cujo título é o tópico que foi resumido. Use o [Heading Level 3](https://www.markdownguide.org/basic-syntax/) do MD para o título.
    
3.  A mesma questão de acessibilidade em provas e listas de exercícios se aplica aqui! (Leia o tópico 4 da seção Provas e Listas de Exercícios).

## Exemplificação

Você pode verificar um exemplo de como o seu arquivo em Markdown deve parecer acessando [esse arquivo](tc/leites/20221/provas/reposicao.md) de uma reposição de Teoria da Computação.

## Contribuindo
Agora que você concluiu essa conversão, que tal seguir [nosso tutorial de como criar seu primeiro Pull Request](GuiaPrimeiroPR.md) para contribuir com o Tamburetei?