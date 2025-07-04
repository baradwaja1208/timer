import tkinter as tk
from tkinter import messagebox

# Timer durations (in seconds)
WORK_TIME = 30 * 60  # ← change back to 30 * 60 for full use
SHORT_BREAK = 10 * 60
LONG_BREAK = 20 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x400")
        self.root.configure(bg="#E6E6FA")  # Light blue background

        # Timer label
        self.timer_label = tk.Label(
            self.root, text="30:00", font=("italic", 40, "bold"),
            fg="#1E3F66", bg="#DCEFFD"
        )
        self.timer_label.pack(pady=20)

        # Mode label
        self.mode_label = tk.Label(
            self.root, text="Work Time", font=("italic", 16),
            fg="#2F4858", bg="#DCEFFD"
        )
        self.mode_label.pack(pady=5)

        # Buttons
        self.start_button = tk.Button(
            self.root, text="Start", command=self.start_timer,
            width=10, bg="#4CAF50", fg="white", font=("Ttalic", 12, "bold")
        )
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(
            self.root, text="Stop", command=self.stop_timer,
            width=10, state=tk.DISABLED, bg="black", fg="white", font=("Ttalic", 12, "bold")
        )
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(
            self.root, text="Reset", command=self.reset_timer,
            width=10, bg="#2196F3", fg="white", font=("Arial", 12, "bold")
        )
        self.reset_button.pack(pady=5)

        # Timer variables
        self.work_time_left = WORK_TIME
        self.break_time_left = SHORT_BREAK
        self.is_work_time = True
        self.pomodoros_completed = 0
        self.is_running = False

        self.root.mainloop()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.work_time_left = WORK_TIME
        self.break_time_left = SHORT_BREAK
        self.is_work_time = True
        self.is_running = False
        self.timer_label.config(text="30:00")
        self.mode_label.config(text="Work Time")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if not self.is_running:
            return

        if self.is_work_time:
            self.work_time_left -= 1
            current_time = self.work_time_left
            if current_time <= 0:
                self.is_work_time = False
                self.pomodoros_completed += 1
                self.break_time_left = LONG_BREAK if self.pomodoros_completed % 4 == 0 else SHORT_BREAK
                messagebox.showinfo("Pomodoro Complete", "Time for a break!")
        else:
            self.break_time_left -= 1
            current_time = self.break_time_left
            if current_time <= 0:
                self.is_work_time = True
                self.work_time_left = WORK_TIME
                messagebox.showinfo("Break Over", "Back to work!")

        # Display updated time
        current_time = self.work_time_left if self.is_work_time else self.break_time_left
        minutes, seconds = divmod(current_time, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.mode_label.config(text="Work Time" if self.is_work_time else "Break Time")

        # 🟢 THIS LINE IS CRITICAL — it keeps updating every second
        self.root.after(1000, self.update_timer)

# Run it
PomodoroTimer()
