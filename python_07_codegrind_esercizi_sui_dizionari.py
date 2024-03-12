# esercizio 1
mio_dizionario = {}
print(mio_dizionario)
# esercizio 2
persona = {"nome":"Mario", "cognome":"Rossi", "età": 30}
print(persona)
# esercizio 3
eta = persona["età"]
print(eta)
# esercizio 4
persona["email"] = "mario.rossi@email.com"
print(persona)
# esercizio 5
del persona["cognome"]
print(persona)
# esercizio 6
chiavi = list(persona.keys())
print(chiavi)
# esercizio 7
valori = list(persona.values())
print(valori)
# esercizio 8
persona["età"] = 35
print(persona["età"])
# esercizio 9
num_elementi = len(persona)
print(num_elementi)