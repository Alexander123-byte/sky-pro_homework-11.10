import json

from question import Question


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    score = 0
    count_right_answers = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count_right_answers = count_right_answers + 1

    return f"Вот и всё!\n"\
           f"Отвечено {count_right_answers} вопроса из {len(questions)}\n"\
           f"Набрано баллов: {score}"
