# Início em IA

Este repositório contém um projeto introdutório de Inteligência Artificial em Python, focado em classificação de textos e análise de comentários sobre aulas.

O objetivo principal é demonstrar, de forma simples, como:
- carregar dados em um CSV;
- transformar texto em dados numéricos;
- treinar um modelo de classificação;
- testar frases novas;
- criar um programa interativo para classificar comentários.

## Conteúdo do repositório

- `ia_frases.py` — script que treina um modelo de classificação textual usando `pandas` e `scikit-learn`.
- `classificar_aula.py` — script interativo que classifica comentários em `Positivo`, `Negativo` ou `Neutro`.
- `Criação de uma IA.pdf` — material complementar com explicações do projeto.

## Visão geral

Este projeto foi criado como uma introdução prática ao aprendizado de máquina e ao processamento de linguagem natural (NLP). A ideia é mostrar como uma máquina pode aprender a identificar emoções e sentimentos em textos simples, como avaliações de aulas.

## Como funciona

### 1) Classificação textual com machine learning
O arquivo `ia_frases.py` realiza os seguintes passos:

1. lê um dataset de comentários;
2. separa as frases da classificação;
3. divide os dados em treinamento e teste;
4. converte texto em números com `TfidfVectorizer`;
5. treina um modelo `LogisticRegression`;
6. mede a acurácia do modelo;
7. testa uma frase nova.

### 2) Classificação interativa
O arquivo `classificar_aula.py` analisa frases digitadas pelo usuário e compara palavras-chave positivas e negativas. Exemplo:

- positivas: `excelente`, `ótima`, `ótimo`, `interessante`
- negativas: `ruim`, `péssima`, `péssimo`, `difícil`

Com base nessas palavras, o programa retorna uma classificação final.

## Estrutura esperada do dataset

Para o script `ia_frases.py`, o arquivo `comentarios.csv` deve ter um formato semelhante a este:

```csv
frase,classificacao
"Eu adorei a aula!",1
"A aula foi muito ruim.",0
"Foi interessante, mas poderia melhorar.",1
"Essa aula está difícil.",0
```

Legenda:
- `1` = positivo
- `0` = negativo

## Requisitos

Antes de rodar os scripts, instale as dependências:

```bash
pip install pandas scikit-learn
```

## Como executar

### Treinar e testar o modelo

```bash
python ia_frases.py
```

### Executar o classificador interativo

```bash
python classificar_aula.py
```

## Observações

- Este projeto é um exemplo didático de introdução à IA e Machine Learning.
- O código foi pensado para fins de estudo e demonstração.
- O projeto pode ser expandido com mais dados, pré-processamento melhorado e outros modelos.

## Autor

- Alanzin82

## Licença

Este repositório não possui uma licença definida explicitamente no projeto.