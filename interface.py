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
app.title("Courser Flow")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tab_verificar = tabview.add("Verificar")
tab_cursadas = tabview.add("Cursadas")
tab_sugestoes = tabview.add("Sugestões")

checkboxes = {}

label_cursadas = ctk.CTkLabel(tab_cursadas, text="Selecione as matérias cursadas:")
label_cursadas.pack(pady=5)

for d in disciplinas:
    var = ctk.BooleanVar()
    cb = ctk.CTkCheckBox(tab_cursadas, text=d, variable=var)
    cb.pack(anchor="w", padx=10)
    checkboxes[d] = var


combo = ctk.CTkComboBox(tab_verificar, values=disciplinas)
combo.set("Escolha a matéria")
combo.pack(pady=10)

label_resultado = ctk.CTkLabel(tab_verificar, text="")
label_resultado.pack(pady=10)


def get_cursadas():
    return [d for d, var in checkboxes.items() if var.get()]


def verificar():
    materia = combo.get()

    if materia not in disciplinas:
        label_resultado.configure(text="Selecione uma matéria válida")
        return

    cursadas = get_cursadas()
    lista = "[" + ",".join(cursadas) + "]"

    try:
        # verifica se pode
        query = f"pode_cursar({materia}, {lista})"
        resultado = list(prolog.query(query))

        if resultado:
            label_resultado.configure(text="✅ Pode cursar")
        else:
            # verifica o que falta
            query_falta = f"faltam_pre_requisitos({materia}, {lista}, F)"
            resultado_falta = list(prolog.query(query_falta))

            if resultado_falta:
                faltantes = resultado_falta[0]["F"]
                label_resultado.configure(
                    text=f"❌ Não pode cursar\nFaltam: {faltantes}"
                )
            else:
                label_resultado.configure(text="❌ Não pode cursar")

    except Exception as e:
        label_resultado.configure(text=f"Erro: {str(e)}")


btn = ctk.CTkButton(tab_verificar, text="Verificar", command=verificar)
btn.pack(pady=10)

label_sugestoes = ctk.CTkLabel(tab_sugestoes, text="Disciplinas que você pode cursar:")
label_sugestoes.pack(pady=10)

resultado_sugestoes = ctk.CTkLabel(tab_sugestoes, text="")
resultado_sugestoes.pack(pady=10)


def sugerir():
    cursadas = get_cursadas()
    lista = "[" + ",".join(cursadas) + "]"

    try:
        query = f"todas_podem({lista}, X)"
        resultado = list(prolog.query(query))

        if resultado:
            possiveis = resultado[0]["X"]

            # remove as já cursadas
            possiveis = [p for p in possiveis if p not in cursadas]

            if possiveis:
                resultado_sugestoes.configure(text="\n".join(possiveis))
            else:
                resultado_sugestoes.configure(text="Nada disponível")
        else:
            resultado_sugestoes.configure(text="Nada encontrado")

    except Exception as e:
        resultado_sugestoes.configure(text=f"Erro: {str(e)}")


btn_sugerir = ctk.CTkButton(tab_sugestoes, text="Ver sugestões", command=sugerir)
btn_sugerir.pack(pady=10)

app.mainloop()