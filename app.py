from pyswip import Prolog

prolog = Prolog()
# Load Prolog facts/rules from a local file
prolog.consult("knowledge_base.pl")


results = list(prolog.query("parent(X, Y)"))
print("Results from Prolog:", results)