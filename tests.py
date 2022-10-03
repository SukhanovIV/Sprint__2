from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_example_impossible(self):
        example = BooksCollector()
        example.add_new_book('1984')
        example.add_new_book('1984')
        assert len(example.get_books_rating()) == 1

    def test_set_book_rating_example_impossible(self):
        example = BooksCollector()
        example.add_new_book('1984')
        example.set_book_rating('О дивный новый мир', 10)
        assert example.get_book_rating('О дивный новый мир') == None

    def test_get_book_rating_example_less_impossible(self):
        example_less = BooksCollector()
        example_less.add_new_book('1984')
        example_less.set_book_rating('1984', 9)
        example_less.set_book_rating('1984', 0)
        assert example_less.get_book_rating('1984') == 9

    def test_get_book_rating_example_more_impossible(self):
        example_more = BooksCollector()
        example_more.add_new_book('1984')
        example_more.set_book_rating('1984', 8)
        example_more.set_book_rating('1984', 11)
        assert example_more.get_book_rating('1984') == 8

    def test_add_book_in_favorites_example_added(self):
        example = BooksCollector()
        example.add_new_book('1984')
        example.add_book_in_favorites('1984')
        assert len(example.get_list_of_favorites_books()) == 1

    def test_get_books_with_specific_rating_example_is_present(self):
        example = BooksCollector()
        example.add_new_book('1984')
        example.set_book_rating('1984', 7)
        example = example.get_books_with_specific_rating(7)
        assert example[0] == '1984'

    def test_delete_book_from_favorites_example_possible(self):
        example = BooksCollector()
        example.add_new_book('1984')
        example.add_new_book('О дивный новый мир')
        example.add_book_in_favorites('1984')
        example.add_book_in_favorites('О дивный новый мир')
        example.delete_book_from_favorites('1984')
        assert len(example.get_list_of_favorites_books()) == 1
