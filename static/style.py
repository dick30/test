import tkinter as tk


def configure_root(root):
    root.geometry("600x400")  # 設定介面大小
    root.resizable(True, True)  # 允許調整大小


def add_scrollbar(frame):
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")
    return scrollbar
