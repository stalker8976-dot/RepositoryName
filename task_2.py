# TODO Найдите количество книг, которое можно разместить на дискете
bytes_simvol = 4 # TODO байт на один символ
simvolov_ctroke = 25 # TODO символов в строке
ctrok_ctranige = 50 # TODO строк на странице
ctranige_book = 100 # TODO страниц в книге
disketa_xranilige = 1.44 # TODO обьем дискеты
# TODO рачет обьема одной книги в байтах
total_bytes_book = bytes_simvol * simvolov_ctroke * ctrok_ctranige * ctranige_book
# TODO перевод дискеты в байты
disketa_xranilige_b = disketa_xranilige * 1024 * 1024
# TODO количество книг помещающихся в дискету
d_books = int(disketa_xranilige_b // total_bytes_book)

print("Количество книг, помещающихся на дискету:", d_books)
