import tkinter as tk
from tkinter import filedialog, messagebox, font

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Untitled - Notepad")
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.editmenu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

         # create format menu
        formatmenu = tk.Menu(self.menubar, tearoff=0)
        self.font_family = tk.StringVar(value="Arial")
        self.font_size = tk.IntVar(value=12)
        # formatmenu.add_command(label="Word Wrap", command=WordWrap)
        formatmenu.add_command(label="Font...", command=font)
        self.menubar.add_cascade(label="Format", menu=formatmenu)

        # create view menu
        viewmenu = tk.Menu(self.menubar, tearoff=0)
        # viewmenu.add_command(label="Zoom In", command=self.Zoom)
        # viewmenu.add_command(label="Zoom Out", command=self.zoom_out)
        # viewmenu.add_command(label="Normal Size", command=self.normal_size)
        self.menubar.add_cascade(label="View", menu=viewmenu)

        # create help menu
        helpmenu = tk.Menu(self.menubar, tearoff=0)
        # helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        
        self.master.config(menu=self.menubar)

    def new_file(self):
        self.textarea.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textarea.get("1.0", tk.END))

    def format_file(self):
        file_path = filedialog.askformatfilename()
        if file_path:
            with open(file_path, "w") as format:
                file.write(self.textarea.get("1.0", tk.END))


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
