from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label()
        self.score.config(text=f"score: {self.quiz.score}", font=("Arial", 16, 'normal'), pady=20, bg=THEME_COLOR,
                          fg='white')
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Test", font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)

        false_bt_img = PhotoImage(file='images/false.png')
        self.false_bt = Button(image=false_bt_img, highlightthickness=0, command=self.false_bt)
        self.false_bt.grid(row=2, column=0, padx=(0, 0), pady=(20, 0))

        true_bt_img = PhotoImage(file='images/true.png')
        self.true_bt = Button(image=true_bt_img, highlightthickness=0, command=self.true_bt)
        self.true_bt.grid(row=2, column=1, padx=(0, 0), pady=(20, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas['bg'] = 'white'
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score['text'] = f"Score {self.quiz.score}"
        else:
            self.canvas.itemconfig(self.question_text , text = "You have reached all the questions")
            self.true_bt.config(state = "disabled")
            self.false_bt.config(state="disabled")

    def false_bt(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def true_bt(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas['bg'] = 'green'


        else:
            self.canvas['bg'] = 'red'

        self.window.after(1000, func=self.get_next_question)
