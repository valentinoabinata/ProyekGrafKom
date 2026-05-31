
from tkinter import *

class FormulaPanel(Frame):

    def __init__(self, parent):
        super().__init__(parent, bd=2, relief="groove")

        title = Label(
            self,
            text="FORMULA PANEL",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=5)

        frame = Frame(self)
        frame.pack(fill=BOTH, expand=True)

        self.text = Text(
            frame,
            wrap=WORD,
            font=("Consolas", 10)
        )

        scrollbar = Scrollbar(
            frame,
            orient=VERTICAL,
            command=self.text.yview
        )

        self.text.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)

    def update_formula(self, content):

        self.text.config(state="normal")

        self.text.delete("1.0", END)

        self.text.insert("1.0", str(content))

        self.text.config(state="normal")
