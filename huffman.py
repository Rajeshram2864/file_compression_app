import heapq, pickle
from collections import Counter
from utils import BitWriter, BitReader


class Node:
    def __init__(self, freq, byte=None, left=None, right=None):
        self.freq = freq
        self.byte = byte
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def _build_tree(self, data):
        freq = Counter(data)
        heap = [Node(f, b) for b, f in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            parent = Node(n1.freq + n2.freq, None, n1, n2)
            heapq.heappush(heap, parent)
        return heap[0]

    def _make_codes(self, root):
        codes = {}

        def generate(node, code):
            if node.byte is not None:
                codes[node.byte] = code or '0'
                return
            generate(node.left, code + '0')
            generate(node.right, code + '1')

        generate(root, '')
        return codes

    def compress(self, in_path, out_path):
        with open(in_path, 'rb') as f:
            data = f.read()
        root = self._build_tree(data)
        codes = self._make_codes(root)
        writer = BitWriter()
        for b in data:
            writer.write_bits(codes[b])
        writer.flush()
        with open(out_path, 'wb') as f:
            pickle.dump((codes, writer.get_bytes()), f)

    def decompress(self, in_path, out_path):
        with open(in_path, 'rb') as f:
            codes, compressed = pickle.load(f)
        reverse = {v: k for k, v in codes.items()}
        reader = BitReader(compressed)
        cur = ''
        result = bytearray()
        while (b := reader.read_bit()) is not None:
            cur += str(b)
            if cur in reverse:
                result.append(reverse[cur])
                cur = ''
        with open(out_path, 'wb') as f:
            f.write(result)
