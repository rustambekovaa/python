import json

class Answer:
    def __init__(self, text, is_correct):
        self.text = text
        self.is_correct = is_correct

    def to_dict(self):
        return {"text": self.text, "is_correct": self.is_correct}

class Question:
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers

    def to_dict(self):
        return {"text": self.text, "answers": [answer.to_dict() for answer in self.answers]}

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def to_dict(self):
        return {"name": self.name, "questions": [question.to_dict() for question in self.questions]}

def add_quiz():
    name = input("Enter quiz name: ")
    questions = []

    while True:
        text = input("Enter question text (or 'done' to finish adding questions): ")
        if text.lower() == "done":
            break

        answers = []
        while True:
            answer_text = input("Enter answer text (or 'done' to finish adding answers): ")
            if answer_text.lower() == "done":
                break
            is_correct = input("Is this answer correct? (yes/no): ").lower() == "yes"
            answers.append(Answer(answer_text, is_correct))
        
        questions.append(Question(text, answers))

    quiz = Quiz(name, questions)
    return quiz

def remove_quiz(quizzes):
    name = input("Enter the name of the quiz you want to remove: ")
    for quiz in quizzes:
        if quiz.name == name:
            quizzes.remove(quiz)
            print(f"Quiz '{name}' removed successfully.")
            return
    print(f"Quiz '{name}' not found.")

def view_quizzes(quizzes):
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz.name}")



def take_quiz(quiz):
    print(f"Taking quiz: {quiz.name}")
    score = 0
    for question in quiz.questions:
        print(question.text)
        for idx, answer in enumerate(question.answers, start=1):
            print(f"{idx}. {answer.text}")
        choice = int(input("Enter your choice: ")) - 1
        if question.answers[choice].is_correct:
            score += 1
    print(f"Your score: {score}/{len(quiz.questions)}")

def save_quizzes(quizzes):
    with open("quizzes.json", "w", encoding="utf-8") as file:
        json.dump([quiz.to_dict() for quiz in quizzes], file, ensure_ascii=False)

def load_quizzes():
    try:
        with open("quizzes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            quizzes = []
            for quiz_data in data:
                questions = []
                for question_data in quiz_data["questions"]:
                    answers = []
                    for answer_data in question_data["answers"]:
                        answers.append(Answer(answer_data["text"], answer_data["is_correct"]))
                    questions.append(Question(question_data["text"], answers))
                quizzes.append(Quiz(quiz_data["name"], questions))
            return quizzes
    except FileNotFoundError:
        return []

def main():
    quizzes = load_quizzes()

    while True:
        print("\n1. Add quiz")
        print("2. Remove quiz")
        print("3. View quizzes")
        choice = input("Enter your choice: ")

        if choice == "1":
            quiz = add_quiz()
            quizzes.append(quiz)
            save_quizzes(quizzes)
        elif choice == "2":
            remove_quiz(quizzes)
            save_quizzes(quizzes)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
