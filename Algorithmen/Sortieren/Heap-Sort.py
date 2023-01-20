def heap_sort(arr):
    n = len(arr)
    
    # Erstelle einen Max-Heap
    # Anwenden der heapify() Funktion auf alle Knoten von hinten nach vorne.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    
    # Entferne eins nach dem anderen die größten Elemente
    for i in range(n-1, 0, -1):

        # tausche Wurzel ans Ende der Heap
        arr[i], arr[0] = arr[0], arr[i]

        # Max-Heap nach "entfernen" der Wurzel mit Heapify() wiederherstellen.
        # Sortieren erfolgt hier in-Place 
        # Durch Übergabe von i als länge des Array (n) an heapify() 
        # wird der sortierte Bereich am Ende des Array nicht bearbeitet und ignoriert.
        heapify(arr, i, 0)
    
    # Rückgabe des Sortierten Arrays
    return arr


def heapify(arr, n, i):
    # Setze largest als Wurzel
    largest = i

    # links = 2*i + 1
    l = 2 * i + 1

    # rechts = 2*i + 2
    r = 2 * i + 2

    # Überprüfe, ob linkes Kind von Wurzel existiert und größer ist als Wurzel
    if l < n and arr[i] < arr[l]:
        largest = l
    
    # Überprüfe, ob rechtes Kind von Wurzel existiert und größer ist als Wurzel
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Ändere Wurzel, falls nötig
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # tausche
        heapify(arr, n, largest)


################
# Testcode

def testcode1():
    arr = [2, 4, 63, 34, 7, 34, 6, 32, 1, 6, 89]

    print(f"Unsortiert:\t{arr}")
    print(f"Sortiert:\t{heap_sort(arr)}")


def testcode2():
    with open("Algorithmen/Sortieren/peformancetests/IntSet.txt", 'r') as f:
        strarr = f.readlines()

    arr = [int(x) for x in strarr]

    heap_sort(arr)


testcode2()