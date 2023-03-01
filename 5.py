n = int(input("Введите количество слов: "))
w = []

for i in range(n):
    word = input("Введите слово: ")
    w.append(word)

result = " ".join(w)

print("Результат:", result)