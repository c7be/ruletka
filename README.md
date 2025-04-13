# Gra Ruletka 🎰$$$

Ten program symuluje grę w ruletkę, w której użytkownik może obstawiać numery lub kolory i sprawdzać wyniki na podstawie wyników losowania.

## Funkcjonalności

- **Losowanie**: Program symuluje obroty koła ruletki, generując wyniki od 0 do 36.
- **Kolory**: Każda liczba jest przypisana do koloru: czerwony, czarny lub zielony.
- **Obstawianie**: Użytkownik może obstawiać konkretne liczby lub kolory.
- **Wygrana**: Program oblicza wygrane na podstawie reguł ruletki:
  - Wygrana za liczbę: 35x kwota zakładu.
  - Wygrana za kolor czerwony/czarny: 2x kwota zakładu.
  - Wygrana za kolor zielony (liczba 0): 30x kwota zakładu.

## Jak uruchomić

1. Upewnij się, że masz zainstalowany Python (w wersji 3.6+).
2. Skopiuj kod do pliku `roulette.py`.
3. Uruchom program:
   ```bash
   python roulette.py
