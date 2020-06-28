print("\n\nThis program works using moles or using grams. If using grams, replace Coefficient with the atomic weights of the molecules and the ammound of grams.")

src = float(input("CoEfficient of Molecule With Known Ammount: "))
dest = float(input("CoEfficient of Molecule to find: "))
ConversionFactor = float(input("Given Ammount: "))

destAmmount = str((dest/src) * ConversionFactor)

print("Ammount Found = ", destAmmount)
