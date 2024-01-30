import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
SEC_IN_MIN = 1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    print("reset" + str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    print("set timer text to 00:00")
    title_label.config(text="Timer")
    print("set title label to Timer")
    check_marks.config(text="")
    print("set check marks to empty string")
    global reps
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print("reps: " + str(reps))

    work_sec = WORK_MIN * SEC_IN_MIN
    short_break_sec = SHORT_BREAK_MIN * SEC_IN_MIN
    long_break_sec = LONG_BREAK_MIN * SEC_IN_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        reset_timer()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pompodoro")

window.config(padx=100, pady=50, bg=YELLOW)

# Add image file using canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

# Timer label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Start button
start_btn = Button(text="Start", command=start_timer, bg="white", highlightthickness=0, font=(FONT_NAME, 10, "bold"))
start_btn.grid(column=0, row=2)

# Reset button
reset_btn = Button(text="Reset", bg="white", command=reset_timer, highlightthickness=0, font=(FONT_NAME, 10, "bold"))
reset_btn.grid(column=2, row=2)

# Check mark label
check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
