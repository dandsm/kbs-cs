# Explicación del código

## Importar librerías necesarias

from pyswip import Prolog
from pyDatalog import pyDatalog
import timeit

## Configuración inicial para Prolog

prolog = Prolog()
prolog.consult("knowledge_base.pl")

## Definición de reglas en Prolog

% Regla: una enfermedad es posible si, para TODO síntoma de la enfermedad, el paciente lo presenta
posible*enfermedad(Paciente, Enfermedad) :-
% Aseguramos que la enfermedad existe
sintoma(Enfermedad, *),
forall(
sintoma(Enfermedad, Sintoma),
sintomas_paciente(Paciente,Sintoma)
).

## Función para consultar Prolog

def prolog_query(paciente):
resultados = list(prolog.query(f"posible_enfermedad({paciente}, Enfermedad)"))
enfermedades = {resultado["Enfermedad"] for resultado in resultados}
return enfermedades

## Configuración inicial para PyDatalog

pyDatalog.clear()
pyDatalog.create_terms(
'sintoma',  
 'sintomas_paciente',
'sintima_ausente',
'posible_enfermedad',
'P', 'E', 'S', 'X'
)

## Definición de reglas en PyDatalog

sintima_ausente(P, E) <= (
sintoma(E, S)
& ~sintomas_paciente(P, S)
)

posible_enfermedad(P, E) <= (
sintoma(E, S)
& ~sintima_ausente(P, E)
)

## Función para consultar PyDatalog

def pydatalog_query(patient):
query = posible_enfermedad(patient, E)
return set(result[0] for result in query)

## Validación inicial: Demostrar que ambas consultas generan los mismos resultados antes del benchmark

def compare_queries(patient):
pydatalog_results = pydatalog_query(patient)
prolog_results = prolog_query(patient)

    print(f"\n=== Resultados para {patient} ===")
    print(f"PyDatalog => {pydatalog_results}")
    print(f"Prolog    => {prolog_results}")

    if pydatalog_results == prolog_results:
        print("-> Resultados coinciden.")
    else:
        only_in_py = pydatalog_results - prolog_results
        only_in_pl = prolog_results - pydatalog_results

        if only_in_py:
            print(f"-> Sólo en PyDatalog: {only_in_py}")
        if only_in_pl:
            print(f"-> Sólo in Prolog:    {only_in_pl}")

## Comprobar que ambas implementaciones coincidan

compare_queries('juan')
compare_queries('rodrigo_chaves')

## Benchmarking: evaluar desempeño de ambas implementaciones

print("Test de performance (10000 ejecuciones para cada uno):")

prolog_time = timeit.timeit(lambda: prolog_query('juan'), number=10000)
print(f"Prolog via PySWIP - Tiempo de ejecución: {prolog_time:.4f} segundos")

pydatalog_time = timeit.timeit(lambda: pydatalog_query('juan'), number=10000)
print(f"PyDatalog - Tiempo de ejecución: {pydatalog_time:.4f} segundos")

## Base de conocimiento en Datalog

# Hechos: síntomas asociados a enfermedades

- sintoma('gripe', 'fiebre')
- sintoma('gripe', 'dolor_cabeza')
- sintoma('gripe', 'dolor_garganta')
- sintoma('gripe', 'congestion_nasal')

- sintoma('resfriado', 'congestion_nasal')
- sintoma('resfriado', 'estornudos')
- sintoma('resfriado', 'dolor_garganta')

- sintoma('covid', 'fiebre')
- sintoma('covid', 'tos_seca')
- sintoma('covid', 'perdida_olfato')
- sintoma('covid', 'dificultad_respirar')

- sintoma('alergia', 'estornudos')
- sintoma('alergia', 'ojos_llorosos')
- sintoma('alergia', 'congestion_nasal')

# Hechos: síntomas que presenta cada paciente

- sintomas_paciente('maria', 'fiebre')
- sintomas_paciente('maria', 'tos_seca')
- sintomas_paciente('maria', 'perdida_olfato')

- sintomas_paciente('juan', 'congestion_nasal')
- sintomas_paciente('juan', 'estornudos')
- sintomas_paciente('juan', 'dolor_garganta')

- sintomas_paciente('luisa', 'estornudos')
- sintomas_paciente('luisa', 'ojos_llorosos')
- sintomas_paciente('luisa', 'congestion_nasal')

- sintomas_paciente('rodrigo_chaves', 'fiebre')
- sintomas_paciente('rodrigo_chaves', 'tos_seca')
- sintomas_paciente('rodrigo_chaves', 'perdida_olfato')
- sintomas_paciente('rodrigo_chaves', 'dificultad_respirar')

## Base de conocimiento en Prolog

% Hechos: síntomas asociados a enfermedades
sintoma(gripe, fiebre).
sintoma(gripe, dolor_cabeza).
sintoma(gripe, dolor_garganta).
sintoma(gripe, congestion_nasal).

sintoma(resfriado, congestion_nasal).
sintoma(resfriado, estornudos).
sintoma(resfriado, dolor_garganta).

sintoma(covid, fiebre).
sintoma(covid, tos_seca).
sintoma(covid, perdida_olfato).
sintoma(covid, dificultad_respirar).

sintoma(alergia, estornudos).
sintoma(alergia, ojos_llorosos).
sintoma(alergia, congestion_nasal).

% Hechos: síntomas que presenta cada paciente
sintomas_paciente(maria, fiebre).
sintomas_paciente(maria, tos_seca).
sintomas_paciente(maria, perdida_olfato).

sintomas_paciente(juan, congestion_nasal).
sintomas_paciente(juan, estornudos).
sintomas_paciente(juan, dolor_garganta).

sintomas_paciente(luisa, estornudos).
sintomas_paciente(luisa, ojos_llorosos).
sintomas_paciente(luisa, congestion_nasal).

sintomas_paciente(rodrigo_chaves, fiebre).
sintomas_paciente(rodrigo_chaves, tos_seca).
sintomas_paciente(rodrigo_chaves, perdida_olfato).
sintomas_paciente(rodrigo_chaves, dificultad_respirar).
