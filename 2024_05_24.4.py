a = []

for i in range (1,11):
    frandscore = int(input("친구 점수:"))
    a.append(frandscore)
    result = sum(a)

print(result / len(a))



