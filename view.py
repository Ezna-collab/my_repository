import customtkinter as ctk

class CalculatorView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Calculatrice")
        self.geometry("300x400")

        self.display = ctk.CTkEntry(self, font=("Arial",24), justify="right")
        self.display.grid(row=0,column=0,columnspan=7,sticky="nsew",padx=10,pady=10)

        self.buttons = {}
        btns = [
                        '⌫',
            'C','()','%','Ω',
            '7','8','9','+',
            '4','5','6','-',
            '1','2','3','*',
            '±','0','.','/',
                  '=',

        ]

        for i, b in enumerate(btns):
            btn = ctk.CTkButton(self,text=b)
            btn.grid(row=(i//4)+1,column=i%4,sticky="nsew",padx=5,pady=5)
            self.buttons[b] = btn

        for i in range(5):
            self.grid_rowconfigure(i,weight=1)
        for i in range(4):
            self.grid_columnconfigure(i,weight=1)

    def set_display(self, text):
        self.display.delete(0,ctk.END)
        self.display.insert(0,text)
