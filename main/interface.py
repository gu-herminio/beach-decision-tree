"""Interface gráfica para prever se o dia é adequado para ir à praia.

Execute com: python main/interface.py (a partir da pasta do projeto).
O código original em main.py permanece intacto.
"""

from pathlib import Path
import tkinter as tk
from tkinter import ttk

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Treina o mesmo tipo de modelo usando os mesmos dados e variáveis do main.py.
PROJECT_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(PROJECT_DIR / "data" / "exercicio_ml_praia.csv")
x = df[["temperatura_c", "horas_sol"]]
y = df["vai_a_praia"]
x_train, _x_test, y_train, _y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)


def prever():
    try:
        temperatura = float(temperatura_var.get().replace(",", "."))
        horas_sol = float(horas_var.get().replace(",", "."))
    except ValueError:
        resultado_var.set("Digite valores numéricos válidos.")
        return

    previsao = model.predict(pd.DataFrame(
        [[temperatura, horas_sol]],
        columns=["temperatura_c", "horas_sol"],
    ))[0]
    resposta = str(previsao).strip().lower()
    vai = resposta in {"sim", "s", "yes", "1", "true"}
    resultado_var.set("Sim, vai à praia! ☀️" if vai else "Não vai à praia. 🌧️")


root = tk.Tk()
root.title("Decisão da Praia")
root.resizable(False, False)
root.configure(padx=24, pady=20)

ttk.Label(root, text="Vamos à praia?", font=("Helvetica", 19, "bold")).grid(
    row=0, column=0, columnspan=2, sticky="w", pady=(0, 5)
)
ttk.Label(root, text="Informe a previsão para o dia:").grid(
    row=1, column=0, columnspan=2, sticky="w", pady=(0, 16)
)

temperatura_var = tk.StringVar()
horas_var = tk.StringVar()
resultado_var = tk.StringVar(value="Preencha os campos e clique em Ver resultado.")

ttk.Label(root, text="Temperatura (°C)").grid(row=2, column=0, sticky="w", pady=5)
temperatura_input = ttk.Entry(root, textvariable=temperatura_var, width=18)
temperatura_input.grid(row=2, column=1, sticky="ew", pady=5)

ttk.Label(root, text="Horas de sol").grid(row=3, column=0, sticky="w", pady=5)
horas_input = ttk.Entry(root, textvariable=horas_var, width=18)
horas_input.grid(row=3, column=1, sticky="ew", pady=5)

ttk.Button(root, text="Ver resultado", command=prever).grid(
    row=4, column=0, columnspan=2, sticky="ew", pady=(14, 12)
)
ttk.Label(root, textvariable=resultado_var, font=("Helvetica", 12, "bold")).grid(
    row=5, column=0, columnspan=2, sticky="w"
)

temperatura_input.focus()
root.bind("<Return>", lambda _event: prever())
root.mainloop()
