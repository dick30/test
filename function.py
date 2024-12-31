import webbrowser
import os


def create_file(filename):
    with open(filename, "w") as f:
        f.write("")


def open_website(url):
    webbrowser.open(url)
