class BitWriter:
    def __init__(self):
        self.buffer = 0
        self.count = 0
        self.data = bytearray()

    def write_bits(self, bits):
        for bit in bits:
            self.buffer = (self.buffer << 1) | int(bit)
            self.count += 1
            if self.count == 8:
                self.data.append(self.buffer)
                self.buffer = 0
                self.count = 0

    def flush(self):
        if self.count:
            self.buffer <<= (8 - self.count)
            self.data.append(self.buffer)

    def get_bytes(self):
        return bytes(self.data)


class BitReader:
    def __init__(self, data):
        self.data = data
        self.byte_index = 0
        self.bit_index = 0

    def read_bit(self):
        if self.byte_index >= len(self.data):
            return None
        byte = self.data[self.byte_index]
        bit = (byte >> (7 - self.bit_index)) & 1
        self.bit_index += 1
        if self.bit_index == 8:
            self.bit_index = 0
            self.byte_index += 1
        return bit
