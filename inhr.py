class person:
    name=None
    def set_name(self,n):
        self.name=n
class student(person):
    age=0
    def set_age(self,a):
        self.age=a 
    def display(self):
        print(self.name)
        print(self.age)
s1=student()
s1.set_name("sam")
s1.set_age(22)
s1.display()  