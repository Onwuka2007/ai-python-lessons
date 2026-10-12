import random

# define
class Hat:
    houses = ['Gr', 'Hu', 'Ra', 'Sl']
        
    @classmethod
    def sort_name(cls, student_name):
        print(f'{student_name} is in a {random.choice(cls.houses)}')
    
# Instantiate   
Hat().sort_name('Harry')