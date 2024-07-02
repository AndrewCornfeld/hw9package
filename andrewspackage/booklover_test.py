import unittest
import booklover

class BookLoverTestSuite(unittest.TestCase):
    
    
    def test_1_add_book(self): 
        
        bl1 = booklover.BookLover('john', 'john@gmail','all')
        bl1.add_book('book', 3)
        assert 'book' in list(bl1.book_list['book_name']), "Book was not in the list!"

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl2 = booklover.BookLover('john', 'john@gmail','all')
        bl2.add_book('book', 3)
        bl2.add_book('book', 4)
        assert (bl2.book_list.groupby('book_name').size()['book'] == 1), "Book was added twice!"
        
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl3 = booklover.BookLover('john', 'john@gmail','all')
        bl3.add_book('book', 3)
        assert (bl3.has_read('book')), "Book has not been read!"
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl4 = booklover.BookLover('john', 'john@gmail','all')
        bl4.add_book('book', 3)
        self.assertFalse(bl4.has_read('booijoijoijok')), "Book has not been read!"
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl5 = booklover.BookLover('john', 'john@gmail','all')
        bl5.add_book('book', 3)
        bl5.add_book('asdf', 4)
        bl5.add_book('new book', 1)
        assert (bl5.num_books_read() == 3), "Book count was inaccurate!"

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bl6 = booklover.BookLover('john', 'john@gmail','all')
        bl6.add_book('book', 3)
        bl6.add_book('asdf', 4)
        bl6.add_book('new book', 1)
        fav_books = bl6.fav_books()
        assert (bl6.book_list.loc[x] > 3 for x in fav_books), "Favorite books list was not accurate!"
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)