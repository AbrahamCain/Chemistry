g = float(input("Grams: "))
m = float(input("Atomic Mass Unit: "))
Avogadro = (6.022 * (10**23))

atoms = ((g/m)*Avogadro)

print("Atoms = " + str(atoms))

