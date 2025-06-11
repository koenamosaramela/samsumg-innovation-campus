class Student:
    def __init__(self, name, student_id):

        self.name = name
        self.student_id = student_id
        self.eng_quiz = []
        self.math_quiz = []
        self.science_quiz = []

    def __str__(self):

        return (f"Name : {self.name}, ID : {self.student_id}\n"
                f"English quiz score : {', '.join(map(str, self.eng_quiz))
                if self.eng_quiz 
                else 'N/A'}, "
                
                f"Mathematics quiz score : {', '.join(map(str, self.math_quiz)) 
                if self.math_quiz
                else 'N/A'}\n"
                
                f"Science quiz score : {', '.join(map(str, self.science_quiz))
                if self.science_quiz 
                else 'N/A'},")

    def set_eng_quiz(self, score):
        self.eng_quiz.append(score)

    def set_math_quiz(self, score):
        self.math_quiz.append(score)

    def set_science_quiz(self, score):
        self.science_quiz.append(score)

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_eng_quiz(self):
        return self.eng_quiz

    def get_math_quiz(self):
        return self.math_quiz

    def get_science_quiz(self):
        return self.science_quiz

    def get_total_score(self):
        total = sum(self.eng_quiz) + sum(self.math_quiz) + sum(self.science_quiz)
        return total

    def get_avg_score(self):
        total_scores = self.get_total_score()
        num_quizzes = len(self.eng_quiz) + len(self.math_quiz) + len(self.science_quiz)
        if num_quizzes == 0:
            return 0.0
        return total_scores / num_quizzes

if __name__ == "__main__":

    student_name = input("Enter the student’s name : ")
    student_id = input("Enter the student’s ID : ")
    eng_score = int(input("Enter the student’s English quiz score : "))
    math_score = int(input("Enter the student’s mathematics quiz score : "))
    science_score = int(input("Enter the student’s science quiz score : "))
    print()

    student1 = Student(student_name, student_id)

    student1.set_eng_quiz(eng_score)
    student1.set_math_quiz(math_score)
    student1.set_science_quiz(science_score)

    print(student1)
    print()
    print(f"Total : {student1.get_total_score()}, Average : {student1.get_avg_score():.1f}")