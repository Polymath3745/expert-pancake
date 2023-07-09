class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.m_name = name
        self.m_house = house

    
def main():
    student = get_student()
    print(f"{student.m_name} from {student.m_house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except AttributeError:
        print("Invalid")

if __name__ == '__main__':
    main()