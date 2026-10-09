# Using classes
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError('Missing name')
        
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    def charm(self):
        match self.patronus:
            case 'Stag':
                return 'has stag'
            case 'Otter':
                return 'has otter'
            case _:
                return 'nothing'
            
    # Getter - fn in a class that gets an attr
    def house(self):
        return self.house
    
    # Setter
    def house(self, house):
        self.house = house
     
def main():
    student = get_student()
    print(student)
    print(student.charm())
    
def get_student():
    n = input('Name: ')
    h = input('House: ')
    p = input('Patronus: ')
    
    student = Student(n, h, p)
    return student
    
if __name__ == '__main__': 
    main()