#Necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Importing the dataset
df = pd.read_csv('data/exercicio_ml_praia.csv')


# Separating the variables, X will be the features and Y will be the target
x = df[['temperatura_c','horas_sol']]
y = df['vai_a_praia']


#Separating the data into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
#print(f"Dados de treino: {len(x_train)}")
#print(f"Dados de teste: {len(x_test)}")

# Creating the model
model = DecisionTreeClassifier()
model.fit(x_train,y_train)

# Making the predictions with test data
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)

# Making the predictions with custom data
custom_temperature = float(input("Digite a temperatura em °C: "))
custom_hours_sun = float(input("Digite quantas horas de sol haverá: "))
new_day = [[custom_temperature,custom_hours_sun]]
custom_prediction = model.predict(new_day)

print("Vai à praia? \n", custom_prediction[0])

accuracy = accuracy_score(y_test,y_pred)
print(f"Acurácia do modelo: {accuracy:.2%}")

# Generating a figure to understand how the decision tree classifies the result
'''plt.figure(figsize=(14, 8))
plot_tree(
    model,
    feature_names=['temperatura_c', 'horas_sol'],
    class_names=['Não', 'Sim'],
    filled=True,
    rounded=True
)
plt.show()'''
