"""date = 24
print(type(date))

info = "test"
print(type(info))

data1 = 56.3
print(type(data1))

#complex - Liczba zespolona
complexNum = 20 + 5j
print(type(complexNum))

#Ćwiczenie
print("-"*100)

avgNum = (4 + 6 + 7 + 9 + 12) / 5
print("Średnia z liczb", avgNum)
print("Typ danych", type(avgNum))

print("-"*100)

#Łańcuch znaków - string
text = "Hello World"
print(text)
print("Typ danych", type(text))
print(text[2])
x = text[6]
print(x)
print(text[6:])
print(text[::3])
print(text[2:8:3])
print(text[:8])
print(text[-3])
print(text * 3)
lines = '''Tekst próbny
kontynuacja w nowej linii
i jeszcze jednej linii'''

print(lines)

lines2 = "Pierwsza linia\nDruga linia\t oraz tabulacji\nTrzecia linia"
print(lines2)
print(len(lines2)) #len zwraca długość ciągu znaków

#Funkcja input
data2 = input("Podaj dane: ")

#Cwiczenie
print("Wpisz imię:")
name = input()
surname = input("Wpisz nazwisko: ")
print("Wpisz miasto: ")
city = input(">>>")
print(f"Nazywasz {name} {surname} mieszkasz w {city}")
"""

#Wartość logiczna - boolean
print("=" * 100)
a = True
print(a)
print(type(a))
print(10 > 12)
print(23 > 5)

number = 20

if  (number > 10):
    print(f"Liczba {number} jest większa od 10")


#Ćwiczenie
num = 0

if  num > 0:
    print(num, "jest liczbą dodatnią")

if  num < 0:
    print(num, "jest liczbą ujemną")

if num == 0:
    print(num, "jest równe zero")

#Liczba zmiennoprzecinkowa
num2 = 120.567
print(type(num2))
print(f"Liczba zaokrąglona do 2 miejsc {num2:.2f}")