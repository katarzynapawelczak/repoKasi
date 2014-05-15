def dodaj(a, b):
    return a+b
    
def getInfo():
    print("To jest prosty program dodajacy dwie liczby")
    
getInfo()

liczba1 = int(input("Wprowadz pierwsza liczbe: "))
liczba2 = int(input("Wprowadz druga liczbe: "))
print(dodaj(liczba1, liczba2))
