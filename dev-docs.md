# Developer Documentation
run `main.py` to start the complete app

## Building
To build the app run
```shell
pyinstaller --name word-2-pptx --icon=assets/app-icon.ico --onefile --windowed main.py
```

## GitHub release
push a commit to master with a tag 'v*.*.*' if version is 0.1.2 'v0.1.2'

**ui** contains all stuff about the graphical user interface with tkinter.

**word2pptx** contains all stuff about handling the parsing of the word file, to making the powerpoint file. To build the powerpoint, it uses the library [python-pptx](https://github.com/scanny/python-pptx) with the import name `pptx`.