# Funktion 1
def strom_berechnen(leistung, spannung):
    # TODO
    pass
# Funktion 2
def spannungsfall(strom, widerstand):
    # Todo
    pass

# Funktion 3
def verlustleistung(strom, widerstand):
    # TODO
    pass
# Funktion 3
def verlustleistung(strom, widerstand):
    # TODO
    pass # Dies ist eine Pass Anweisung

leistung = 2000   # Watt
spannung = 230    # Volt
widerstand = 0.5  # Ohm

strom = strom_berechnen(leistung, spannung)
u_verlust = spannungsfall(strom, widerstand)
p_verlust = verlustleistung(strom, widerstand)

print("Strom:", round(strom, 2), "A")
print("Spannungsfall:", round(u_verlust, 2), "V")
print("Verlustleistung:", round(p_verlust, 2), "W")
