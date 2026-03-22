import customtkinter as ctk
from pyswip import Prolog
import unicodedata

prolog = Prolog()
prolog.consult("regras.pl")

disciplinas_por_periodo = {
    1: {
        "calculo_diferencial_e_integral_1": "Cálculo Diferencial e Integral 1",
        "calculo_vetorial_e_geometria_analitica": "Cálculo Vetorial e Geometria Analítica",
        "matematica_discreta": "Matemática Discreta",
        "introducao_a_ciencia_da_computacao": "Introdução à Ciência da Computação",
        "introducao_a_programacao": "Introdução à Programação",
        "metodologia_do_trabalho_cientifico_para_ciencia_da_computacao": "Metodologia do Trab. Científico",
        "pesquisa_aplicada_a_ciencia_da_computacao": "Pesquisa Aplicada à Ciência da Computação"
    },
    2: {
        "calculo_diferencial_e_integral_2": "Cálculo Diferencial e Integral 2",
        "introducao_a_algebra_linear": "Introdução à Álgebra Linear",
        "logica_aplicada_a_computacao": "Lógica Aplicada à Computação",
        "arquitetura_de_computadores_1": "Arquitetura de Computadores 1",
        "programacao_orientada_a_objetos": "Programação Orientada a Objetos"
    },
    3: {
        "calculo_numerico": "Cálculo Numérico",
        "calculo_das_probabilidades_e_estatistica_1": "Cálculo das Probab. e Estatística I",
        "linguagens_formais_e_computabilidade": "Linguagens Formais e Computabilidade",
        "arquitetura_de_computadores_2": "Arquitetura de Computadores 2",
        "estruturas_de_dados_e_algoritmos_1": "Estruturas de Dados e Algoritmos 1",
        "programacao_funcional": "Programação Funcional"
    },
    4: {
        "introducao_a_inteligencia_artificial": "Introdução à Inteligência Artificial",
        "redes_de_computadores_1": "Redes de Computadores 1",
        "introducao_ao_processamento_digital_de_imagens": "Introd. ao Proc. Digital de Imagens",
        "sistemas_operacionais_1": "Sistemas Operacionais 1",
        "estruturas_de_dados_e_algoritmos_2": "Estruturas de Dados e Algoritmos 2",
        "engenharia_de_software": "Engenharia de Software"
    },
    5: {
        "sistemas_baseados_em_conhecimento": "Sistemas Baseados em Conhecimento",
        "analise_e_projeto_de_algoritmos": "Análise e Projeto de Algoritmos",
        "paradigmas_de_linguagens_de_programacao": "Paradigmas de Ling. de Programação",
        "programacao_concorrente_e_distribuida": "Prog. Concorrente e Distribuída",
        "banco_de_dados_1": "Banco de Dados 1",
        "especificacao_de_requisitos_de_software": "Especificação de Requisitos de Software"
    },
    6: {
        "paradigmas_de_aprendizagem_de_maquina": "Paradigmas de Aprend. de Máquina",
        "seguranca_computacional": "Segurança Computacional",
        "construcao_de_compiladores_1": "Construção de Compiladores 1",
        "sistemas_distribuidos": "Sistemas Distribuídos",
        "inovacao_de_base_cientifica_tecnologica_e_empreendedorismo": "Inovação e Empreendedorismo",
        "metodos_de_projeto_de_software": "Métodos de Projeto de Software"
    },
    7: {
        "sistemas_de_informacao_nas_organizacoes": "Sist. de Informação nas Organizações",
        "interacao_humano_computador": "Interação Humano-Computador",
        "engenharia_de_sistemas_distribuidos": "Engenharia de Sistemas Distribuídos",
        "gerenciamento_de_projeto_de_software": "Gerenciamento de Projeto de Software",
        "teste_de_software": "Teste de Software"
    },
    8: {
        "computadores_e_sociedade": "Computadores e Sociedade",
        "estagio_supervisionado": "Estágio Supervisionado"
    }
}

disciplinas = {}
for per in disciplinas_por_periodo.values():
    disciplinas.update(per)

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
app.geometry("1400x700")
app.title("Courser Flow")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tab_verificar = tabview.add("Verificar")
tab_cursadas = tabview.add("Cursadas")
tab_sugestoes = tabview.add("Sugestões")

checkboxes = {}

label_cursadas = ctk.CTkLabel(tab_cursadas, text="Selecione as matérias cursadas:", font=("Arial", 16, "bold"))
label_cursadas.pack(pady=10)

frame_colunas = ctk.CTkScrollableFrame(tab_cursadas, orientation="horizontal")
frame_colunas.pack(fill="both", expand=True, padx=10, pady=10)

for p, (periodo, disc_periodo) in enumerate(disciplinas_por_periodo.items()):
    col_frame = ctk.CTkFrame(frame_colunas, fg_color="transparent")
    col_frame.grid(row=0, column=p, sticky="n", padx=10, pady=5)
    
    lbl_periodo = ctk.CTkLabel(col_frame, text=f"{periodo}º Período", font=("Arial", 14, "bold"))
    lbl_periodo.pack(pady=10)
    
    for chave, nome in disc_periodo.items():
        var = ctk.BooleanVar()
        cb = ctk.CTkCheckBox(col_frame, text=nome, variable=var, font=("Arial", 12))
        cb.pack(anchor="w", padx=5, pady=5)
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