from tkinter import *
from tkinter import messagebox
from os import system
from tkinter.filedialog import *
import tkinter.scrolledtext as tks
app = Tk()

darkgray = "#2F2F2F"
darkblue = "#344D7C"

app.geometry("1280x720")
app.title("PyEditor 1.0")
system("title PyEditor Console")

print("""* This is PyEditor Console. If you click the [Run] button,
The program will be executed in this console. *\n""")

def savefile():
    try:
        ftitle = asksaveasfilename(defaultextension=".py", title=" Save", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(ftitle, "w", encoding="utf-8") as f:
            f.write(ent.get("1.0", "end"))
        messagebox.showinfo(title="Information", message=f"Sucessfuly saved as \"{ftitle}\"!")
    except Exception as e:
        messagebox.showerror(" Error", f"Cannot save file as {ftitle}. Error code: \"{e}\"")

def openfile():
    try:
        open_file = askopenfilename(defaultextension=".py", title=" Open", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")))
        global of
        of = open_file
        with open(open_file, "r", encoding="utf-8") as f:
            fr = f.readlines()
            ent.delete(1.0, "end")
            for i in fr:
                ent.insert("end", i)
    except Exception as e:
        messagebox.showerror(" Error", f"Cannot open file. Error code: \"{e}\"")

def save():
    try:
        with open(of, "w", encoding="utf-8") as f:
            f.write(ent.get("1.0", "end"))
        
        messagebox.showinfo(title="Information", message="Sucessfuly saved!")
    except Exception as e:
        messagebox.showerror(" Error", f"Cannot save file. Error code: \"{e}\"")

def run():
    exec(ent.get("1.0", "end"))

app.config(bg = darkblue)
app.option_add("*Font", "Consolas 16")

txt1 = Button(app, text="Open", font=('', 10), bg=darkblue, fg="white", relief="flat", command=openfile)
txt1.place(x=25, y=12)

txt2 = Button(app, text="Save as..", font=('', 10), bg=darkblue, fg="white", relief="flat", command=savefile)
txt2.place(x=75, y=12)

txt4 = Button(app, text="Save", font=('', 10), bg=darkblue, fg="white", relief="flat", command=save)
txt4.place(x=150, y=12)

txt3 = Button(app, text="Run", font=('', 10), bg=darkblue, fg="white", relief="flat", command=run)
txt3.place(x=205, y=12)

ent = Text(app, fg="white", bg=darkgray, relief="flat", insertbackground="white", height=100, width=app.winfo_screenwidth())
ent.pack(side="left", padx=(30, 0), pady = (45, 0))

ent.insert("end", "# Write code in here!")

app.mainloop()
