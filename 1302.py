n = int(input())


books = {}
for _ in range(n):
    title = input()
    if title in books.keys():
        books[title] += 1
    else:
        books[title] = 1


print(books.sort())
