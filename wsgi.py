from flask import Flask
from tkinter import *
application = Flask(__name__)

@application.route("/")
def hello():
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.mainloop()
    return "Hello World!"

if __name__ == "__main__":
    application.run()
