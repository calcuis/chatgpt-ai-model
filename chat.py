import os
ModelPath="chat.gguf"

from tkinter import *
import tkinter.scrolledtext as st

root = Tk()
root.title("chatGPT")

if os.path.isfile(ModelPath) and os.access(ModelPath,os.R_OK):
    print("Model file exists and is readable.")
    from llama_cpp import Llama
    llm = Llama(model_path=ModelPath)

    root.columnconfigure([0, 1, 2], minsize=150)
    root.rowconfigure(0, weight=2)
    root.rowconfigure(1, weight=1)

    i = Entry()
    o = st.ScrolledText()

    def submit(i):
        root.title("Processing...")
        output = llm("Q: "+str(i.get()), max_tokens=2048, echo=True)
        answer = output['choices'][0]['text']
        print(answer)
        o.insert(INSERT, answer+"\n\n")
        i.delete(0, END)
        root.title("chatGPT")

    btn = Button(text = "Submit", command = lambda: submit(i))
    i.grid(row=1, columnspan=2, sticky="nsew")
    btn.grid(row=1, column=2, sticky="nsew")
    o.grid(row=0, columnspan=3, sticky="nsew")
else:
    print("Either model file (chat.gguf) is missing or is not readable.")
    e = Label(text="\n Either model file (chat.gguf) is missing or is not readable! \n")
    e.pack()

root.mainloop()
