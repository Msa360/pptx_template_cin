# Developer Documentation
run `main.py` to start the complete app

## Building
To build the app as an executable for production:
```shell
pyinstaller --name word-2-pptx --icon=assets/app-icon.ico --onefile --windowed main.py
```

## GitHub release
steps to do once ready to release new version:
- update the version in [readme](README.md) 
- commit only this change, and the commit message will be the release description
- tag this commit with `git tag <version>` with the right version number
- do `git push` and `git push origin <version>`


Pushing a tag to master with the form 'vX.X.X' will trigger a release action, if version is 0.1.2, then tag it as 'v0.1.2'. GitHub Actions will make a windows exe with [pyinstaller](https://pyinstaller.org/en/stable/) and include it in the release assets.

## Architecture
**ui** contains all stuff about the graphical user interface with tkinter.

**word2pptx** contains all stuff about handling the parsing of the word file, to making the powerpoint file. To build the powerpoint, it uses the library [python-pptx](https://github.com/scanny/python-pptx) with the import name `pptx`.