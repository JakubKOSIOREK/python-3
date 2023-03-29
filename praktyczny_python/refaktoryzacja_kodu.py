"""Refaktoryzacja kodu to nic innego jak jego zmiana.
W tym przykładnie kolejno będziemy upraszczać kod tak,
aby stał się bardziej czytelny i łatwiejszy w obsłudze.
"""
#---------------------------------------------------------
# WERSJA 1 - przypatrujemy się logice liczenia
#---------------------------------------------------------
def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    return (subtotal + taxable_subtotal * 0.23 - (subtotal * 0.1 if subtotal > 100 else 0)) # 1. rozdzielamy linie

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 1 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 2
#---------------------------------------------------------
def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    return (subtotal
            + taxable_subtotal * 0.23 # 2. dla tej lini tworzymy nową zmienną tax = taxable_subtotal * 0.23
            - (subtotal * 0.1 if subtotal > 100 else 0))

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 2 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 3
#---------------------------------------------------------

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * 0.23
    return (subtotal
            + tax
            - (subtotal * 0.1 if subtotal > 100 else 0)) # 3. dla tej lini tworzymy nową zmienną discount = (subtotal * 0.1 if subtotal > 100 else 0)

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 3 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 4
#---------------------------------------------------------

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * 0.23
    discount = (subtotal * 0.1 if subtotal > 100 else 0) # 4. to możemy zmienić na prostę instrukcję if / else
    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 4 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 5
#---------------------------------------------------------

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * 0.23

    # 5. funkcję if / else przenosimy do osobnej podfunkcji
    if subtotal > 100:
        discount = subtotal * 0.1
    else:
        discount = 0
    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 5 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 6
#---------------------------------------------------------

def calculate_discount(subtotal):
    if subtotal > 100: # 6. dla tej lini tworzymy nową zmienną is_eligible_for_discount = subtotal > 100
        return subtotal * 0.1
    else:
        return 0

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * 0.23
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 6 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 7 - patrzymy na zmienne które są stałymi
#---------------------------------------------------------

def calculate_discount(subtotal):
    is_eligible_for_discount = subtotal > 100
    if is_eligible_for_discount:
        return subtotal * 0.1
    else:
        return 0

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * 0.23 # 7. dla tej lini tworzymy nową stałą TAX_RATE = 0.23
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 7 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 8
#---------------------------------------------------------

TAX_RATE = 0.23

def calculate_discount(subtotal):
    is_eligible_for_discount = subtotal > 100 # 8. dla tej lini tworzymy nową stałą MIN_SUBTOTAL_FOR_DISCOUNT = 100
    if is_eligible_for_discount:
        return subtotal * 0.1
    else:
        return 0

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * TAX_RATE
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 8 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 9
#---------------------------------------------------------

TAX_RATE = 0.23
MIN_SUBTOTAL_FOR_DISCOUNT = 100

def calculate_discount(subtotal):
    is_eligible_for_discount = subtotal > MIN_SUBTOTAL_FOR_DISCOUNT
    if is_eligible_for_discount:
        return subtotal * 0.1
    else:
        return 0

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * TAX_RATE
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 9 --> Total: {total}')

#---------------------------------------------------------
# WERSJA 10
#---------------------------------------------------------

TAX_RATE = 0.23
MIN_SUBTOTAL_FOR_DISCOUNT = 100
DISCOUNT_PERCENT = 0.1

def calculate_discount(subtotal):
    is_eligible_for_discount = subtotal > MIN_SUBTOTAL_FOR_DISCOUNT
    if is_eligible_for_discount:
        return subtotal * DISCOUNT_PERCENT
    else:
        return 0

def calculate_total():
    subtotal = 150.0
    taxable_subtotal = 100.0

    tax = taxable_subtotal * TAX_RATE
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

if __name__ == "__main__":
    total = calculate_total()
    print(f'\nwersja 10 --> Total: {total}')

print('\nPo refaktoryzacji kodu nadal jest zachowana jego funkcjonalnosć')