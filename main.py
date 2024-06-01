from tkinter import *
from tkinter import messagebox
import datetime
import pyperclip

month_table = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

types_dict = {
    "Time": "t",
    "Time (long)": "T",
    "Date": "d",
    "Date (long)": "D",
    "Long date with time": "f",
    "Long date with time and day of the week": "F",
    "Relative": "R"
}

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Discord timestamp conventer")
        self.geometry("400x300")
        self.resizable(0, 0)

        current_datetime = datetime.datetime.now()

        self.year = StringVar(self, value=current_datetime.year)
        self.month = StringVar(self, value=month_table[current_datetime.month-1])
        self.day = StringVar(self, value=current_datetime.day)
        self.hour = StringVar(self, value=current_datetime.hour)
        self.minute = StringVar(self, value=current_datetime.minute)
        self.second = StringVar(self, value=current_datetime.second)
        
        self.type = StringVar(self, value="Time")

        self.gui()

        self.mainloop()

    def make_timestamp(self):
        try:
            year = int(self.year.get())
            month = month_table.index(self.month.get()) + 1
            day = int(self.day.get())
            hour = int(self.hour.get())
            minute = int(self.minute.get())
            second = int(self.second.get())
            type = types_dict[self.type.get()]

            result = f"<t:{round(datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp())}:{type}>"

            pyperclip.copy(result)

            messagebox.showinfo("Copied", "Your timestamp was copied successfully!")
        except Exception:
            messagebox.showerror("Wrong input", "Your input is incorrect!")

    def gui(self):
        Label(
            self,
            text="Year",
            anchor="w"
        ).place(x=10, y=10, width=100, height=30)

        Spinbox(
            self,
            textvariable=self.year,
            from_=1970, to=3000,
            justify="left",
        ).place(x=120, y=10, width=270, height=30)

        Label(
            self,
            text="Month",
            anchor="w"
        ).place(x=10, y=50, width=100, height=34)

        OptionMenu(
            self,
            self.month,
            *month_table
        ).place(x=120, y=50, width=270, height=34)

        Label(
            self,
            text="Day",
            anchor="w"
        ).place(x=10, y=94, width=100, height=30)

        Spinbox(
            self,
            textvariable=self.day,
            from_=1, to=31,
            justify="left"
        ).place(x=120, y=94, width=40, height=30)

        Label(
            self,
            text="Time",
            anchor="e"
        ).place(x=180, y=94, width=40, height=30)

        Spinbox(
            self,
            textvariable=self.hour,
            from_=0, to=23,
            justify="left"
        ).place(x=230, y=94, width=40, height=30)

        Label(
            self,
            text=":"
        ).place(x=270, y=94, width=20, height=30)

        Spinbox(
            self,
            textvariable=self.minute,
            from_=0, to=59,
            justify="left"
        ).place(x=290, y=94, width=40, height=30)

        Label(
            self,
            text=":"
        ).place(x=330, y=94, width=20, height=30)

        Spinbox(
            self,
            textvariable=self.second,
            from_=0, to=59,
            justify="left"
        ).place(x=350, y=94, width=40, height=30)

        Label(
            self,
            text="Type",
            anchor="w"
        ).place(x=10, y=134, width=100, height=34)

        OptionMenu(
            self,
            self.type,
            *list(types_dict.keys())
        ).place(x=120, y=134, width=270, height=34)

        Button(
            self,
            text="Copy timestamp",
            command=self.make_timestamp
        ).place(x=10, y=256, width=380, height=34)

if __name__ == "__main__":
    Window()
