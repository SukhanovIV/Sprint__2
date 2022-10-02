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
    def test_add_new_book_add_two_identical_books_impossible(self):
        two_identical_books = BooksCollector()
        two_identical_books.add_new_book('1984')
        two_identical_books.add_new_book('1984')
        assert len(two_identical_books.get_books_rating()) == 1
    def test_set_book_rating_book_has_no_rating_impossible(self):
        book_has_no_rating = BooksCollector()
        book_has_no_rating.add_new_book('1984')
        book_has_no_rating.set_book_rating('О дивный новый мир', '10')
        assert book_has_no_rating.get_book_rating([0]) == 1
    def test_get_book_rating_book_rating_less_than_one_impossible(self):
        book_rating_less_than_one = BooksCollector()
        book_rating_less_than_one.add_new_book('1984')
        book_rating_less_than_one.set_book_rating('1984', '9')
        book_rating_less_than_one.set_book_rating('1984', '0')
        assert book_rating_less_than_one.get_book_rating([0]) == 9
    def test_get_book_rating_book_rating_more_than_ten_impossible(self):
        book_rating_more_than_ten = BooksCollector()
        book_rating_more_than_ten.add_new_book('1984')
        book_rating_more_than_ten.set_book_rating('1984', '8')
        book_rating_more_than_ten.set_book_rating('1984', '11')
        assert book_rating_more_than_ten.get_book_rating([0]) == 8
    def test_add_book_in_favorites_selected_book_added(self):
        selected_book = BooksCollector()
        selected_book.add_new_book('1984')
        selected_book.add_book_in_favorites('1984')
        assert len(selected_book.get_list_of_favorites_books()) == 1
    def test_get_books_with_specific_rating_selected_book_with_rating_is_present(self):
        selected_book_with_rating = BooksCollector()
        selected_book_with_rating.add_new_book('1984')
        selected_book_with_rating.set_book_rating('1984', '7')
        selected_book_with_rating.get_books_with_specific_rating('7')
        assert selected_book_with_rating.get_books_with_specific_rating([0]) == '1984'
    def test_delete_book_from_favorites_deleted_selected_book_possible(self):
        deleted_selected_book = BooksCollector()
        deleted_selected_book.add_new_book('1984')
        deleted_selected_book.add_new_book('О дивный новый мир')
        deleted_selected_book.add_book_in_favorites('1984')
        deleted_selected_book.add_book_in_favorites('О дивный новый мир')
        deleted_selected_book.delete_book_from_favorites('1984')
        assert len(deleted_selected_book.get_list_of_favorites_books()) == 1