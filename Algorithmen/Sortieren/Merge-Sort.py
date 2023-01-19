def merge_sort(arr):
    #Wenn einzelner Wert, dann diesen zurückgeben -> trivial sortiert
    if len(arr) <= 1:
        return arr

    #Mitte des Arrays finden
    mid = len(arr) // 2
    
    #Linke hälfte des Arrays und rekursiver Aufruf von merge_sort()
    left_half = merge_sort(arr[:mid])
    
    #Rechte hälfte des Arrays und rekursiver Aufruf von merge_sort()
    right_half = merge_sort(arr[mid:])
    
    #Aufruf von merge(mit den beiden Teilarrays) innerhalb der rekursiven Funktion merge_sort()
    return merge(left_half, right_half)

def merge(left, right):
    #Neues, leeres Array deklarieren
    result = []
    
    #Zählervariablen
    i = 0
    j = 0
    
    #Solange Arrays noch nicht vollständig durchlaufen wurden:
    #Sobald eines der beiden abgeschlossen ist, ist die Schleife zuende, obwohl in einem noch unverarbeitete Werte vorhanden sind!
    #Diese müssen am Ende der Funktion angehangen werden. Das kann einfach gemacht werden, da die Teilarrays bereits richtig sortiert sind.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            #Wenn der Wert aus dem Linken Array kleiner ist, wird dieser zuerst dem sortierten Array hinzugefügt.
            result.append(left[i])
            i += 1
        else:
            #Wenn der Wert aus dem Linken Array kleiner ist, wird dieser zuerst dem sortierten Array hinzugefügt.
            result.append(right[j])
            j += 1
    
    #Rest aus dem nicht vollständig durchlaufenen Array hinten anhängen. Dass abgearbeite ist in dem Fall: []
    result += left[i:]
    result += right[j:]
    
    #Rückgabe des sortierten Array
    return result


##############################################
#Testcode

#Definition des zu Sortierenden Array
arr = [5,9,6,8,2,1,0,8,6]

#Ausgabe Unsortiert und Sortiert.
print(f"Unsortiert:\t {arr}")
print(f"Sortiert:\t {merge_sort(arr)}")