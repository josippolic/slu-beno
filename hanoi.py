def hanoi(n, izvor, cilj, pomocni):
    if n == 1:
        print(f"Premesti disk 1 sa {izvor} na {cilj}")
        return
    
    hanoi(n - 1, izvor, pomocni, cilj)
    print(f"Premesti disk {n} sa {izvor} na {cilj}")
    hanoi(n - 1, pomocni, cilj, izvor)

# Demonstracija sa 3 diska
broj_diskova = 3
print(f"Resenje problema Tornjeva Hanija za {broj_diskova} diska:")
hanoi(broj_diskova, 'A', 'C', 'B')  # Stubovi: A (izvor), C (cilj), B (pomoćni)
