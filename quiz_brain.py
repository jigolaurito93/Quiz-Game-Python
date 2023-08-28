# TODO: Ask questions
# TODO: Check if the answer was correct
# TODO: Check if were at the end of the quiz

class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False) :")
       