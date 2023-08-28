# TODO: Ask questions
# TODO: Check if the answer was correct
# TODO: Check if were at the end of the quiz

class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.current_score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) : ").capitalize()
        
        if answer != current_question.answer:
            return False
        self.current_score += 1
        print("You got it right!")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.current_score}/{self.question_number}.\n\n")
        return True

        
       