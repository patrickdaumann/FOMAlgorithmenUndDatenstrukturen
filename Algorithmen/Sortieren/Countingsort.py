from random import randint

def countingsort(arr):
    # Arbeitsvariable Eingabefeld
    E = arr
    
    # Counting Feld mit Nullen initialisieren
    C = [0 for x in range(max(arr)+1)]
    
    # Rueckgabefeld mit Nullen initialisieren
    R = [0 for x in range(len(arr))]

    # Vorkommnisse der einzelnen Werte im Eingabefeld zaehlen
    for i in range(len(arr)):
        C[E[i]] +=1
    print(f"C:\t{C}")

    # Kummulative Summe im Counting Feld bilden
    for i in range(1, max(arr)+1):
        C[i] += C[i-1]
    print(f"C:\t{C}")

    # Sortiertes Ausgabefeld erstellen
    for i in range(len(arr)-1, -1, -1):
        R[C[E[i]]-1] = E[i]
        C[E[i]]-=1
    print(f"C:\t{C}")
    # Ausgabe des sortierten Feldes
    return R



############################################
# Testcode

length = 6
arr = [randint(0, 5) for x in range(length)]
print(arr)

print(f"Arr:\t{arr}")
print(f"max(arr) = {max(arr)}")
print(countingsort(arr))
