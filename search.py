def trova_intervallo(x, intervalli):
    sinistra, destra = 0, len(intervalli) - 1
    
    while sinistra <= destra:
        medio = (sinistra + destra) // 2
        intervallo_corrente = intervalli[medio]
        
        if intervallo_corrente[0] <= x <= intervallo_corrente[1]:
            return medio  # Ritorna l'indice dell'intervallo trovato
        
        if x < intervallo_corrente[0]:
            destra = medio - 1
        else:
            sinistra = medio + 1
    
    return -1  # x non appartiene a nessun intervallo

# Esempio di utilizzo
x = 7.5
intervalli = [(0, 5), (5, 10), (10, 15), (15, 20)]
indice_intervallo = trova_intervallo(x, intervalli)
if indice_intervallo != -1:
    print(f"Il numero {x} appartiene all'intervallo {indice_intervallo}: {intervalli[indice_intervallo]}")
else:
    print(f"Il numero {x} non appartiene a nessun intervallo.")
