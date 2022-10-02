# qa_python

## Создаём класс для покрытия тестами нашего приложения _BooksCollector_ :

```python
class TestBooksCollector:
```

## **Тест 1.** Проверка добавления книг
### Создаём функцию проверки добавления 2 книг и объект класса _BooksCollector_ :

```python
        def test_add_new_book_add_two_books(self):
            collector = BooksCollector()
```

### Добавляем в объект 2 книги и проверяем, что добавилось именно 2 :

```python
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2
```

## **Тест 2.** Нельзя добавить одну и ту же книгу дважды
### Создаём функцию проверки добавления 2-х одинаковых книг и объект класса _BooksCollector_ :

```python
    def test_add_new_book_add_two_identical_books_impossible(self):
        two_identical_books = BooksCollector()
```

### Добавляем в объект 2 книги с одиноковым названием и проверяем, что добавилось только одна :

```python
        two_identical_books.add_new_book('1984')
        two_identical_books.add_new_book('1984')
        assert len(two_identical_books.get_books_rating()) == 1
```

## **Тест 3.** Нельзя выставить рейтинг книге, которой нет в списке
### Создаём функцию проверки добавления книги и объект класса _BooksCollector_ :

```python
    def test_set_book_rating_book_has_no_rating_impossible(self):
        book_has_no_rating = BooksCollector()
```

### Добавляем в объект книгу и добавляем рейтинг несуществующей книги, проверяем, что функция _get_book_rating_ вернёт значение только добавленной книги :

```python
        book_has_no_rating.add_new_book('1984')
        book_has_no_rating.set_book_rating('О дивный новый мир', '10')
        assert book_has_no_rating.get_book_rating([0]) == 1
```

## **Тест 4.** Нельзя выставить рейтинг меньше 1
### Создаём функцию проверки рейтинга книги меньше 1 и объект класса _BooksCollector_ :

```python
    def test_get_book_rating_book_rating_less_than_one_impossible(self):
        book_rating_less_than_one = BooksCollector()
```

### Добавляем в объект книгу и добавляем ей рейтинг, затем меняем рейтинг на 0 и проверяем, что функция _get_book_rating_ вернёт значение только первоначально добавленного рейтинга :

```python
        book_rating_less_than_one.add_new_book('1984')
        book_rating_less_than_one.set_book_rating('1984', '9')
        book_rating_less_than_one.set_book_rating('1984', '0')
        assert book_rating_less_than_one.get_book_rating([0]) == 9
```

## **Тест 5.** Нельзя выставить рейтинг больше 10
### Создаём функцию проверки рейтинга книги больше 10 и объект класса _BooksCollector_ :

```python
    def test_get_book_rating_book_rating_more_than_ten_impossible(self):
        book_rating_more_than_ten = BooksCollector()
```

### Добавляем в объект книгу и добавляем ей рейтинг, затем меняем рейтинг на 11 и проверяем, что функция _get_book_rating_ вернёт значение только первоначально добавленного рейтинга :

```python
        book_rating_more_than_ten.add_new_book('1984')
        book_rating_more_than_ten.set_book_rating('1984', '8')
        book_rating_more_than_ten.set_book_rating('1984', '11')
        assert book_rating_more_than_ten.get_book_rating([0]) == 8
```

## **Тест 6.** Добавление книги в избранное
### Создаём функцию проверки добавления книги в избранное и объект класса _BooksCollector_ :

```python
    def test_add_book_in_favorites_selected_book_added(self):
        selected_book = BooksCollector()
```

### Добавляем в объект книгу, затем добавляем её же в избранное и проверяем длину списка избранных книг :

```python
        selected_book.add_new_book('1984')
        selected_book.add_book_in_favorites('1984')
        assert len(selected_book.get_list_of_favorites_books()) == 1
```

## **Тест 7.** Вывод книг с определенным рейтингом
### Создаём функцию проверки Вывода книг с определенным рейтингом и объект класса _BooksCollector_ :

```python
    def test_get_books_with_specific_rating_selected_book_with_rating_is_present(self):
        selected_book_with_rating = BooksCollector()
```

### Добавляем в объект книгу, добавляем ей определённый рейтинг, вывыдим эту книгу по её рейтингу :

```python
        selected_book_with_rating.add_new_book('1984')
        selected_book_with_rating.set_book_rating('1984', '7')
        selected_book_with_rating.get_books_with_specific_rating('7')
        assert selected_book_with_rating.get_books_with_specific_rating([0]) == '1984'
```

## **Тест 8.** Удаления книги из избранного
### Создаём функцию проверки удаления книги из избранного и объект класса _BooksCollector_ :

```python
    def test_delete_book_from_favorites_deleted_selected_book_possible(self):
        deleted_selected_book = BooksCollector()
```

### Добавляем в объект 2 книги, добавляем их в избранное, удалёем одну из книг, проверяем длину метода _get_list_of_favorites_books_ :

```python
        deleted_selected_book.add_new_book('1984')
        deleted_selected_book.add_new_book('О дивный новый мир')
        deleted_selected_book.add_book_in_favorites('1984')
        deleted_selected_book.add_book_in_favorites('О дивный новый мир')
        deleted_selected_book.delete_book_from_favorites('1984')
        assert len(deleted_selected_book.get_list_of_favorites_books()) == 1
```