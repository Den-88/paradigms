% Rules
sum_list([], 0).
sum_list([Head | Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.

% Пример запроса и ответ:
% sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Result).
% Result = 55
