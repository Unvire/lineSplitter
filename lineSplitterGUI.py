import tkinter as tk
from tkinter.messagebox import showinfo,showerror

class LineSplitter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Line splitter')
        self.geometry('700x600')
        self.resizable(False, False)

        self.frame = tk.Frame()

        self.inputLabel = tk.Label(self.frame, text='Paste input string')
        self.inputEntry = tk.Entry(self.frame, width=105)
        self.separatorLabel = tk.Label(self.frame, text='Separator character')
        self.separatorEntry = tk.Entry(self.frame)
        self.wordsInLineLabel = tk.Label(self.frame, text='Number of elements in one row')
        self.wordsInLineEntry = tk.Entry(self.frame)
        self.generateButton = tk.Button(self.frame, text='Generate', command=lambda: self.generateText())
        self.replaceButton = tk.Button(self.frame, text='Replace "." to ","', state='disabled', command=lambda: self.replaceCommas())
        self.saveButton = tk.Button(self.frame, text='Save to txt file', state='disabled', command=lambda: self.saveFile())
        self.generatedDataText = tk.Text(self.frame)
        self.emptyLabel1 = tk.Label(self.frame)
        self.emptyLabel2 = tk.Label(self.frame)

        self.inputLabel.grid(row=0, column=0, columnspan=2)
        self.inputEntry.grid(row=1, column=0, columnspan=2)
        self.separatorLabel.grid(row=2, column=0)
        self.separatorEntry.grid(row=3, column=0)
        self.wordsInLineLabel.grid(row=2, column=1)
        self.wordsInLineEntry.grid(row=3, column=1)
        self.generateButton.grid(row=4, column=0, columnspan=2)
        self.emptyLabel1.grid(row=5, column=0, columnspan=2)
        self.generatedDataText.grid(row=6, column=0, columnspan=2)
        self.emptyLabel2.grid(row=7, column=0, columnspan=2)
        self.replaceButton.grid(row=8, column=0)
        self.saveButton.grid(row=8, column=1)
        self.frame.pack()

        self.bind('<Return>', lambda x: self.generateText())

    def generateText(self):
        inputText = self.inputEntry.get()
        separator = self.separatorEntry.get()
        wordsInLine = self.wordsInLineEntry.get()

        noError = True
        try:
            wordsInLine = int(wordsInLine)
        except ValueError:
            noError = False

        if noError and wordsInLine > 0:
            text = inputText.split(separator)
            textOut = []

            for i, word in enumerate(text):
                textOut.append(word + ';')
                if (i + 1) % wordsInLine == 0:
                    textOut.append('\n')

            self.generatedDataText.delete('1.0',tk.END)
            self.generatedDataText.insert('1.0', ''.join(textOut))

            self.replaceButton['state'] = 'normal'
            self.saveButton['state'] = 'normal'

        else:
            tk.messagebox.showerror('Error', 'Expected a positive integer in the "number of words in one row" textbox')

    def replaceCommas(self):
        text = self.generatedDataText.get('1.0',tk.END)
        textOut = text.replace('.',',')

        self.generatedDataText.delete('1.0',tk.END)
        self.generatedDataText.insert('1.0', ''.join(textOut))

    def saveFile(self):
        text = self.generatedDataText.get('1.0',tk.END)
        with open('output.txt','w') as outputFile:
            outputFile.write(text)





if __name__ == '__main__':
    app = LineSplitter()
    app.mainloop()

