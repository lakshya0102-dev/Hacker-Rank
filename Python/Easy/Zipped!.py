n, x = map(int, input().split())

marks = []

for i in range(x):
    marks.append(map(float, input().split()))

for student in zip(*marks):
    print(sum(student) / x)
