list = [2200, 2350, 2600, 2130, 2190]
print(list[1] - list[0])
print(list[1] + list[0] + list[2])

for x in range(len(list)):
    if list[x] == 2000:
        print("true")
        break

print("false")

list.append(1980)
list.remove(2130)
list.insert(3, 1930)
print(list)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
heros.remove('black panther')
heros.insert(3, 'black panther')
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)

inp = int(input("Write a maximum number: "))
list = []

for num in range(1, inp):
    if num % 2 != 0:
        list.append(num)
print(list)