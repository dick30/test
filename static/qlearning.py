import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


class FileUploader:
    def __init__(self):
        self.upload_path = "uploads"
        if not os.path.exists(self.upload_path):
            os.makedirs(self.upload_path)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.basename(file_path)
            new_filename = f"{timestamp}_{filename}"
            new_path = os.path.join(self.upload_path, new_filename)

            with open(file_path, "rb") as source:
                with open(new_path, "wb") as target:
                    target.write(source.read())
            return new_path
        return None

    def open_file_location(self, file_path):
        if os.path.exists(file_path):
            os.startfile(os.path.dirname(file_path))


def main():
    root = tk.Tk()
    root.title("檔案上傳系統")

    uploader = FileUploader()
    current_file_path = None

    def handle_upload():
        nonlocal current_file_path
        current_file_path = uploader.upload_file()
        if current_file_path:
            status_label.config(text=f"檔案已上傳至: {current_file_path}")

    def handle_open():
        if current_file_path:
            uploader.open_file_location(current_file_path)

    upload_btn = tk.Button(root, text="上傳檔案", command=handle_upload)
    upload_btn.pack(pady=10)

    open_btn = tk.Button(root, text="開啟檔案位置", command=handle_open)
    open_btn.pack(pady=5)

    status_label = tk.Label(root, text="尚未上傳檔案", wraplength=300)
    status_label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
