data = [0, 1, 2, 3, 4, 5, 6]
print(f"Długość listy data {len(data)}")
del data[0]
del data[1]
print(f"Długość listy data {len(data)}")
if 3 in data:
    print("3 jest na liście")

for el in data:
    print(el)