pyinstaller --specpath ./release/spec --distpath ./release --workpath ./release --icon=../../icon/bannerlord_icon.ico --onefile main.py
COPY .\release\main.exe .\release\PersistentEmpiresServerInstaller.exe
