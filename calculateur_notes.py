from pathlib import Path
def saisir_note(message):
    while True:
        try:
            note = float(input(message))
            if 0 <= note <= 20:
                return note
            print("Erreur : la note doit etre entre 0 et 20.")
        except ValueError:
            print("Erreur : entrez un nombre.")
    
nom = input("Entrez le nom de l'etudiant : ")
nombre_notes = int(input("Combien de notes ? "))

notes = []
for compteur in range(1, nombre_notes + 1):
    message = f"Entrez la note {compteur} sur 20 : "
    notes.append(saisir_note(message))
moyenne = sum(notes) / len(notes)
print("Etudiant :", nom)
print("Moyenne :", round(moyenne, 2))

if moyenne >= 10:
    decision = "Admis"
else:
    decision = "A revoir"

print("Decision :", decision)
with open("resultats.txt", "a", encoding="utf-8") as fichier:
    fichier.write(f"Etudiant : {nom}\n")
    fichier.write(f"Moyenne : {round(moyenne, 2)}\n")
    fichier.write(f"Decision : {decision}\n\n")
chemin_rapport = Path(__file__).with_name("resultats.txt")
with open(chemin_rapport, "a", encoding="utf-8") as fichier:
