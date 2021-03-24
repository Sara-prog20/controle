note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

#def moyenne(x,y):
 # return (x[2]+y[2])/2



#eleve1=note1+note2
#print(moyenne(note1,note2))



###c-Moyenne de l'eleve 1
def moyenne(liste):
  valeurs=0
  for i in range(len(liste)):
    valeurs=valeurs+liste[i][2]
    moyenne=valeurs/len(liste)
  return moyenne
notes_eleve1 = [note1, note2, note3, note4, note5, note6]
print("moyenne de eleve1",moyenne(notes_eleve1))

###b-moyenne de eleve1 en maths

notes_eleve1_math = [note1,note3, note6]
print("moyenne de eleve1 en math",moyenne(notes_eleve1_math))

## liste compréhension
def moyenne_comprehension(liste):
  liste=[]
  return [sum(liste[i][2])/len(liste) for liste[i] in liste]

print(moyenne_comprehension(notes_eleve1))

##c- Fonction qui calcule moyenne d'un élève dans une matière.
notes = [note1, note2, note3, note4, note5, note6,note7,note8]
def moyenne_tuples(notes,eleve,matiere):
  eleve=[note for note in notes if note[0]==eleve]
  print(eleve)
  matiere=[note for note in eleve if note[1]==matiere]
  print(matiere)
  notes=[note[2] for note in eleve and matiere]
  res=sum(notes)/len(notes)
  return res

print(moyenne_tuples(notes,"eleve1","math"))

##5-
notes_enregistrees = []
class Note:
  def __init__(self, eleve, matiere, valeur):
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self = notes_enregistrees.append(self)


  def afficher(self):
    print('eleve:', self.eleve, 'matière:', self.matiere, 'note:', self.valeur)
  
  def __str__(self):
    return f"eleve: {self.eleve} matière: {self.matiere} note: {self.valeur}"


onotes = []
for a in notes:
  onotes.append(Note(a[0],a[1],a[2]))


#6-
for x in range(len(onotes)) :
  print(onotes[x])

#7-
for x in range(len(notes_enregistrees)) :
  print(notes_enregistrees[x])


#8-
def moyenne_Notes(nom=None,matiere=None):
  liste = notes_enregistrees
  resultat = []
  liste_eleve=[]
  for a in liste :
    liste_eleve= [x for x in liste if x.eleve == nom or nom == None]
    liste_matiere= [x for x in liste_eleve if x.matiere == matiere or matiere == None]
    resultat = [x.valeur for x in liste_matiere ]
    moyenne = sum(resultat)/len(resultat)
  return moyenne

print(moyenne_Notes())