# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
import tkinter as tk
# from project import character

window = tk.Tk()
window.title("DnD Character Creator")
greeting = tk.Label(text="𝕯𝖓𝕯(5𝖊) 𝕮𝖍𝖆𝖗𝖆𝖈𝖙𝖊𝖗 𝕮𝖗𝖊𝖆𝖙𝖔𝖗",
                    foreground='white',
                    background='black')
greeting.pack()
start = tk.Label(text="Would you like to get started? y/n")
start_input = tk.Entry()
start.pack()
start_input.pack()

window.mainloop()
