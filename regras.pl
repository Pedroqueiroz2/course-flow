pre_req(calculo2, calculo1).
pre_req(calculo3, calculo2).
pre_req(estrutura_dados, programacao1).
pre_req(ia, estrutura_dados).

pode_cursar(Disciplina, Cursadas) :-
    findall(Pre, pre_req(Disciplina, Pre), Pres),
    subset(Pres, Cursadas).

subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).