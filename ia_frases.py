import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. CARREGAR OS DADOS
dados = pd.read_csv("comentarios.csv")
print(dados.head())

# 2. SEPARAR ENTRADA E RESPOSTA
X = dados["frase"]
y = dados["classificacao"]

# 3. SEPARAR DADOS DE TREINAMENTO E TESTE
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. TRANSFORMAR TEXTO EM NÚMEROS
vetorizador = TfidfVectorizer()
X_treino_numerico = vetorizador.fit_transform(X_treino)
X_teste_numerico = vetorizador.transform(X_teste)

# 5. CRIAR O MODELO
modelo = LogisticRegression()

# 6. TREINAR A IA
modelo.fit(X_treino_numerico, y_treino)

# 7. TESTAR O MODELO
previsoes = modelo.predict(X_teste_numerico)
acuracia = accuracy_score(y_teste, previsoes)
print("Acurácia:", acuracia)

# 8. TESTAR UMA FRASE NOVA
frase = ["Eu adorei essa aula!"]
frase_numerica = vetorizador.transform(frase)
resultado = modelo.predict(frase_numerica)
print("Frase:", frase[0])
print("Classificação:", resultado[0])