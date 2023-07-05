class Student:
    ...
    def __init__(self, name, house):
        self.m_name = name
        self.m_house = house

    # place holder

def main():
    student = get_student()
    print(f"{student.m_name} from {student.m_house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == '__main__':
    main()