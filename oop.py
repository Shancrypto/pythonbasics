#oop is object oriented programming
# propertis + functions
#class #template
# book - title,author,isbn,price

class book:
    # constructor == function
     def __init__(self, title, author, price, isbn):
            self.title = title
            self.author = author
            self.price = price
            self.isbn = isbn
     def print_details(self):
         print("Title",self.title)
         print("Author",self.author)
         print("Price",self.price)
         print("Isbn",self.isbn)
         print("--------------")
     def appy_discount(self,discount):
         self.price = (self.price * (1- discount / 100))
         print("New price is", self.price)
b1 = book("Two Rivers", "Chinua Achebe", 70000, 90000)

b2 = book("Blossoms of Savvannah", "Chinua Achibu", 7000, 9000)
b3 = book("A Doll`s House", "Chanua Achebe", 72000, 92200)
b1.print_details()
b1.appy_discount(10)
b1.print_details()
# print(h2.price) incase want to print price only
b2.print_details()
b3.print_details()
#copy branch
# push
# raise pull request
# accept == merge
# deploy == server
