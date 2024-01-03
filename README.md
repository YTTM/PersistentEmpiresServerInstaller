# Persistent Empires Server Installer

### Binary release
* [1.0](https://github.com/YTTM/PersistentEmpiresServerInstaller/raw/main/release/PersistentEmpiresServerInstaller.exe)

You don't trust ? No problem, you can build your own binary or execute the script using Python !

### User guide

**Persistent Empires Server Installer** is a Python script which give you a
user interface and configuration files to simplify the installation of the
persistent empires mod on your server.
This script only copy files from folders to folders.

If you want to install a server, follow theses steps :
1. Create the destination directory.
2. Download **Mount and Blade II: Dedicated Server** using steamcmd.
3. Download **Persistent Empires mod** from workshop using steamcmd or discord.
4. Download Persistent Empires **server license** from discord.
5. Download Persistent Empires **server release** from discord.
6. Download Persistent Empires **server SubModule.xml** from discord.
7. Create and fill optional folders
    * ModuleData configuration
    * Bannerlord mission files (.txt)
    * Server starter files (.bat)
    
Check [installer.py](installer.py) for more information about source
and destination folders.

8. Start **Persistent Empires Server Installer**

![image](https://github.com/YTTM/PersistentEmpiresServerInstaller/assets/120769366/7593d2c9-a87a-4881-93db-ee810831e521)

9. Fill the wanted folder (you may also load a configuration file)
10. Press check
    * red : folder do not exist
    * orange : folder do not match file check
    * yellow : folder will be skiped
    * green : folder do match file check
    
![image](https://github.com/YTTM/PersistentEmpiresServerInstaller/assets/120769366/c73bf799-1dd7-4414-b0b4-3ceebf4cfb01)

11. Correct if needed
    
![image](https://github.com/YTTM/PersistentEmpiresServerInstaller/assets/120769366/d66a1ebe-f875-4fbf-94d5-c1e3e5c39675)

12. Press Install

![image](https://github.com/YTTM/PersistentEmpiresServerInstaller/assets/120769366/46302f07-ecac-45f9-b582-4a58ba0de55b)

Congratulation, you are done, you can close **Persistent Empires Server Installer** !

#### Additional options
```
usage: main.py [-h] [--config CONFIG] [--nogui]

optional arguments:
  --config CONFIG.json
  --nogui
```

### Developers

#### Requirements
* Python >= 3.9
* [pygubu](https://github.com/alejandroautalan/pygubu) and [pygubu-designer](https://github.com/alejandroautalan/pygubu-designer)
* [pyinstaller](https://pyinstaller.org/en/stable/)

#### Setup and use venv
```
python -m venv venv
call venv/Scripts/activate.bat

pip install -U pip setuptools wheel
pip install pyinstaller
pip install pygubu pygubu-designer
```

#### Build binary
```
buid.bat
```

#### Start pygubu-designer
```
pygubu-designer
```
