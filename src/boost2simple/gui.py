import tkinter as tk
import webbrowser
from ctypes import windll
from tkinter.filedialog import askdirectory
from tkinter.font import Font

from boost2simple import converter

primary_light = "#F7F7FF"
primary_dark = "#545E75"
intro_text = "Ideally, use a directory for importing " \
             "which has no other contents " \
             "than a folder for each exported BoostNote workspace. " \
             "See instructions at: "
repo_url = "https://github.com/RWitak/boost2simple#boost2simple"


def visit_repo():
    webbrowser.open(repo_url)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background=primary_light)
        self.master = master
        self.pack(ipadx=8, ipady=8)
        self.create_widgets()
        self.input_dir = "."
        self.output_dir = "."
        self.markdown = True
        self.title = True

    def convert(self):
        converter.convert(self.input_dir, self.output_dir)

    def set_input_dir(self):
        self.input_dir = askdirectory(title="Select BoostNote directory")

    def set_output_dir(self):
        self.output_dir = askdirectory(title="Select export directory")

    def create_widgets(self):
        self.winfo_toplevel().title("boost2simple - the BoostNote->SimpleNote converter")

        intro_frame = tk.Frame(self, bg=primary_light)
        intro_frame.pack(side="top", padx=8, pady=16)

        manual = tk.Label(intro_frame,
                         text=intro_text,
                         wraplength=400,
                         bg=primary_light)
        manual.pack(side="top", fill=tk.X, padx=8, pady=8)
        manual_font = Font(manual, manual.cget("font"))
        manual_font.configure(slant="italic")
        manual.configure(font=manual_font)

        link = tk.Button(intro_frame,
                         bg=primary_light, fg="blue",
                         text=repo_url,
                         command=visit_repo,
                         underline=True)
        link.pack(side="top")
        link_font = Font(link, link.cget("font"))
        link_font.configure(underline=True)
        link.configure(font=link_font)

        input_frame = tk.Frame(self, bg=primary_light)
        input_frame.pack(side="top", fill=tk.X, padx=8, pady=8)

        input_label = tk.Label(master=input_frame, bg=primary_light)
        input_label["text"] = "Select BoostNote directory"
        input_label.pack(side="left")

        input_dir_btn = tk.Button(master=input_frame, bg=primary_dark, fg=primary_light)
        input_dir_btn["text"] = "..."
        input_dir_btn["command"] = self.set_input_dir
        input_dir_btn.pack(side="right")

        output_frame = tk.Frame(self, bg=primary_light)
        output_frame.pack(side="top", fill=tk.X, padx=8, pady=8)

        output_label = tk.Label(output_frame, bg=primary_light)
        output_label["text"] = "Select export directory"
        output_label.pack(side="left", fill=tk.X)

        output_dir_btn = tk.Button(output_frame, bg=primary_dark, fg=primary_light)
        output_dir_btn["text"] = "..."
        output_dir_btn["command"] = self.set_output_dir
        output_dir_btn.pack(side="right")

        checkbox_frame = tk.Frame(self, bg=primary_light)
        checkbox_frame.pack(side="top")

        markdown_toggle = tk.Checkbutton(master=checkbox_frame,
                                         text="use Markdown",
                                         onvalue=True,
                                         offvalue=False,
                                         bg=primary_light)
        markdown_toggle.select()
        markdown_toggle.pack(side="left")
        title_toggle = tk.Checkbutton(master=checkbox_frame,
                                      text="include original title",
                                      onvalue=True,
                                      offvalue=False,
                                      bg=primary_light)
        title_toggle.select()
        title_toggle.pack(side="left")

        convert_btn = tk.Button(self,
                                background=primary_dark,
                                foreground=primary_light,
                                font=("Helvetica", 12, "normal"))
        convert_btn["text"] = "Convert"
        convert_btn["command"] = self.convert

        convert_btn.pack(side="top", padx=8, pady=8, ipadx=4, ipady=0)

        self.quit = tk.Button(self,
                              text="Exit",
                              bg="#C03221",
                              fg=primary_light,
                              command=self.master.destroy)
        self.quit.pack(side="top", ipadx=4, ipady=0)


windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
