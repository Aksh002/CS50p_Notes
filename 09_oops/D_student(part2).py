class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
    def __str__(self):
        return f"{self.name} is from {self.house}"
    @classmethod
    def get(cls):
        name=input("name: ")
        house=input("House: ")
        return cls(name,house)  #return Student(name,house)
        #This cls() used above is a features of oops that u can now instentiate a student obj just using cls thats passed in.We can technically use Student() also bit cls is much safe
        #This above line means create an obj of the current class,whatever cls is,which is Here gonna be Student.It is initaillise withname and house
#This is by nature of class in oops, all student specific fxnality
def main():
    student=Student.get()
    print(student)    

if __name__=="__main__":
    main()
#It is weired if u had to create student obj in order to call get,in order to get another student,thats inefficient.Here we will just get a student via class method that by defination does not require u to create a student obj first
#we dont need to create obj first,we will just use the class itself 
    
#All we hv done here is that we hv migrated all the logic frm a stand alone fxn student_get(chich was related to student) into the the class named Student as get(),but im calling get a classmethod to be able to call a get without having a student object in my universe alr.
    
#def main can be on the top also,doesnt matter where fxns are as main is called in the main only

#instance variables and instance methods belongs or operate on specific objects, class variables and methods operate on the entire class itself,all obj of the class 
    
#                  static methods
#   @staticmethod decorator used here
    



 