class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

rin = Student("Rin", 8888)
rin.print()
rin.changeID(3333)
rin.print()