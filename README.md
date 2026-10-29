# Beach Decision Tree

**A small machine learning project that predicts whether to go to the beach using the day's temperature and sunshine hours.**

This repository is an educational example of a decision tree classifier built with Python and scikit-learn. It includes a command-line program, a small CSV dataset, and a graphical interface for entering new weather conditions.

## What the project does

The model uses two input features:

- `temperatura_c`: temperature in degrees Celsius.
- `horas_sol`: number of sunshine hours.

It predicts the target `vai_a_praia`, whose values are `Sim` (yes) and `Não` (no). The model learns patterns from the examples in `data/exercicio_ml_praia.csv` and applies those patterns to a new pair of values.

The classifier is a **decision tree**. During training, it learns a sequence of feature-based splits that separate examples with different target labels. For example, it may learn that certain combinations of temperature and sunshine hours are associated with going to the beach. The exact splits are learned from the training data; they are not hand-written rules.

The dataset contains 30 illustrative rows. The scripts reserve 20% of the rows for a test split and train on the remaining 80%. `main.py` also prints the accuracy measured on that test split. With such a small, simple dataset, this score is only an educational demonstration and should not be treated as a reliable real-world weather recommendation.

## Project files

```text
.
├── data/
│   └── exercicio_ml_praia.csv  # Training and test examples
├── main/
│   ├── main.py                 # Command-line prediction and test accuracy
│   └── interface.py            # Tkinter graphical interface
└── README.md
```

## Requirements

- Python 3.9 or newer
- pandas
- scikit-learn
- Tkinter (included with most standard Python installations; on some Linux distributions it is installed separately)

Install the Python packages with:

```bash
python -m pip install pandas scikit-learn
```

## Run the graphical interface

From the repository root, run:

```bash
python main/interface.py
```

Enter a temperature and the expected sunshine hours, then select **Ver resultado**. Decimal values may use either a dot or a comma. Pressing Enter also requests a prediction.

## Run the command-line program

From the repository root, run:

```bash
python main/main.py
```

The program asks for temperature and sunshine hours, prints the prediction, and reports test accuracy. Run it from the repository root so the relative path to the CSV resolves correctly.

## Dataset format

The CSV has three columns and no extra index column:

| Column | Meaning | Example |
| --- | --- | --- |
| `temperatura_c` | Temperature in Celsius | `26` |
| `horas_sol` | Sunshine hours | `5` |
| `vai_a_praia` | Target label (`Sim` or `Não`) | `Sim` |

To experiment, edit or extend the CSV while keeping these column names and label values consistent.

## Notes

- The graphical interface trains its own instance of the decision tree from the same CSV, so the original command-line script can remain unchanged.
- The decision tree has no fixed random seed, so training can produce different trees across runs in cases where the algorithm has tied choices.
- A model only learns from its examples. This tiny dataset does not account for rain, wind, sea conditions, location, or individual preferences.

---

# Árvore de Decisão para Ir à Praia

**Um pequeno projeto de aprendizado de máquina que prevê se vale a pena ir à praia com base na temperatura e nas horas de sol do dia.**

Este repositório é um exemplo educacional de um classificador de árvore de decisão feito em Python e scikit-learn. Ele inclui um programa de linha de comando, uma pequena base de dados CSV e uma interface gráfica para informar novas condições do tempo.

## O que o projeto faz

O modelo usa duas variáveis de entrada:

- `temperatura_c`: temperatura em graus Celsius.
- `horas_sol`: quantidade de horas de sol.

Ele prevê o alvo `vai_a_praia`, cujos valores são `Sim` e `Não`. O modelo aprende padrões a partir dos exemplos de `data/exercicio_ml_praia.csv` e aplica esses padrões a um novo par de valores.

O classificador é uma **árvore de decisão**. Durante o treinamento, ele aprende uma sequência de divisões baseada nas variáveis de entrada para separar exemplos com rótulos diferentes. Por exemplo, pode aprender que certas combinações de temperatura e horas de sol estão associadas a ir à praia. As divisões exatas são aprendidas a partir dos dados de treinamento; elas não são regras escritas manualmente.

A base de dados contém 30 linhas ilustrativas. Os programas reservam 20% das linhas para um conjunto de teste e treinam com os 80% restantes. O `main.py` também mostra a acurácia medida nesse conjunto de teste. Como a base é pequena e simples, essa métrica serve apenas como demonstração educacional e não deve ser considerada uma recomendação meteorológica confiável para situações reais.

## Arquivos do projeto

```text
.
├── data/
│   └── exercicio_ml_praia.csv  # Exemplos para treinamento e teste
├── main/
│   ├── main.py                 # Previsão no terminal e acurácia de teste
│   └── interface.py            # Interface gráfica com Tkinter
└── README.md
```

## Requisitos

- Python 3.9 ou mais recente
- pandas
- scikit-learn
- Tkinter (incluído na maioria das instalações padrão do Python; em algumas distribuições Linux, pode ser necessário instalá-lo separadamente)

Instale os pacotes Python com:

```bash
python -m pip install pandas scikit-learn
```

## Abrir a interface gráfica

Na pasta raiz do repositório, execute:

```bash
python main/interface.py
```

Informe a temperatura e as horas de sol previstas e clique em **Ver resultado**. Valores decimais podem usar ponto ou vírgula. Pressionar Enter também solicita uma previsão.

## Executar o programa no terminal

Na pasta raiz do repositório, execute:

```bash
python main/main.py
```

O programa solicita a temperatura e as horas de sol, imprime a previsão e mostra a acurácia no conjunto de teste. Execute-o a partir da pasta raiz para que o caminho relativo até o CSV seja encontrado.

## Formato da base de dados

O CSV tem três colunas e não possui uma coluna extra de índice:

| Coluna | Significado | Exemplo |
| --- | --- | --- |
| `temperatura_c` | Temperatura em Celsius | `26` |
| `horas_sol` | Horas de sol | `5` |
| `vai_a_praia` | Rótulo alvo (`Sim` ou `Não`) | `Sim` |

Para experimentar, edite ou amplie o CSV mantendo esses nomes de coluna e valores dos rótulos consistentes.

## Observações

- A interface gráfica treina sua própria instância da árvore de decisão usando o mesmo CSV, permitindo manter o script original de terminal intacto.
- A árvore não usa uma semente aleatória fixa; em situações de empate entre escolhas, o resultado do treinamento pode variar entre execuções.
- O modelo só aprende com os exemplos disponíveis. Esta base pequena não considera chuva, vento, condições do mar, localização ou preferências individuais.
