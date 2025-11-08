from huffman import Huffman
from lzw import LZW
import os


class Compressor:
    def __init__(self):
        self.huffman = Huffman()
        self.lzw = LZW()

    def compress(self, file_path: str, algorithm: str):
        base, _ = os.path.splitext(file_path)
        if algorithm == 'Huffman':
            out = base + '.huff'
            self.huffman.compress(file_path, out)
        else:
            out = base + '.lzw'
            self.lzw.compress(file_path, out)
        return out

    def decompress(self, file_path: str, algorithm: str):
        out = file_path + '.decompressed'
        if algorithm == 'Huffman':
            self.huffman.decompress(file_path, out)
        else:
            self.lzw.decompress(file_path, out)
        return out