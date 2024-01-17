### chatGPT
*** **run chatGPT locally (offline) - with basic GUI**
```
python chat.py
```
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-ai-model/master/demo.png" width="350" height="300">](https://github.com/calcuis/chatgpt-ai-model/blob/main/demo.png)

### code review

This Python code is a simple graphical user interface (GUI) application that uses the Llama to interact with a chat model for generating responses. Here's a breakdown of the code:

*install the llama-cpp-python library via pip or pip3 (once only)
```
pip install llama-cpp-python 
```
Importing Modules:
```
from llama_cpp import Llama
from tkinter import *
import tkinter.scrolledtext as st
```
The llama_cpp module is imported, which presumably provides an interface to the Llama chat model.
The Tk class from the tkinter module is imported for creating the main application window.
The scrolledtext module from tkinter is imported as st to create a scrolled text widget for displaying the chat history.

Creating Llama Instance:
```
llm = Llama(model_path="chat.gguf")
```
An instance of the Llama class is created with the specified model path ("chat.gguf"); get the sample pre-trained model file from releases (0.1).


Setting up the GUI:
```
root = Tk()
root.title("chatGPT")
root.columnconfigure([0, 1], minsize=180)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
```
A Tkinter root window is created with the title "chatGPT."
Column and row configurations are set to control the layout.

Creating Entry and ScrolledText Widgets:
```
i = Entry()
o = st.ScrolledText()
```
An Entry widget (i) is created for user input.
A scrolled text widget (o) is created for displaying the chat history.

Define Submit Function:
```
def submit(i):
    output = llm("Q: "+str(i.get()), max_tokens=1024, echo=True)
    answer = output['choices'][0]['text']
    print(answer)
    o.insert(INSERT, answer+"\n\n")
    i.delete(0, END)
```
The submit function is defined to handle the button click event.
It retrieves user input from the Entry widget (i), sends it to the Llama model, and retrieves the generated response.
The response is printed to the console and inserted into the scrolled text widget (o).
Clear the widget (i) after submission.

Create Submit Button:
```
btn = Button(text="Submit", command=lambda: submit(i))
```
A Button widget (btn) is created with the label "Submit," and the submit function is set as its command.

Grid Placement of Widgets:
```
i.grid(row=1, column=0, sticky="nsew")
btn.grid(row=1, column=1, sticky="nsew")
o.grid(row=0, columnspan=2, sticky="nsew")
```
The widgets are placed in the Tkinter grid layout.
The Entry widget (i) and the Submit button (btn) are placed in the second row, with the Entry widget in the first column and the button in the second column.
The scrolled text widget (o) spans across both columns and is placed in the first row.

When the user enters a question and clicks the "Submit" button, the input is sent to the Llama model, and the generated response is displayed in the scrolled text widget.

**Reference**

github.com/calcuis/llama-cpp-python-gradio-server

github.com/calcuis/chatgpt-command-line-interface
