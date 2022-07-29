from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(
        Question(question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz_brain.current_score}/{len(question_bank)}")
