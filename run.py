import os
from terminal import mainterminal

class Main:
    def __init__(self):
        print('Welcome!')
        self.terminal = mainterminal()
        self.path = os.getcwd()
        self.prompt = ""

    def check(self):
        if not os.path.exists(self.path + "/download"):
            os.makedirs(self.path + "/download")

    def run(self):
        self.terminal.loop()
        self.check()


app = Main()
app.run()