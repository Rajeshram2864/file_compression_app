import customtkinter as ctk    # pyright: ignore[reportMissingImports]
from tkinter import filedialog, messagebox
import os
from compressor import Compressor


class CompressionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('File Compression Tool')
        self.geometry('500x400')
        self.file_path = None
        self.compressor = Compressor()
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text='Select a File to Compress or Decompress', font=('Segoe UI', 18, 'bold'))
        self.label.pack(pady=20)

        self.file_button = ctk.CTkButton(self, text='Browse File', command=self.browse_file)
        self.file_button.pack(pady=10)

        self.file_label = ctk.CTkLabel(self, text='No file selected', text_color='gray')
        self.file_label.pack(pady=5)

        self.algorithm_menu = ctk.CTkOptionMenu(self, values=['Huffman', 'LZW'])
        self.algorithm_menu.pack(pady=15)

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)
        self.progress.pack(pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=20)

        self.compress_btn = ctk.CTkButton(btn_frame, text='Compress', command=self.compress_file)
        self.compress_btn.grid(row=0, column=0, padx=10)

        self.decompress_btn = ctk.CTkButton(btn_frame, text='Decompress', command=self.decompress_file)
        self.decompress_btn.grid(row=0, column=1, padx=10)

        self.status_label = ctk.CTkLabel(self, text='Status: Idle', text_color='lightgray')
        self.status_label.pack(pady=10)

    def browse_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.file_path = file
            self.file_label.configure(text=os.path.basename(file))

    def compress_file(self):
        if not self.file_path:
            messagebox.showwarning('No file', 'Please select a file.')
            return
        algo = self.algorithm_menu.get()
        try:
            self.status_label.configure(text=f'Compressing using {algo}...')
            self.update_idletasks()
            out = self.compressor.compress(self.file_path, algo)
            self.progress.set(1)
            messagebox.showinfo('Success', f'Compressed file saved as: {out}')
            self.status_label.configure(text='Compression completed ✅')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def decompress_file(self):
        if not self.file_path:
            messagebox.showwarning('No file', 'Please select a file.')
            return
        algo = self.algorithm_menu.get()
        try:
            self.status_label.configure(text=f'Decompressing using {algo}...')
            self.update_idletasks()
            out = self.compressor.decompress(self.file_path, algo)
            self.progress.set(1)
            messagebox.showinfo('Success', f'Decompressed file saved as: {out}')
            self.status_label.configure(text='Decompression completed ✅')
        except Exception as e:
            messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    app = CompressionApp()
    app.mainloop()
