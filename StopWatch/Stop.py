import time
import tkinter as tk
from tkinter import ttk

class FuturisticStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Stopwatch with Lap Feature")
        self.root.geometry("500x550")
        self.root.configure(bg="#121212")

        self.start_time = 0
        self.running = False
        self.elapsed_time = 0
        self.laps = []
        self.last_action = None

        # Timer Display
        self.timer_display = tk.Label(
            self.root,
            text="00:00:00.000",
            font=("Orbitron", 30, "bold"),
            bg="#121212",
            fg="#00FFEA",
            padx=20,
            pady=10
        )
        self.timer_display.pack(pady=20)

        # Instructions
        self.label_info = tk.Label(
            self.root,
            text="Slide to Control Stopwatch",
            font=("Poppins", 13, "italic"),
            bg="#121212",
            fg="#A3A3A3"
        )
        self.label_info.pack(pady=5)

        # Slider Control
        self.slider_control = tk.Scale(
            self.root,
            from_=0, to=2,
            orient=tk.HORIZONTAL,
            length=350,
            showvalue=False,
            tickinterval=1,
            resolution=1,
            bg="#121212",
            fg="#00FFEA",
            troughcolor="#007BFF",
            sliderlength=45,
            width=18,
            font=("Arial", 11),
            highlightbackground="#00FFEA",
            command=self.slider_action
        )
        self.slider_control.pack(pady=10)

        # Slider Labels
        self.label_frame = tk.Frame(self.root, bg="#121212")
        tk.Label(self.label_frame, text="▶ Start", bg="#121212", fg="#00FF00", font=("Arial", 12)).pack(side=tk.LEFT, padx=50)
        tk.Label(self.label_frame, text="■ Stop", bg="#121212", fg="#FF4500", font=("Arial", 12)).pack(side=tk.LEFT, padx=50)
        tk.Label(self.label_frame, text="↻ Reset", bg="#121212", fg="#1E90FF", font=("Arial", 12)).pack(side=tk.LEFT, padx=50)
        self.label_frame.pack()

        # Lap Button
        self.lap_button = tk.Button(self.root, text="Lap", command=self.record_lap, font=("Arial", 14), 
                                    bg="#1E90FF", fg="white", width=8)
        self.lap_button.pack(pady=10)

        # Lap Listbox
        self.lap_listbox = tk.Listbox(self.root, font=("Arial", 12), width=30, height=8, bg="#121212", 
                                      fg="#00FFEA", selectbackground="gray")
        self.lap_listbox.pack(pady=10)

        # Keyboard Shortcuts
        self.root.bind("<space>", lambda event: self.start_stop())
        self.root.bind("r", lambda event: self.reset_timer())
        self.root.bind("l", lambda event: self.record_lap())

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.timer_display.config(text=self.format_time(self.elapsed_time))
            self.root.after(10, self.update_time)

    def start_timer(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.elapsed_time = 0
        self.laps.clear()
        self.timer_display.config(text="00:00:00.000")
        self.lap_listbox.delete(0, tk.END)

    def record_lap(self):
        if self.running:
            lap_time = self.format_time(self.elapsed_time)
            lap_diff = self.format_time(self.elapsed_time - self.laps[-1] if self.laps else self.elapsed_time)
            self.laps.append(self.elapsed_time)
            self.lap_listbox.insert(tk.END, f"Lap {len(self.laps)}: {lap_time} (+{lap_diff})")

    def slider_action(self, value):
        value = int(value)

        if value == self.last_action:
            return

        if value == 0:
            self.start_timer()
        elif value == 1:
            self.stop_timer()
        elif value == 2:
            self.reset_timer()

        self.last_action = value

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        millis = (seconds - int(seconds)) * 1000
        return f"{int(minutes):02}:{int(seconds):02}:{int(millis):03}"

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = FuturisticStopwatch(root)
    root.mainloop()
