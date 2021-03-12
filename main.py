# import library
from tkinter import *
timer = None


# create an event handler
def handle_keyrelease(event):
    """Start the timer on a key release"""

    global timer

    # restart the timer on every key release
    if timer:
        window.after_cancel(timer)
    timer = window.after(5000, delete_text)


def delete_text():
    """a function that makes any text disappear after 5 seconds without typing"""

    # delete all text in the text box
    text_box.delete("1.0", END)


# create main window of the app
window = Tk()

# the size of the window is defined
window.minsize(width=450, height=200)
window.config(padx=40, pady=20)
window.title("Disappearing Text App")

# use label method of tkinter for labeling in window
warning = Label(text="WARNING: ALL TEXT DISAPPEARS WHEN YOU DON'T TYPE FOR 5 SECONDS",
                font=("Arial", 10, "bold"), fg="red")
warning.pack(pady=10)

# text box
text_box = Text(width=50, height=5)
text_box.focus_set()
text_box.pack(pady=10)

# bind event to an event handler
text_box.bind("<KeyRelease>", handle_keyrelease)

message = Label(text="The timer starts once you start typing", font=("Arial", 15, "bold"))
message.pack(pady=10)

# start the GUI
window.mainloop()
