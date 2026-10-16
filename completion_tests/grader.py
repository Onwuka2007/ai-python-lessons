lazy import statistics

class Question:
    def __init__(self, question_id, test, max_marks):
        self.question_id = question_id
        self.test = test
        self.max_marks = max_marks

    def __str__(self):
        return f"[Q{self.question_id}] {self.test} (Max Marks: {self.max_marks})"

    # Getter for max_marks
    @property
    def max_marks(self):
        return self._max_marks

    # setter
    @max_marks.setter
    def max_marks(self, max_marks):
        if max_marks <= 0:
            raise ValueError("Must be a positive number greater than zero.")
        self._max_marks = max_marks

    def grade(self, student_answers):
        raise NotImplementedError("Subclasses must implement grade()")


class MultipleChoiceQuestion(Question):
    def __init__(self, question_id, test, max_marks, correct_option):
        super().__init__(question_id, test, max_marks)
        self.correct_option = correct_option

    def grade(self, student_answer):
        if student_answer.strip().upper() == self.correct_option.strip().upper():
            return self.max_marks
        return 0


class CodeOutputQuestion(Question):
    def __init__(self, question_id, test, max_marks, expected_output):
        super().__init__(question_id, test, max_marks)
        self.expected_output = expected_output

    def grade(self, student_answer):
        if student_answer.strip().upper() == self.expected_output.strip().upper():
            return self.max_marks
        return 0


def main():
    try:
        _ = Question(0, "Broken", -5)
    except ValueError as e:
        print(f"Validation Caught: {e}\n")

    mcq = MultipleChoiceQuestion(1, "What keyword defines a function?", 5, "def")
    coq = CodeOutputQuestion(2, "Print hello world", 10, "Hello World")

    exam = [mcq, coq]

    # Keep track of all scores across the exam
    student_scores = []

    for question in exam:
        print(question)
        ans = input("What is your answer? ")

        # Grade the current question immediately
        score = question.grade(ans)
        student_scores.append(score)

        print("✅") if score == question.max_marks else print("❌")

    # After the loop is done, calculate the stats!
    total_earned = sum(student_scores)
    total_possible = sum(q.max_marks for q in exam)

    print("\n\n--- Exam Summary ---")
    print(f"Total Score: {total_earned} / {total_possible}")
    print(f"Average Question Score: {statistics.mean(student_scores)}")


if __name__ == "__main__":
    main()
