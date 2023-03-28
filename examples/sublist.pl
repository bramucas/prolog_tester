%Marcelo Ferreiro Sánchez
%Ainhoa de Diego Silva

%Enunciado 1
sublist(S, L) :- append(_H, T, L), append(S, _, T).

%Enunciado 3
del(X, L1, L2) :-
    append(Principio, [X|Final], L1),
    append(Principio, Final, L2).
%Enunciado 5
flatten([], []).
flatten([P|F], L2) :-
    flatten(P, F2),   % recursively flatten X
    flatten(F, F3), % recursively flatten the rest of the list
    append(F2, F3, L2). % concatenate the flattened X and the flattened rest of the list to form L2
flatten(P, [P]).     % if X is not a list, append it to the output list

%Enunciado 4
delete(X, L1, L2) :-
    append(Principio, [X|Final], L1),
    append(Principio, Final, L2).
insert(X, L1, L2) :-
    append(Principio, Final, L1),
    append(Principio, [X|Final], L2).


perm(L1,L2):- insert(X,L1,T), delete(X,T,L2), not(L2 = L1).
% %Enunciado 2.
% insert(X, L1, L2) :-
%     append(principio, final, L1),
%     append(principio, [X|final], L2).
