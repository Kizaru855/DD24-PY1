# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_bytes = 1.44 * 1024 * 1024

symbol_size = 4
symbols = 25
lines = 50
pages = 100

book_size = symbol_size * symbols * lines * pages

books_amount = int(disk_size_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books_amount)
