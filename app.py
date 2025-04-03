from pyswip import Prolog
from pyDatalog import pyDatalog
import timeit

# ----- Prolog Setup -----
prolog = Prolog()
prolog.consult("knowledge_base.pl")

def prolog_query(patient):
    results = list(prolog.query(f"posible_enfermedad({patient}, Enfermedad)"))
    unique = {result["Enfermedad"] for result in results}
    return unique

# ----- PyDatalog Setup -----
pyDatalog.create_terms(
    'sintoma',           
    'sintomas_paciente',
    'sintima_ausente',
    'posible_enfermedad',
    'P', 'E', 'S', 'X'
)

# Hechos: síntomas asociados a enfermedades
+ sintoma('gripe', 'fiebre')
+ sintoma('gripe', 'dolor_cabeza')
+ sintoma('gripe', 'dolor_garganta')
+ sintoma('gripe', 'congestion_nasal')

+ sintoma('resfriado', 'congestion_nasal')
+ sintoma('resfriado', 'estornudos')
+ sintoma('resfriado', 'dolor_garganta')

+ sintoma('covid', 'fiebre')
+ sintoma('covid', 'tos_seca')
+ sintoma('covid', 'perdida_olfato')
+ sintoma('covid', 'dificultad_respirar')

+ sintoma('alergia', 'estornudos')
+ sintoma('alergia', 'ojos_llorosos')
+ sintoma('alergia', 'congestion_nasal')

# Hechos: síntomas que presenta cada paciente
+ sintomas_paciente('maria', 'fiebre')
+ sintomas_paciente('maria', 'tos_seca')
+ sintomas_paciente('maria', 'perdida_olfato')

+ sintomas_paciente('juan', 'congestion_nasal')
+ sintomas_paciente('juan', 'estornudos')
+ sintomas_paciente('juan', 'dolor_garganta')

+ sintomas_paciente('luisa', 'estornudos')
+ sintomas_paciente('luisa', 'ojos_llorosos')
+ sintomas_paciente('luisa', 'congestion_nasal')

+ sintomas_paciente('rodrigo_chaves', 'fiebre')
+ sintomas_paciente('rodrigo_chaves', 'tos_seca')
+ sintomas_paciente('rodrigo_chaves', 'perdida_olfato')
+ sintomas_paciente('rodrigo_chaves', 'dificultad_respirar')

sintima_ausente(P, E) <= (
    sintoma(E, S) 
    & ~sintomas_paciente(P, S)
)

posible_enfermedad(P, E) <= (
    sintoma(E, S)
    & ~sintima_ausente(P, E)
)

def pydatalog_query(patient):
    query = posible_enfermedad(patient, E)
    return set(result[0] for result in query)

# ----- Testing -----
def compare_queries(patient):
    # 1) Get the set of diseases returned by PyDatalog
    pydatalog_results = pydatalog_query(patient)
    # 2) Get the set of diseases returned by Prolog
    prolog_results = prolog_query(patient)
    
    # 3) Print them out in a more descriptive way
    print(f"\n=== Resultados para {patient} ===")
    print(f"PyDatalog => {pydatalog_results}")
    print(f"Prolog    => {prolog_results}")
    
    # 4) Check for differences
    if pydatalog_results == prolog_results:
        print("-> Resultados coinciden.")
    else:
        # Diseases found only by PyDatalog
        only_in_py = pydatalog_results - prolog_results
        # Diseases found only by Prolog
        only_in_pl = prolog_results - pydatalog_results
        
        if only_in_py:
            print(f"-> Sólo en PyDatalog: {only_in_py}")
        if only_in_pl:
            print(f"-> Sólo in Prolog:    {only_in_pl}")

compare_queries('juan')
compare_queries('rodrigo_chaves')

# ----- Benchmarking -----
print("Test de performance (10000 ejecuciones para cada uno):")

prolog_time = timeit.timeit(lambda: prolog_query('juan'), number=10000)
print(f"Prolog via PySWIP - Tiempo de ejecución: {prolog_time:.4f} segundos")

pydatalog_time = timeit.timeit(lambda: pydatalog_query('juan'), number=10000)
print(f"PyDatalog - Tiempo de ejecución: {pydatalog_time:.4f} segundos")
