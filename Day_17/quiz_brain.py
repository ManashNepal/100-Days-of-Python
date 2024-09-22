class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer, question_answer)
    
    def check_answer(self, user_anwer, question_anwer):
        if user_anwer.lower() == question_anwer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {question_anwer}")
        print(f"Your current score is: {self.score}/{self.question_number}")


        

