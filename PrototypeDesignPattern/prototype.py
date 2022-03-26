import copy


class Book:
    def __init__(self, name, authors, price, **kwargs):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        string_list = list()
        for k, v in self.__dict__.items():
            string_list.append(f"{k}: {v}")
        return "; ".join(string_list)


class NewBook:
    def __init__(self):
        self.objects = dict()

    def register(self, ident, obj):
        self.objects[ident] = obj

    def unregister(self, ident):
        del self.objects[ident]

    def clone(self, ident, **kwargs):
        found = self.objects.get(ident)
        if not found:
            raise ValueError("not found ident")
        obj = copy.deepcopy(found)
        obj.__dict__.update(kwargs)
        return obj


def main():
    old_book = Book(name="西游记", authors="曹雪芹", price="998刀", publisher="作家出版社")
    all_book = NewBook()
    CIP = "978-7-111-55797-5"
    all_book.register(CIP, old_book)
    new_book = all_book.clone(CIP, edition=2)
    for i in (old_book, new_book):
        print(i)


if __name__ == '__main__':
    main()
