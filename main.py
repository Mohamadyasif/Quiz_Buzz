from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question=Questions(question_text, question_answer)
    question_bank.append(new_question)
q_brain=QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()
print("you have completed the quiz")
print(f"your final score is{q_brain.score}/{q_brain.question_number}")