# TODO Найдите количество книг, которое можно разместить на дискете

size_bytes = 1.44 * 1024 * 1024

book_size = 4 * 25 * 50 * 100

books_amount = int(size_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books_amount)
