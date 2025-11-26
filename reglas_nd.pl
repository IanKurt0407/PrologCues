% reglas_nd.pl

% --- DEFINICIÓN DE REGLAS ---

% Regla para contar indicadores activos
% findall crea una lista con todos los indicadores que Python haya inyectado
cuenta_indicadores(Cantidad) :-
    findall(X, indicador(X), Lista),
    length(Lista, Cantidad).

% --- REGLAS DE DIAGNÓSTICO (Umbrales) ---

% Si tiene 4 o más indicadores, se considera posible neurodivergencia
resultado(posible_neurodivergente) :-
    cuenta_indicadores(N),
    N >= 4.

% Si tiene menos de 4, se considera posible neurotipicidad
resultado(posible_neurotipico) :-
    cuenta_indicadores(N),
    N < 4.

