import os
import time
import tkinter as tk
from tkinter import messagebox

DEFAULT_GAP = 60 * 15

class SleepApp():
    def __init__(self, window):
        self.window = window
        self.window = tk.Frame(self.window, bg="white")
        self.window.pack(fill=tk.BOTH, expand=True)

        self.timer_text = tk.StringVar()
        self.timer_text.trace('w', self.build_timer)
        self.timer_left = tk.IntVar()
        #self.time_left.set(DEFAULT_GAP)
        if self.timer_left == '':
            pass
        else:
            self.timer_left.trace('w', self.go_to_sleep)

        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_entry()
        self.build_buttons()
        self.build_timer()

        self.update()


    def build_grid(self):
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)

    def build_banner(self):
        banner = tk.Label(
            self.window,
            background = "grey",
            text = "Sleep App",
            fg = "white",
            font = ("Helvetica", 20),

        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10,pady=10,
            columnspan = 3
        )

    def build_buttons(self):
        buttons_frame = tk.Frame(self.window)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=3)
        buttons_frame.columnconfigure(1, weight=3)
        buttons_frame.columnconfigure(2, weight=3)

        self.start_button = tk.Button(
            buttons_frame,
            text = "Start",
            command = self.start_timer
        )

        self.stop_button = tk.Button(
            buttons_frame,
            text = "Stop",
            command = self.stop_timer
        )

        self.exit_button = tk.Button(
            buttons_frame,
            text = "Exit",
            command = self.quit_app
        )

        self.start_button.grid(row=0, column=0, sticky="ew")
        self.stop_button.grid(row=0, column=1, sticky="ew")
        self.exit_button.grid(row=0, column=2, sticky="ew")

    def build_timer(self, *args):
        timer = tk.Label(
            self.window,
            text = self.timer_text.get(),
            font = ("Helvetica, 30")
        )
        timer.grid(row=1, column=0, sticky='nsew')


    def start_timer(self):

        self.timer_left.set(self.timer_left.get())
        self.running = True
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def quit_app(self):
        window.destroy()

    def build_entry(self, *args):
        #self.timer_left = tk.IntVar()
        e1 = tk.Entry(self.window, textvariable=self.timer_left)
        e1.grid(row=4, columnspan = 3)
        return self.timer_left


    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)


    def go_to_sleep(self, *args):
        if not self.timer_left.get():
        #    print("Going to sleep!")
        #print(self.timer_left.get())
            os.popen('rundll32.exe powrprof.dll, SetSuspendState 0,1,0')

    def update(self):
        time_left = self.timer_left.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.timer_left.set(time_left-1)

        else:
            #minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                #'{:0>2}:{:0>2}'.format(minutes, seconds)
                "No time was set!"
            )

            self.stop_timer()

        self.window.after(1000, self.update)

if __name__ == "__main__":
    window = tk.Tk()
    SleepApp(window)
    window.wm_title("Sleep App")
    window.geometry("400x200")
    window.mainloop()
