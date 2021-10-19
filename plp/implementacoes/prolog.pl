% Verifica se o parâmetro Busca existe numa lista de listas, retornando true ou false.
ehMember(_, [], false).
ehMember(Busca, [H|T], R):-
    (member(Busca, H) -> R = true ; ehMember(Busca, T, R)
    ).

%  Gera a lista que queremos excluir da lista de lista passada como parâmetro.
%  Exemplo: removegg(111, [[333, Nome, Placa], [111, Nome, Placa]]) -> [111, Nome, Placa]
removegg(_, [], []).
removegg(Cpf, [H|T], C):- (member(Cpf, H) -> C = H; removegg(Cpf, T, C)).

remove(X, [X|T], T).
remove(X, [H|T], [H|T1]):- remove(X,T,T1).

%  Escreve no arquivo csv.
% Por exemplo, nesse caso vai escrever o CPF, Nome e Placa que são os parâmetros, mas você pode botar mudar.
escreverArquivo(Cpf, Nome, Placa):-
    open('nomeArquivo.csv', append, Fluxo),
    writeln(Fluxo, (Cpf, Nome, Placa)),
    close(Fluxo).

%  Retorna o maior elemento de uma lista.
maior_lista([R],R).
maior_lista([C|L],R) :- maior_lista(L,A), (A > C -> R = A; R = C).

%  Corta uma lista a partir do índice passado como parâmetro.
geraL(_, 11, []).
geraL(L, I, [H|T]):- 
    nth0(I, L, El),
    H = El,
    NewI is I+1,
    geraL(L, NewI, T).

%  Retorna o índice do maior elemento passado como parâmetro.
pegaIndice(L, I, Maior, R):-
    nth0(I, L, P),
    (Maior =:= P -> R = I, !; NewI is I+1, pegaIndice(L, NewI, Maior, R)).
