class Student:
    def __init__(self, name, house):
        # This triggers the setters when the object is first created!
        self.name = name
        self.house = house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    # --- GETTERS ---
    @property
    def name(self):
        return self._name
    
    @property
    def house(self):
        return self._house
    
    # --- SETTERS ---
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        # FIX: Save to _name, don't just return it
        self._name = name
    
    @house.setter
    def house(self, house):
        if not house:
            raise ValueError('Missing house')
        # FIX: Save to _house, using self.house here would loop infinitely!
        self._house = house
        
    @classmethod
    def get_student(cls):
        name = input('Enter your name: ')
        house = input('Enter your house: ')
        return cls(name, house)
       
def main():
    student = Student.get_student()
    print(student)
    
    # This assignment automatically triggers the 'house' setter method!
    student.house = 'Number 4, Privet Drive'
    print(student)
    
    
if __name__ == '__main__': 
    main()