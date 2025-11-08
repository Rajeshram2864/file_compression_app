
# 🗜️ File Compression App (Python GUI)

A modern, cross-platform **File Compression & Decompression Tool** built in **Python** with a beautiful **CustomTkinter GUI**.  
Supports two classic **lossless compression algorithms** — **Huffman Coding** and **LZW (Lempel–Ziv–Welch)** — to reduce file size without losing any data.

---

## 🚀 Features

- 🧠 **Two compression algorithms** — Huffman & LZW  
- 🖥 **User-friendly GUI** with progress bar and dark/light theme  
- 💾 **Compress & decompress any file type** (text, code, data, etc.)  
- 📊 Displays compression ratio & file size  
- 🧰 Cross-platform (Windows, macOS, Linux)  
- 🧩 Modular and OOP-based code structure  
- 🎓 Great for learning data compression or demonstrating algorithm design

---

## 🏗️ Project Structure

file_compression_app
│

├── main.py # GUI entry point

├── compressor.py # Manager class for Huffman and LZW

├── huffman.py # Huffman compression & decompression algorithm

├── lzw.py # LZW (Lempel–Ziv–Welch) compression & decompression algorithm

├── utils.py # Helper classes for bit-level I/O and file utilities

├── requirements.txt # Project dependencies



---

## ⚙️ Installation & Setup
### 1️⃣ Clone the repository

git clone https://github.com/Rajeshram2864/file_compression_app.git

cd file_compression_app


### 2️⃣ Create a virtual environment
🪟 On Windows:
python -m venv venv
venv\Scripts\activate


🐧 On macOS / Linux:
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the app
python main.py

🧠 Algorithms Used
🔹 Huffman Coding

Builds a binary tree based on symbol frequencies.

Assigns shorter codes to frequent symbols and longer codes to rare ones.

Best for text files and symbol-based compression.

🔹 LZW (Lempel–Ziv–Welch)

Dictionary-based algorithm that replaces repeated patterns with codes.

Works well on structured or repetitive data like JSON, XML, and source code.

## 📂 Supported File Types

| File Type | Extensions | Compression Efficiency | Recommended Algorithm |
|------------|-------------|------------------------|-----------------------|
| **Text Files** | `.txt`, `.csv`, `.json`, `.xml`, `.html`, `.log` | 🔥 Excellent (40–80%) | Huffman / LZW |
| **Source Code** | `.py`, `.c`, `.cpp`, `.js`, `.java`, `.sql` | ⚡ Good (30–70%) | Huffman |
| **Data Files** | `.json`, `.xml`, `.yaml` | ⚡ Good (20–60%) | LZW |
| **Documents** | `.pdf`, `.docx`, `.xlsx`, `.pptx` | 🟡 Low (already compressed) | Either |
| **Images** | `.png`, `.jpg`, `.jpeg`, `.gif` | 🔴 Minimal or none | Not recommended |
| **Audio / Video** | `.mp3`, `.mp4`, `.wav`, `.avi` | 🔴 None | Not recommended |
| **Archives / Executables** | `.zip`, `.rar`, `.7z`, `.iso`, `.exe` | 🔴 None | Not recommended |

✅ **Works on any binary file**  
🔒 **Lossless:** The original data is perfectly restored on decompression

---

## 📊 Example Compression Ratios

| File Type | Original Size | Compressed Size | Savings |
|------------|----------------|------------------|----------|
| `text.txt` | 50 KB | 15 KB | 🔥 70% |
| `source.py` | 10 KB | 4 KB | ⚡ 60% |
| `data.json` | 100 KB | 45 KB | ⚡ 55% |
| `photo.jpg` | 2 MB | 1.98 MB | 🧊 <1% |

---

## 🧩 GUI Overview

| Feature | Description |
|----------|--------------|
| 🖱️ **File Selector** | Browse and choose any file from your system |
| 🧠 **Algorithm Selector** | Choose between **Huffman** or **LZW** compression |
| ⚙️ **Compress Button** | Starts compression of the selected file |
| 🔄 **Decompress Button** | Restores original file from compressed data |
| 📊 **Progress Bar** | Displays real-time compression/decompression progress |
| 📁 **Output File Info** | Shows compressed file size and compression ratio |
| 💬 **Status Log** | Displays detailed step-by-step process messages |
| 🎨 **Modern GUI** | Built with **CustomTkinter** (dark & light theme support) |
| 💾 **Cross-Platform** | Works on Windows, macOS, and Linux |

---

