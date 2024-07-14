from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import requests
import sys

class QuestionAnswerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Question Answering App')

        layout = QVBoxLayout()

        self.question_label = QLabel('Question:')
        layout.addWidget(self.question_label)

        self.question_input = QTextEdit()
        layout.addWidget(self.question_input)

        self.context_label = QLabel('Context:')
        layout.addWidget(self.context_label)

        self.context_input = QTextEdit()
        layout.addWidget(self.context_input)

        self.answer_label = QLabel('Answer:')
        layout.addWidget(self.answer_label)

        self.answer_output = QTextEdit()
        self.answer_output.setReadOnly(True)
        layout.addWidget(self.answer_output)

        self.submit_button = QPushButton('Get Answer')
        self.submit_button.clicked.connect(self.get_answer)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def get_answer(self):
        question = self.question_input.toPlainText()
        context = self.context_input.toPlainText()
        response = requests.post('http://127.0.0.1:5001/ask', json={'question': question, 'context': context})  # Changed port to 5001
        answer = response.json().get('answer', 'No answer found')
        self.answer_output.setText(answer)

def main():
    app = QApplication(sys.argv)
    ex = QuestionAnswerApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
