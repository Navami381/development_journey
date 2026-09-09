class Editor:
    def open(self):
        print("editor open method..")

    def execute(self):
        print("execute traditional way python module_name.py")

class Vscode(Editor):
    def open(self):                 #method overriding
        print("open with code .")

vscode_instance=Vscode()
vscode_instance.open()