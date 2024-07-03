class BookLover():
    import pandas as pd
    import numpy as np
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    def add_book(self, book_name, rating):
        if book_name in list(self.book_list['book_name']):
            print('this book is already in your book list!')
            return
        else:
            import pandas as pd
            new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
    def num_books_read(self):
        return len(list(self.book_list['book_name']))
    
    def fav_books(self):
        favs = self.book_list[self.book_list.book_rating > 3]
        return favs['book_name']
            
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # And so forth