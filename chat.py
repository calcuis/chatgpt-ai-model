from llama_cpp import Llama
llm = Llama(model_path="chat.gguf")
from tkinter import *
import tkinter.scrolledtext as st

root = Tk()
root.title("chatGPT")
root.columnconfigure([0, 1], minsize=180)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
i = Entry()
o = st.ScrolledText()

def submit(i):
    root.title("Processing...")
    output = llm("Q: "+str(i.get()), max_tokens=1024, echo=True)
    answer = output['choices'][0]['text']
    print(answer)
    o.insert(INSERT, answer+"\n\n")
    i.delete(0, END)
    root.title("chatGPT")

btn = Button(text = "Submit", command = lambda: submit(i))
i.grid(row=1, column=0, sticky="nsew")
btn.grid(row=1, column=1, sticky="nsew")
o.grid(row=0, columnspan=2, sticky="nsew")

root.mainloop()
