class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        # This is why convention is member var name = arg name
        # The getter/setter is called for it
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"        

    # Getter
    # _house is used in both getter and setter
    @property 
    def house(self):
        return self._house
    
    # Setter
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    
def main():
    student = get_student()
    # setter will be called 
    # and will raise error if invalid house is set
    # student.house = "Number Four, Pivet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == '__main__':
    main()