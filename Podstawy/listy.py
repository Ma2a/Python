"""
lista = ['text1', 25, 45.6, 'text2', 23]
print(type(lista))
print(lista[1])
print(lista[4])
print(lista[-2])
print(len(lista)) #długość listy
#zakres
print(lista[0:4])
print(lista[2:4])
print(lista[1:])
print(lista[::2])
lista[1] = 'test'
print(lista)
del lista[1]
print(lista)

for data in lista:
    print(data)

if 'text2' in lista:
    print('text2 jest na liście')

print(45.6 in lista)

#lista wielopoziomowa
data1 = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five']]
print(data1[0][2])

#operator konkatenacji - łączenie list
data2 = ['Tomasz', 'Anna']
data3 = ['Robert', 'Kasia', 'Alicja']
data4 = data2 + data3
print(data4)

multiData = data2 * 4
print(multiData)
"""
#pusta lista
lista1=[]
print(lista1)
#metoda dodawania elementów na koniec listy
lista1.append(10)
print(lista1)
lista1.append('test')
print(lista1)
#metoda wyczyszczenie
lista1.clear()
print(lista1)
#przekopiowanie listy
x = [1, 2, 3, 4, 5, 6, 7]
y = x
x[0]=50
print(y)

a = [1,2,3,4,5,6]
b = a.copy()
a[0]=50
print(b)

#metoda zliczająca
z = [1,3,3,5,5,6,6,6,7]
print(z.count(6))
#metoda dodaje na koniec listy elementy innej listy
list1 = [1,2,2,3]
list2 = ['a', 'b', 'c']
list1.extend(list2)
print(list1)
#Metoda zwracająca numer indeksu pierwszego wystąpienia elementu
print(list1.index('a'))
print(list1.index(2,2))
print(list1.index('a',1,5))
#metoda wstawia nowy element listy w miejsce o wskazanym indeksie
print(list1)
list1.insert(3, 'test')
print(list1)
#Metoda usuwa elementy po indeksie pop(indeks)
print(list1.pop(5))

#Metoda usuwa pierwszy pasujący element z listy
list2 = [1, 2, 2, 3, 4, 5, 6]
print(list2)
list2.remove(2)
print(list2)

#metoda sortująca elementy listy
list3 = [5,2,3,8,4,1,7,6]
print(list3)
#niemalejące
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

#metoda odwracająca kolejność listy
list4= ['Tomasz', 'Ada','Bartek','Katarzyna']
list4.sort()
print(list4)
list4.reverse()
print(list4)