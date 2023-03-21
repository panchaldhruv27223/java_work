class library :
    def __init__(self , listofbooks) :
        self.books = listofbooks

    def desplayAvaliableBooks(self):
        print("avaliable books are :")
        for book in self.books :
            print("\t*" +book)
            
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued a {bookname} book and return it within 30 days .")
            self.books.remove(bookname) 
            return True
        else:
            print(f"sorry , {bookname} book was already issued . you can try after few days.")
            return False
    
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("return successful. have a great day.")




class studant :
    def requestbook(self):
        self.book =input("enter a name of book you want to borrow :")
        return self.book
    
    def returnbook(self):
        self.book = input("enter a name of book you want to return :")
        return self.book



if __name__ == "__main__" :
    centerlibrary = library(["java" , "python" ,"c","Algorithm","cn","ada"])
    # centerlibrary.desplayAvaliableBooks()

    studant = studant()

    while(True):
        welcomemsg = '''
    ====welcome to the central library
    please choose an option
    1.list all the books 
    2.request a book 
    3.return a book
    4.exit'''
        print(welcomemsg)

        a = int(input("Enter a choise : "))

        if a == 1 :
            centerlibrary.desplayAvaliableBooks()
        
        elif a ==2 :
            centerlibrary.borrowbook(studant.requestbook())
        elif a == 3 :
            centerlibrary.returnbook(studant.returnbook())
        elif a == 4 :
            print("thanks for chosing central library. have a great day ahead .")
            exit()
        else :
            print("you chose a wrong option .")
        