import customtkinter as ctk
from pyswip import Prolog

prolog = Prolog()
prolog.consult("regras.pl")

disciplinas = [
    "calculo1",
    "calculo2",
    "calculo3",
    "programacao1",
    "estrutura_dados",
    "ia"
]

app = ctk.CTk()
app.geometry("400x300")
app.title("Sistema de Disciplinas")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tab_verificar = tabview.add("Verificar")
tab_cursadas = tabview.add("Cursadas")

checkboxes = {}

label_cursadas = ctk.CTkLabel(tab_cursadas, text="Selecione as matérias cursadas:")
label_cursadas.pack(pady=5)

for d in disciplinas:
    var = ctk.BooleanVar()
    cb = ctk.CTkCheckBox(tab_cursadas, text=d, variable=var)
    cb.pack(anchor="w", padx=10)
    checkboxes[d] = var


entry_materia = ctk.CTkEntry(tab_verificar, placeholder_text="Matéria desejada")
entry_materia.pack(pady=10)

label_resultado = ctk.CTkLabel(tab_verificar, text="")
label_resultado.pack(pady=10)

def verificar():
    materia = entry_materia.get().lower()

    cursadas = [d for d, var in checkboxes.items() if var.get()]

    lista = "[" + ",".join(cursadas) + "]"
    query = f"pode_cursar({materia}, {lista})"

    try:
        resultado = list(prolog.query(query))

        if resultado:
            label_resultado.configure(text="✅ Pode cursar")
        else:
            label_resultado.configure(text="❌ Não pode cursar")

    except Exception as e:
        label_resultado.configure(text="Erro na consulta")

btn = ctk.CTkButton(tab_verificar, text="Verificar", command=verificar)
btn.pack(pady=10)

app.mainloop()