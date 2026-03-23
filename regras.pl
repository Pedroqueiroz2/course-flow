% DISCIPLINAS

disciplina(calculo_diferencial_e_integral_1).
disciplina(calculo_vetorial_e_geometria_analitica).
disciplina(matematica_discreta).
disciplina(introducao_a_ciencia_da_computacao).
disciplina(introducao_a_programacao).
disciplina(metodologia_do_trabalho_cientifico_para_ciencia_da_computacao).
disciplina(pesquisa_aplicada_a_ciencia_da_computacao).

disciplina(introducao_a_algebra_linear).
disciplina(calculo_diferencial_e_integral_2).
disciplina(logica_aplicada_a_computacao).
disciplina(arquitetura_de_computadores_1).
disciplina(programacao_orientada_a_objetos).

disciplina(calculo_numerico).
disciplina(calculo_das_probabilidades_e_estatistica_1).
disciplina(linguagens_formais_e_computabilidade).
disciplina(arquitetura_de_computadores_2).
disciplina(estruturas_de_dados_e_algoritmos_1).
disciplina(programacao_funcional).

disciplina(introducao_a_inteligencia_artificial).
disciplina(redes_de_computadores_1).
disciplina(introducao_ao_processamento_digital_de_imagens).
disciplina(sistemas_operacionais_1).
disciplina(estruturas_de_dados_e_algoritmos_2).
disciplina(engenharia_de_software).

disciplina(sistemas_baseados_em_conhecimento).
disciplina(analise_e_projeto_de_algoritmos).
disciplina(paradigmas_de_linguagens_de_programacao).
disciplina(programacao_concorrente_e_distribuida).
disciplina(banco_de_dados_1).
disciplina(especificacao_de_requisitos_de_software).

disciplina(paradigmas_de_aprendizagem_de_maquina).
disciplina(seguranca_computacional).
disciplina(construcao_de_compiladores_1).
disciplina(sistemas_distribuidos).
disciplina(inovacao_de_base_cientifica_tecnologica_e_empreendedorismo).
disciplina(metodos_de_projeto_de_software).

disciplina(sistemas_de_informacao_nas_organizacoes).
disciplina(interacao_humano_computador).
disciplina(engenharia_de_sistemas_distribuidos).
disciplina(gerenciamento_de_projeto_de_software).
disciplina(teste_de_software).

disciplina(computadores_e_sociedade).
disciplina(estagio_supervisionado).

% PRÉ-REQUISITOS 

% Básicos
pre_req(calculo_diferencial_e_integral_2, calculo_diferencial_e_integral_1).
pre_req(calculo_diferencial_e_integral_2, calculo_vetorial_e_geometria_analitica).

pre_req(introducao_a_algebra_linear, calculo_vetorial_e_geometria_analitica).

pre_req(programacao_orientada_a_objetos, introducao_a_programacao).

pre_req(logica_aplicada_a_computacao, matematica_discreta).

pre_req(arquitetura_de_computadores_1, introducao_a_ciencia_da_computacao).

% Intermediárias
pre_req(calculo_das_probabilidades_e_estatistica_1, calculo_diferencial_e_integral_2).

pre_req(arquitetura_de_computadores_2, arquitetura_de_computadores_1).

pre_req(calculo_numerico, calculo_diferencial_e_integral_2).
pre_req(calculo_numerico, programacao_orientada_a_objetos).

pre_req(programacao_funcional, introducao_a_programacao).

pre_req(estruturas_de_dados_e_algoritmos_1, programacao_orientada_a_objetos).

pre_req(linguagens_formais_e_computabilidade, logica_aplicada_a_computacao).

pre_req(sistemas_operacionais_1, programacao_orientada_a_objetos).
pre_req(sistemas_operacionais_1, arquitetura_de_computadores_1).

pre_req(introducao_a_inteligencia_artificial, logica_aplicada_a_computacao).
pre_req(introducao_a_inteligencia_artificial, estruturas_de_dados_e_algoritmos_1).

pre_req(estruturas_de_dados_e_algoritmos_2, estruturas_de_dados_e_algoritmos_1).

pre_req(introducao_ao_processamento_digital_de_imagens, calculo_das_probabilidades_e_estatistica_1).
pre_req(introducao_ao_processamento_digital_de_imagens, estruturas_de_dados_e_algoritmos_1).

pre_req(redes_de_computadores_1, programacao_orientada_a_objetos).

pre_req(engenharia_de_software, programacao_orientada_a_objetos).

% Avançadas
pre_req(analise_e_projeto_de_algoritmos, estruturas_de_dados_e_algoritmos_1).

pre_req(banco_de_dados_1, estruturas_de_dados_e_algoritmos_1).

pre_req(especificacao_de_requisitos_de_software, engenharia_de_software).

pre_req(paradigmas_de_linguagens_de_programacao, programacao_funcional).
pre_req(paradigmas_de_linguagens_de_programacao, linguagens_formais_e_computabilidade).

pre_req(sistemas_baseados_em_conhecimento, introducao_a_inteligencia_artificial).

pre_req(programacao_concorrente_e_distribuida, redes_de_computadores_1).
pre_req(programacao_concorrente_e_distribuida, sistemas_operacionais_1).

pre_req(metodos_de_projeto_de_software, engenharia_de_software).

pre_req(paradigmas_de_aprendizagem_de_maquina, introducao_a_inteligencia_artificial).
pre_req(paradigmas_de_aprendizagem_de_maquina, calculo_numerico).

pre_req(seguranca_computacional, redes_de_computadores_1).

pre_req(sistemas_distribuidos, programacao_concorrente_e_distribuida).

pre_req(construcao_de_compiladores_1, estruturas_de_dados_e_algoritmos_1).
pre_req(construcao_de_compiladores_1, linguagens_formais_e_computabilidade).

pre_req(gerenciamento_de_projeto_de_software, engenharia_de_software).

pre_req(engenharia_de_sistemas_distribuidos, sistemas_distribuidos).
pre_req(engenharia_de_sistemas_distribuidos, metodos_de_projeto_de_software).

pre_req(interacao_humano_computador, engenharia_de_software).

pre_req(teste_de_software, engenharia_de_software).

pre_req(estagio_supervisionado, engenharia_de_software).


% REGRAS

% Busca todos os pré-requisitos da disciplina.

pode_cursar(Disciplina, Cursadas) :-
    findall(Pre, pre_req(Disciplina, Pre), Pres),
    subset(Pres, Cursadas). %  Verifica se todos os pré-requisitos estão dentro da lista de cursadas

% Mostra quais pré-requisitos ainda faltam.

faltam_pre_requisitos(Disciplina, Cursadas, Faltantes) :-
    findall(Pre, pre_req(Disciplina, Pre), Pres),
    subtract(Pres, Cursadas, Faltantes).

% Verifica se uma lista está contida dentro de outra

subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).

% SUGESTÕES (Retorna todas as disciplinas que você já pode cursar)

todas_podem(Cursadas, Possiveis) :-
    findall(D,
        (disciplina(D), pode_cursar(D, Cursadas)),
        Possiveis).
