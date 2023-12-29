import base64
import icon

import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.pathchooserinput import PathChooserInput


class BaseWindow:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.resizable(False, False)
        toplevel1.title("Persistent Empires Server Installer - [14e] Yttrium")
        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, width=200)
        label1 = ttk.Label(frame1)
        label1.configure(padding=5, text='Persistent Empires server license')
        label1.grid(column=0, row=0, sticky="w")
        label2 = ttk.Label(frame1)
        label2.configure(padding=5, text='Bannerlord dedicated server')
        label2.grid(column=0, row=1, sticky="w")
        label3 = ttk.Label(frame1)
        label3.configure(padding=5, text='Persistent Empires mod')
        label3.grid(column=0, row=2, sticky="w")
        label4 = ttk.Label(frame1)
        label4.configure(padding=5, text='SubModule.xml')
        label4.grid(column=0, row=3, sticky="w")
        label5 = ttk.Label(frame1)
        label5.configure(padding=5, text='Server binary release')
        label5.grid(column=0, row=4, sticky="w")
        label6 = ttk.Label(frame1)
        label6.configure(padding=5, text='ModuleData configuration files')
        label6.grid(column=0, row=5, sticky="w")
        label7 = ttk.Label(frame1)
        label7.configure(padding=5, text='Bannerlord mission files (.txt)')
        label7.grid(column=0, row=6, sticky="w")
        label8 = ttk.Label(frame1)
        label8.configure(padding=5, text='Server starters (.bat)')
        label8.grid(column=0, row=7, sticky="w")
        label9 = ttk.Label(frame1)
        label9.configure(padding=5)
        label9.grid(column=0, row=8, sticky="w")
        label10 = ttk.Label(frame1)
        label10.configure(
            justify="right",
            padding=5,
            text='Destination folder')
        label10.grid(column=0, row=9, sticky="w")
        pathchooserinput1 = PathChooserInput(frame1)
        self.pe_server_license = tk.StringVar()
        pathchooserinput1.configure(
            mustexist=True,
            textvariable=self.pe_server_license,
            type="directory")
        pathchooserinput1.grid(column=1, padx=10, row=0)
        pathchooserinput1.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput2 = PathChooserInput(frame1)
        self.bannerlord = tk.StringVar()
        pathchooserinput2.configure(
            mustexist=True,
            textvariable=self.bannerlord,
            type="directory")
        pathchooserinput2.grid(column=1, padx=10, row=1)
        pathchooserinput2.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput3 = PathChooserInput(frame1)
        self.pe = tk.StringVar()
        pathchooserinput3.configure(
            mustexist=True,
            textvariable=self.pe,
            type="directory")
        pathchooserinput3.grid(column=1, padx=10, row=2)
        pathchooserinput3.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput4 = PathChooserInput(frame1)
        self.pe_submodule_file = tk.StringVar()
        pathchooserinput4.configure(
            mustexist=True,
            textvariable=self.pe_submodule_file,
            type="file")
        pathchooserinput4.grid(column=1, padx=10, row=3)
        pathchooserinput4.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput5 = PathChooserInput(frame1)
        self.pe_bin = tk.StringVar()
        pathchooserinput5.configure(
            mustexist=True,
            textvariable=self.pe_bin,
            type="directory")
        pathchooserinput5.grid(column=1, padx=10, row=4)
        pathchooserinput5.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput6 = PathChooserInput(frame1)
        self.pe_config = tk.StringVar()
        pathchooserinput6.configure(
            mustexist=True,
            textvariable=self.pe_config,
            type="directory")
        pathchooserinput6.grid(column=1, padx=10, row=5)
        pathchooserinput6.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput7 = PathChooserInput(frame1)
        self.mission = tk.StringVar()
        pathchooserinput7.configure(
            mustexist=True,
            textvariable=self.mission,
            type="directory")
        pathchooserinput7.grid(column=1, padx=10, row=6)
        pathchooserinput7.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput8 = PathChooserInput(frame1)
        self.starter = tk.StringVar()
        pathchooserinput8.configure(
            mustexist=True,
            textvariable=self.starter,
            type="directory")
        pathchooserinput8.grid(column=1, padx=10, row=7)
        pathchooserinput8.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput9 = PathChooserInput(frame1)
        pathchooserinput9.configure(
            mustexist=True,
            state="disabled",
            type="directory")
        pathchooserinput9.grid(column=1, padx=10, row=8)
        pathchooserinput9.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        pathchooserinput10 = PathChooserInput(frame1)
        self.destination = tk.StringVar()
        pathchooserinput10.configure(
            mustexist=True,
            textvariable=self.destination,
            type="directory")
        pathchooserinput10.grid(column=1, padx=10, row=9)
        pathchooserinput10.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.label_show_1 = ttk.Label(frame1)
        self.label_show_1.configure(padding=10)
        self.label_show_1.grid(column=2, row=0, rowspan=5)
        self.label_show_2 = ttk.Label(frame1)
        self.label_show_2.configure(
            justify="center",
            padding=10,
            text='Persistent Empires Server Installer\n\n[14e] Yttrium\nyttrium@14egaming.com')
        self.label_show_2.grid(column=2, row=5, rowspan=5)
        frame1.pack(side="top")
        frame3 = ttk.Frame(toplevel1)
        frame3.configure(height=200, width=200)
        button11 = ttk.Button(frame3)
        button11.configure(text='Check', width=20)
        button11.grid(column=0, row=0)
        button11.configure(command=self.check)
        button12 = ttk.Button(frame3)
        button12.configure(state="disabled", text='Install', width=20)
        button12.grid(column=1, row=0)
        button12.configure(command=self.install)
        frame3.pack(side="top")

        # Main widget
        self.mainwindow = toplevel1
        # Main menu
        _main_menu = self.create_menu1(self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)

    def run(self):
        self.mainwindow.mainloop()

    def create_menu1(self, master):
        menu1 = tk.Menu(master)
        submenu1 = tk.Menu(menu1, tearoff=False)
        menu1.add(tk.CASCADE, menu=submenu1, label='File')
        submenu1.add("command", command=self.open, label='Open')
        submenu1.add("command", command=self.save, label='Save')
        return menu1

    def path_changed(self, event=None):
        pass

    def check(self):
        pass

    def install(self):
        pass

    def open(self):
        pass

    def save(self):
        pass


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.mainwindow.geometry("+0+0")
        self.mainwindow.wm_iconphoto(True, tk.PhotoImage(data=base64.b64decode(icon.bannerlord)))
        self.icon_pe = tk.PhotoImage(data=base64.b64decode(icon.pe))
        self.label_show_1.configure(image=self.icon_pe)
        self.label_show_1.image = self.icon_pe

    def path_changed(self, event=None):
        pass

    def check(self):
        pass

    def install(self):
        pass

    def open(self):
        pass

    def save(self):
        pass
