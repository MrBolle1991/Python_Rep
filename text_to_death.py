from tkinter import *

def check_word_limit(event=None):
    text = entry.get("1.0", "end-1c")  # Hole den gesamten Text aus der Texteingabe
    char_count = len(text)             # Zähle die Zeichen im Text

    word_count_label.config(text=f"Characters till you dead: {char_count} / 100")

    if char_count >= 100:
        show_warning_window()

def show_warning_window():
    warning_window = Toplevel()  # Verwende Toplevel, um ein zusätzliches Fenster zu erzeugen
    warning_window.geometry("500x300")
    warning_window.title("BOOM!")  # Titel des zweiten Fensters geändert

    warning_label = Label(warning_window, text="You were killed because you talk too much bullshit!", font=("Arial", 16))
    warning_label.pack(padx=20, pady=30)

root = Tk()
root.geometry("1000x800")
root.title("Text to Death!")

warning_label = Label(root, text="Be careful, don't talk too much bullshit!", font=("Arial", 14))
warning_label.place(x=500, y=50, anchor="center")

warning_text = Label(root, text="Be careful and don't talk too much bullshit!", font=("Arial", 14))
warning_text.place(x=500, y=750, anchor="center")

input_frame = Frame(root)
input_frame.pack()

entry = Text(input_frame, width=100, height=20)
entry.pack(padx=10, pady=10)
entry.bind("<KeyRelease>", check_word_limit)

word_count_label = Label(root, text="Characters till you dead: 0 / 100", font=("Arial", 14))
word_count_label.place(x=800, y=10, anchor="ne")

root.mainloop()