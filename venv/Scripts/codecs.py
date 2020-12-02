from main import titles,tags,descriptions,dates
entetes = [
     titles,
     tags,
     descriptions,
     dates
]

valeurs = [
     titles,
     tags,
     descriptions,
    dates
]

f = open('Data.csv', 'w')
ligneEntete = ";".join(entetes) + "\n"
f.write(ligneEntete)
for valeur in valeurs:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)

f.close()

#################""
f = open('Data.csv', 'w')
ligneEntete = ";".join(entetes)+ "\n"
f.write(ligneEntete)
for valeur in titles:
     column1 = "".join(titles)
     f.write(column1)
for valeur in tags:
     column2 = "".join(tags)
     f.write(column2)
for valeur in descriptions:
     column3 = "".join(descriptions)
     f.write(column3)
for valeur in dates:
    column4 = ",".join(dates)
    f.write(column4)

f.close()

#######################"

f = open('Data.csv', 'w')
ligneEntete = ";".join(entetes)+ "\n"
f.write(ligneEntete)
for valeur in titles:
     column1 = "".join(titles)
     f.write(column1)
f.write(";")
for valeur in tags:
     column2 = "".join(tags)
     f.write(column2)
f.write(";")
for valeur in descriptions:
     column3 = "".join(descriptions)
     f.write(column3)
f.write(";")
for valeur in dates:
    column4 = "".join(dates)
    f.write(column4)
f.close()