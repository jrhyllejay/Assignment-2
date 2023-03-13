from Item import item

class book(item):

    ISBN = 0
    Author = ''
    Synopsis = ''

    def preview(self):
        print(f"Previewing{self.Title} by {self.Author}:\n{self.Synopsis}")