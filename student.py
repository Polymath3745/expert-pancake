class Student:
    def __init__(self, name, house):
        self.m_name = name
        self.m_house = house

    def check_house(self):
        houses = ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if (self.m_house in houses):
            print("passed")
        else:
            print("fail")
    

    # place holder

def main():
    student = get_student()
    student.check_house()
    print(type(student.m_house))
    print(f"{student.m_name} from {student.m_house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == '__main__':
    main()