pre_req(calculo2, calculo1).
pre_req(calculo3, calculo2).
pre_req(estrutura_dados, programacao1).
pre_req(ia, estrutura_dados).

pode_cursar(Disciplina, Cursadas) :-
    findall(Pre, pre_req(Disciplina, Pre), Pres),
    subset(Pres, Cursadas).

faltam_pre_requisitos(Disciplina, Cursadas, Faltantes) :-
    findall(Pre, pre_req(Disciplina, Pre), Pres),
    subtract(Pres, Cursadas, Faltantes).

subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).

% NOVO: lista todas que pode cursar
todas_podem(Cursadas, Possiveis) :-
    findall(D,
        (pre_req(D, _); \+ pre_req(D, _)), % pega todas disciplinas
        Todas),
    list_to_set(Todas, Unicas),
    findall(D2,
        (member(D2, Unicas), pode_cursar(D2, Cursadas)),
        Possiveis).
