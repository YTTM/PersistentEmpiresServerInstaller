# Persistent Empires Server Installer

### User guide

**Persistent Empires Server Installer** is a Python script which give you a
user interface and configuration files to simplify the installation of the
persistent empires mod on your server.
This script only copy files from folders to folders.

If you want to install a server, follow theses steps :
1. Create or clean the destination directory.
2. Download **Mount and Blade II: Dedicated Server** using steamcmd.
3. Download **Persistent Empires mod** from workshop using steamcmd or discord.
4. Download Persistent Empires **server license** from discord.
5. Download Persistent Empires **server release** from discord.
6. Download Persistent Empires **server SubModule.xml** from discord.

### Binary release


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
