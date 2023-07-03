class Student:
    ...
    # place holder

def main():
    student, gun = get_student()
    print(f"{student.m_name} from {student.m_house}, {gun.m_mag_size}, {gun.m_cost}")

def get_student():
    student = Student()
    student.m_name = input("Name: ")
    student.m_house = input("House: ")
    gun = Student()
    gun.m_mag_size = 15
    gun.m_cost = 2000
    return student, gun

if __name__ == '__main__':
    main()