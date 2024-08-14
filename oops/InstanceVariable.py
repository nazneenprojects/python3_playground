class School:

    def __init__(self, name, std):  # This init method has all instance variable as below name, std, subjects
        self.name = name
        self.std = std
        self.subjects = []          # Empty subject list of each student of school

    def enroll_students(self, subjects):
        self.subjects.append(subjects)


if __name__ == '__main__':
    student_one = School('Harry', 1 )
    student_two = School('Rony', 2)
    student_three = School('Hermoinee', 2)

    student_one.enroll_students('dark arts')
    student_two.enroll_students('botany spell')
    student_three.enroll_students('magic spells')

    print(student_one.subjects)
    print(student_two.subjects)
    print(student_three.subjects)


