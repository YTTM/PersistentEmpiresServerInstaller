import base64

import check
import icon

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from pygubu.widgets.pathchooserinput import PathChooserInput


class BaseWindow:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.resizable(False, False)
        toplevel1.title("Persistent Empires Server Installer - [14e] Yttrium")
        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, width=200)
        self.label_pe_server_license = ttk.Label(frame1)
        self.label_pe_server_license.configure(
            padding=5, text='Persistent Empires server license', width=30)
        self.label_pe_server_license.grid(column=0, row=0, sticky="w")
        self.label_bannerlord = ttk.Label(frame1)
        self.label_bannerlord.configure(
            padding=5, text='Bannerlord dedicated server', width=30)
        self.label_bannerlord.grid(column=0, row=1, sticky="w")
        self.label_pe = ttk.Label(frame1)
        self.label_pe.configure(
            padding=5,
            text='Persistent Empires mod',
            width=30)
        self.label_pe.grid(column=0, row=2, sticky="w")
        self.label_pe_submodule_file = ttk.Label(frame1)
        self.label_pe_submodule_file.configure(
            padding=5, text='SubModule.xml', width=30)
        self.label_pe_submodule_file.grid(column=0, row=3, sticky="w")
        self.label_pe_bin = ttk.Label(frame1)
        self.label_pe_bin.configure(
            padding=5, text='Server binary release', width=30)
        self.label_pe_bin.grid(column=0, row=4, sticky="w")
        self.label_pe_config = ttk.Label(frame1)
        self.label_pe_config.configure(
            padding=5, text='ModuleData configuration files', width=30)
        self.label_pe_config.grid(column=0, row=5, sticky="w")
        self.label_mission = ttk.Label(frame1)
        self.label_mission.configure(
            padding=5, text='Bannerlord mission files (.txt)', width=30)
        self.label_mission.grid(column=0, row=6, sticky="w")
        self.label_starter = ttk.Label(frame1)
        self.label_starter.configure(
            padding=5, text='Server starters (.bat)', width=30)
        self.label_starter.grid(column=0, row=7, sticky="w")
        label9 = ttk.Label(frame1)
        label9.configure(padding=5, width=30)
        label9.grid(column=0, row=8, sticky="w")
        self.label_destination = ttk.Label(frame1)
        self.label_destination.configure(
            justify="right",
            padding=5,
            text='Destination folder',
            width=30)
        self.label_destination.grid(column=0, row=9, sticky="w")
        self.path_pe_server_license = PathChooserInput(frame1)
        self.pe_server_license = tk.StringVar()
        self.path_pe_server_license.configure(
            mustexist=True,
            textvariable=self.pe_server_license,
            type="directory")
        self.path_pe_server_license.grid(column=1, padx=10, row=0)
        self.path_pe_server_license.bind(
            "<<PathChooserPathChanged>>", self.path_changed, add="")
        self.path_bannerlord = PathChooserInput(frame1)
        self.bannerlord = tk.StringVar()
        self.path_bannerlord.configure(
            mustexist=True,
            textvariable=self.bannerlord,
            type="directory")
        self.path_bannerlord.grid(column=1, padx=10, row=1)
        self.path_bannerlord.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.path_pe = PathChooserInput(frame1)
        self.pe = tk.StringVar()
        self.path_pe.configure(
            mustexist=True,
            textvariable=self.pe,
            type="directory")
        self.path_pe.grid(column=1, padx=10, row=2)
        self.path_pe.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.path_pe_submodule_file = PathChooserInput(frame1)
        self.pe_submodule_file = tk.StringVar()
        self.path_pe_submodule_file.configure(
            mustexist=True, textvariable=self.pe_submodule_file, type="file")
        self.path_pe_submodule_file.grid(column=1, padx=10, row=3)
        self.path_pe_submodule_file.bind(
            "<<PathChooserPathChanged>>", self.path_changed, add="")
        self.path_pe_bin = PathChooserInput(frame1)
        self.pe_bin = tk.StringVar()
        self.path_pe_bin.configure(
            mustexist=True,
            textvariable=self.pe_bin,
            type="directory")
        self.path_pe_bin.grid(column=1, padx=10, row=4)
        self.path_pe_bin.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.path_pe_config = PathChooserInput(frame1)
        self.pe_config = tk.StringVar()
        self.path_pe_config.configure(
            mustexist=True,
            textvariable=self.pe_config,
            type="directory")
        self.path_pe_config.grid(column=1, padx=10, row=5)
        self.path_pe_config.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.path_mission = PathChooserInput(frame1)
        self.mission = tk.StringVar()
        self.path_mission.configure(
            mustexist=True,
            textvariable=self.mission,
            type="directory")
        self.path_mission.grid(column=1, padx=10, row=6)
        self.path_mission.bind(
            "<<PathChooserPathChanged>>",
            self.path_changed,
            add="")
        self.path_starter = PathChooserInput(frame1)
        self.starter = tk.StringVar()
        self.path_starter.configure(
            mustexist=True,
            textvariable=self.starter,
            type="directory")
        self.path_starter.grid(column=1, padx=10, row=7)
        self.path_starter.bind(
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
        self.path_destination = PathChooserInput(frame1)
        self.destination = tk.StringVar()
        self.path_destination.configure(
            mustexist=True,
            textvariable=self.destination,
            type="directory")
        self.path_destination.grid(column=1, padx=10, row=9)
        self.path_destination.bind(
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
        self.button_check = ttk.Button(frame3)
        self.button_check.configure(text='Check', width=20)
        self.button_check.grid(column=0, row=0)
        self.button_check.configure(command=self.check)
        self.button_install = ttk.Button(frame3)
        self.button_install.configure(
            state="disabled", text='Install', width=20)
        self.button_install.grid(column=1, row=0)
        self.button_install.configure(command=self.install)
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
    def __init__(self, config=None):
        super().__init__()

        self.mainwindow.geometry('+0+0')
        self.mainwindow.wm_iconphoto(True, tk.PhotoImage(data=base64.b64decode(icon.bannerlord)))
        self.icon_pe = tk.PhotoImage(data=base64.b64decode(icon.pe))
        self.label_show_1.configure(image=self.icon_pe)
        self.label_show_1.image = self.icon_pe

        self.config = dict()
        if config is not None:
            self.load_config(config)
        else:
            self.path_changed()

    def load_config(self, config):
        if not all(check.configuration(config)):
            tk.messagebox.showerror('Load configuration file', 'Invalid configuration')
        else:
            emptyIfNone = lambda a: '' if a is None else a
            self.config = config
            self.pe_server_license.set(emptyIfNone(config['pe_server_license']))
            self.bannerlord.set(emptyIfNone(config['bannerlord']))
            self.pe.set(emptyIfNone(config['pe']))
            self.pe_submodule_file.set(emptyIfNone(config['pe_submodule_file']))
            self.pe_bin.set(emptyIfNone(config['pe_bin']))
            self.pe_config.set(emptyIfNone(config['pe_config']))
            self.mission.set(emptyIfNone(config['mission']))
            self.starter.set(emptyIfNone(config['starter']))
            self.destination.set(emptyIfNone(config['destination']))

    def path_changed(self, event=None):
        self.button_install['state'] = 'disabled'

        noneIfEmpty = lambda a : None if len(a) == 0 else a
        self.config['pe_server_license'] = noneIfEmpty(self.pe_server_license.get())
        self.config['bannerlord'] = noneIfEmpty(self.bannerlord.get())
        self.config['pe'] = noneIfEmpty(self.pe.get())
        self.config['pe_submodule_file'] = noneIfEmpty(self.pe_submodule_file.get())
        self.config['pe_bin'] = noneIfEmpty(self.pe_bin.get())
        self.config['pe_config'] = noneIfEmpty(self.pe_config.get())
        self.config['mission'] = noneIfEmpty(self.mission.get())
        self.config['starter'] = noneIfEmpty(self.starter.get())
        self.config['destination'] = noneIfEmpty(self.destination.get())

        if event.widget == self.path_pe_server_license:
            self.label_pe_server_license.config({'background': 'gray94'})
        elif event.widget == self.path_bannerlord:
            self.label_bannerlord.config({'background': 'gray94'})
        elif event.widget == self.path_pe:
            self.label_pe.config({'background': 'gray94'})
        elif event.widget == self.path_pe_submodule_file:
            self.label_pe_submodule_file.config({'background': 'gray94'})
        elif event.widget == self.path_pe_bin:
            self.label_pe_bin.config({'background': 'gray94'})
        elif event.widget == self.path_pe_config:
            self.label_pe_config.config({'background': 'gray94'})
        elif event.widget == self.path_mission:
            self.label_mission.config({'background': 'gray94'})
        elif event.widget == self.path_starter:
            self.label_starter.config({'background': 'gray94'})
        elif event.widget == self.path_destination:
            self.label_destination.config({'background': 'gray94'})

    def check(self):
        if not all(check.configuration(self.config)):
            tk.messagebox.showerror('Check', 'Invalid configuration')
            return

        check_flags = check.paths(self.config)

        colorFromCheck = lambda a: 'lightgreen' if a is True else ('red' if a is False else
                                                                   ('orange' if a == 'exists' else 'yellow'))

        self.label_pe_server_license.config({'background': colorFromCheck(check_flags[0])})
        self.label_bannerlord.config({'background': colorFromCheck(check_flags[1])})
        self.label_pe.config({'background': colorFromCheck(check_flags[2])})
        self.label_pe_submodule_file.config({'background': colorFromCheck(check_flags[3])})
        self.label_pe_bin.config({'background': colorFromCheck(check_flags[4])})
        self.label_pe_config.config({'background': colorFromCheck(check_flags[5])})
        self.label_mission.config({'background': colorFromCheck(check_flags[6])})
        self.label_starter.config({'background': colorFromCheck(check_flags[7])})
        self.label_destination.config({'background': colorFromCheck(check_flags[8])})
        self.button_install['state'] = 'enable'

    def install(self):
        pass

    def open(self):
        pass

    def save(self):
        pass
