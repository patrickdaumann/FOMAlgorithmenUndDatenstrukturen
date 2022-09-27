from random import randint

"""
Pseudocode:

Insertion-Sort(A,n)
    for j = 2 to n
        key = A[j]
        //Insert A[j] into the sorted Sequence A[1 .. j .. -1]
        i = j - 1
        while i>0 and A[i]>key
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
"""

#Insert Sort Algorithmus
def InsertSort(A):
    '''Sortiert das angegebene Feld A mit dem Insert-Sort Algorithmus (destruktiv)'''
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i > -1 and A[i]>key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key


#Feld initialiseren
n = 10
feld = []

#Feld mit Zufallszahlen fuellen
for i in range(n):
    feld.append(randint(100, 999))

#Ausgabe des unsortierten Feldes
print(f"Unsortiert:\t {feld}")

#Sortieren des Feldes
InsertSort(feld)

#Ausgabe des sortierten Feldes
print(f"Sortiert:\t {feld}")