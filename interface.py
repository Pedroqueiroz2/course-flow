import customtkinter as ctk
from pyswip import Prolog
import unicodedata

prolog = Prolog()
prolog.consult("regras.pl")

disciplinas = {
    "calculo1": "Cálculo 1",
    "calculo2": "Cálculo 2",
    "calculo3": "Cálculo 3",
    "programacao1": "Programação 1",
    "estrutura_dados": "Estrutura de Dados",
    "ia": "Inteligência Artificial"
}

mapa_inverso = {v: k for k, v in disciplinas.items()}

def normalizar(texto):
    texto = texto.lower()

    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    texto = texto.replace(" ", "")
    return texto


def encontrar_materia(texto):
    texto_norm = normalizar(texto)

    for chave in disciplinas:
        if texto_norm == chave:
            return chave

    return None

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

for chave, nome in disciplinas.items():
    var = ctk.BooleanVar()
    cb = ctk.CTkCheckBox(tab_cursadas, text=nome, variable=var)
    cb.pack(anchor="w", padx=10)
    checkboxes[chave] = var


def get_cursadas():
    return [d for d, var in checkboxes.items() if var.get()]

combo = ctk.CTkComboBox(tab_verificar, values=list(disciplinas.values()))
combo.set("")
combo.pack(pady=10)

label_resultado = ctk.CTkLabel(tab_verificar, text="")
label_resultado.pack(pady=10)


def verificar():
    materia_input = combo.get()

    # tenta converter direto
    if materia_input in mapa_inverso:
        materia = mapa_inverso[materia_input]
    else:
        materia = encontrar_materia(materia_input)

    if not materia:
        label_resultado.configure(text="Matéria inválida")
        return

    cursadas = get_cursadas()
    lista = "[" + ",".join(cursadas) + "]"

    try:
        query = f"pode_cursar({materia}, {lista})"
        resultado = list(prolog.query(query))

        if resultado:
            label_resultado.configure(text="Pode cursar")
        else:
            query_falta = f"faltam_pre_requisitos({materia}, {lista}, F)"
            resultado_falta = list(prolog.query(query_falta))

            if resultado_falta:
                faltantes = resultado_falta[0]["F"]

                faltantes = [
                    disciplinas.get(f, f) for f in faltantes
                ]

                label_resultado.configure(
                    text="Não pode cursar\nFaltam:\n" + "\n".join(faltantes))
            else:
                label_resultado.configure(text="Não pode cursar")

    except Exception as e:
        label_resultado.configure(text=f"Erro: {str(e)}")


btn = ctk.CTkButton(tab_verificar, text="Verificar", command=verificar)
btn.pack(pady=10)

label_sugestoes = ctk.CTkLabel(tab_sugestoes, text="Disciplinas disponíveis:")
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

            possiveis = [p for p in possiveis if p not in cursadas]

            if possiveis:
                possiveis_cadeiras = [
                    disciplinas.get(p, p) for p in possiveis
                ]

                resultado_sugestoes.configure(
                    text="\n".join(possiveis_cadeiras)
                )
            else:
                resultado_sugestoes.configure(text="Nada disponível")
        else:
            resultado_sugestoes.configure(text="Nada encontrado")

    except Exception as e:
        resultado_sugestoes.configure(text=f"Erro: {str(e)}")


btn_sugerir = ctk.CTkButton(tab_sugestoes, text="Ver sugestões", command=sugerir)
btn_sugerir.pack(pady=10)

app.mainloop()