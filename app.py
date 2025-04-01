from pyswip import Prolog

prolog = Prolog()
# Load Prolog facts/rules from a local file
prolog.consult("knowledge_base.pl")


results = list(prolog.query("posible_enfermedad(juan, Enfermedad)"))
unique = {result["Enfermedad"] for result in results}
print("Enfermedades posibles para Juan:")
for enfermedad in unique:
    print(enfermedad)
