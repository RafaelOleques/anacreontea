# Ancient Greek's New Technological Muse: Extracting Topoi in the Anacreontea with LLMs

This repository contains the source code for the paper _Ancient Greek's New Technological Muse: Extracting Topoi in the Anacreontea with LLMs_, accepted at the 51st SEMISH (51º Seminário Integrado de Software e Hardware). 

Dataset available at HuggingFace: https://huggingface.co/datasets/ronunes/anacreontea

Topos and their definitions are available at GitHub: https://github.com/RafaelOleques/anacreontea/blob/main/topos.csv

Once the paper is available online, a link will be provided here.

**Abstract:**
> Natural Language Processing (NLP), along with Large Language Models (LLMs), holds significant potential in the domain of literature, leveraging its computational capabilities to analyze and comprehend human language. These techniques prove to be particularly useful in a specific part of Greek literature called Anacreaontea — a collection of poems emulating the style of the 6th-century BCE Greek poet Anacreon. This paper presents an LLM approach to the automatic classification of Anacreaontea poems in their respective topoi. Our methodology explores two well-established autoregressive language models (LLama 2 and Mistral) and investigates the usage of contextual prompting in this scenario. We also provide an annotated corpus with 21 fragments of the Anacreontea with topos for Greek and Portuguese text.

## Sources of Topoi and Portuguese Translations
The topoi and Portuguese translations were extracted from the following studies:

- Antunes, C. L. B. (2016). Entre amores ebrios e fazer artístico: Topoi e poíesis nas ‘anacreonticas’ — between drunken love and artistic praxis: Tópoi and poíesis in the ‘anacreontea’. Estudos Linguísticos e Literarios, (55):374–385.
- Antunes, C. L. B. (2013). As anacreonticas e a imagem de anacreonte na antiguidade. Letras Clássicas, 17(1):109–149.

## Reproducibility

You can reproduce the results or run with different fragments in _results.ipynb_. The code for the classifier is in _LLM_classifier.py_.

## Prompt example

Persona:
Você é um pesquisador especialista em literatura grega antiga com foco nos textos do corpus das anacreônticas.

Instrução:
Faça sua escolha baseado no que melhor representa a temática do texto. Utilize o nome da mesma forma que está no contexto.


Nome de cada tópos e seu contexto:
- "Loucura, sobriedade e as muitas vozes das Anacreônticas": Por ter sido composta por uma variedade de poetas, às vezes pode-se ter uma sensação de esquizofrenia ao ler as Anacreônticas. Na maioria dos poemas sobre o vinho, o eu-lírico dá mostras de uma intensidade de sentimento sem limites. Por outro lado, em outros poemas, nota-se a preocupação com os limites da bebedeira.
- "Poíesis": A preocupação com as artes é uma constante no corpus. Há uma grande quantidade de poemas em que o poeta interpela algum tipo de artesão (pintor, escultor ou ferreiro), pedindo-lhe que faça alguma obra de arte. Em outros, todo o discurso do poema gira em torno de alguma peça de arte que tem um significado especial para o eu lírico. Além dos poemas referentes a outras artes, há, sobretudo, aqueles que se centram em considerações acerca da arte de compor poesia.
- "Riqueza": O amor, o vinho e as artes das musas são defendidos também em detrimento do ouro e das preocupações com a vida.
- "Eros doceamargo": Apesar de eventuais defesas do Amor em detrimento da guerra, as anacreônticas a respeito de Eros, em geral, demonstram uma relação ambígua com o deus. A representação de Eros é sempre como a de um bebê gracioso e brincalhão, porém armado com setas que trazem dor ao coração dos mortais, as quais ele parece usar com total descaso em relação ao que resultará disso.
- "Velhice": Poemas que falam da velhice, os quais, geralmente, insistem na necessidade ainda maior de se gozar dos prazeres da vida quando velho.


Anacreôntica:\
"""\
Anseio pelas danças de\
Dioniso, o amante da alegria!\
Eu amo quando toco a lira\
Bebendo em companhia a um jovem,\
Mas mais que tudo eu amo pôr\
Guirlandas de jacintos ao\
Redor da testa e então brincar\
Na companhia de garotas.\
Meu coração não sabe o que é\
A inveja que lacera o peito.\
Eu fujo das velozes lanças\
De línguas dadas ao abuso.\
Detesto brigas junto ao vinho.\
Em festas cheias de alegria,\
Com moças feito flores frescas,\
Dançando ao som que vem da lira,\
Que eu leve a minha vida em paz\
""" 

Pergunta: Por favor, me informe qual tópos está presente nesta anacreôntica e qual é o mais representativo. \
Resposta: Vamos pensar passo a passo.
