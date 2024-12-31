import tkinter as tk
from tkinter import simpledialog
from function import create_file, open_website
from static.style import configure_root, add_scrollbar


def add_file():
    filename = simpledialog.askstring("Input", "Enter the filename:")
    if filename:
        create_file(filename)
        tk.messagebox.showinfo("Success", f"File '{filename}' created successfully.")


def add_website_button():
    url = simpledialog.askstring("Input", "Enter the website URL:")
    if url:
        button = tk.Button(root, text=url, command=lambda: open_website(url))
        button.pack()


root = tk.Tk()
root.title("功能介面")

# 配置介面樣式
configure_root(root)

# 添加滾輪
frame = tk.Frame(root)
frame.pack(side="left", fill="both", expand=True)
scrollbar = add_scrollbar(frame)

add_file_button = tk.Button(frame, text="新增檔案", command=add_file)
add_file_button.pack()

add_website_button = tk.Button(frame, text="新增網站按鈕", command=add_website_button)
add_website_button.pack()

root.mainloop()
