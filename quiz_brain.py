# TODO: Ask questions
# TODO: Check if the answer was correct
# TODO: Check if were at the end of the quiz

class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.current_score = 0

    def still_has_questions(self):
        length_of_list = len(self.questions_list)
        if self.question_number < length_of_list:
            return True
        else:
            False
        
    # Ask input for question and increment the question number to 1
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) : ").capitalize()

        self.check_answer(answer, current_question.answer)
        
        
        
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print('Youre right')
            self.current_score  += 1
        else: 
            print("Youre wrong")
        
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.current_score}/{self.question_number}.")
        print("\n")
            
        
        # self.current_score += 1
        # print("You got it right!")
        # print(f"The correct answer was: {correct_answer}.")
        # print(f"Your current score is: {self.current_score}/{self.question_number}.\n\n")
        # return True


        
       