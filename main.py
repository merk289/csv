def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data_lines = lines[1:]

    def parse_line(line):
        parts = line.strip().split('|')
        return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]
    return list(map(parse_line, data_lines))


def filtered_books(books, search_word):
    filtered = filter(lambda book: search_word.lower() in book[1].lower(), books)
    def format_book(book):
        return [book[0], f"{book[1]}, {book[2]}", book[3], book[4]]

    return list(map(format_book, filtered))


def get_short_info(books):
    return list(map(lambda book: (book[0], book[2] * book[3]), books))

if __name__ == "__main__":
    # 1. Проверяем первое задание
    print("--- Задание 1 ---")
    books_list = get_books("books.csv")
    print(books_list)

    print("\n--- Задание 2 ---")
    filtered = filtered_books(books_list, "python")
    print(filtered)

    print("\n--- Задание 3 ---")
    short_info = get_short_info(filtered)
    print(short_info)