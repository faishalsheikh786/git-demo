class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name 
        self.roll_no = roll_no
        self.branch = branch

    def __str__(self):
        print(f"Name : {self.name}\nRoll No : {self.roll_no}\nBranch : {self.branch}")
        