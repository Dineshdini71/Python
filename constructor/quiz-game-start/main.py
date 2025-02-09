from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score is {quiz.score}/{quiz.question_number}")



""" To generate the random question from online?
Here is website Line https://opentdb.com/
----- https://opentdb.com/api_config.php ----
"""