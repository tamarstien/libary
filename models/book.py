class Book :

    def __init__(self,name,auther,id,genere):
        self.name=name
        self.auther=auther
        self.id = id
        self.is_borrowed=False
        self.genere=genere


    def print(self):
        return f"{self.name} {self.auther}"

    def __repr__(self):
        return f'Book(name="{self.name}", author="{self.auther}", id="{self.id} ,is_borrowed="{self.is_borrowed},genere={self.genere})'
