sum(0,0).
sum(N,Total):-
    N>0,
    N1 is N-1,
    sum(N1,Temp),
    Total is Temp+N.

