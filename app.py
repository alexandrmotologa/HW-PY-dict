# definim un dicționar cu denumirile disciplinelor și notele corespunzătoare
grades = {
    "English": 8,
    "Math": 9,
    "Anatomy": 7,
}

# calculăm lungimea maximă a unei denumiri de disciplină utilizând funcția max()
# și o listă comprehensivă care extrage lungimea fiecărei denumiri de disciplină din dicționar
max_length = max([len(discipline) for discipline in grades])

# iterăm peste fiecare pereche cheie-valoare din dicționarul de note
# utilizând metoda items(), care ne permite să obținem simultan cheile și valorile
# păstrăm cheia în variabila "discipline" și valoarea în variabila "grade"
for discipline, grade in grades.items():
    print("{:{}}: {}".format(discipline, max_length, grade))