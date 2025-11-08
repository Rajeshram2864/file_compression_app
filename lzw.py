import pickle


class LZW:
    def compress(self, in_path, out_path):
        with open(in_path, 'rb') as f:
            data = f.read()
        dict_size = 256
        dictionary = {bytes([i]): i for i in range(dict_size)}
        w = b''
        result = []
        for b in data:
            wc = w + bytes([b])
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = bytes([b])
        if w:
            result.append(dictionary[w])
        with open(out_path, 'wb') as f:
            pickle.dump(result, f)

    def decompress(self, in_path, out_path):
        with open(in_path, 'rb') as f:
            compressed = pickle.load(f)
        dict_size = 256
        dictionary = {i: bytes([i]) for i in range(dict_size)}
        w = bytes([compressed.pop(0)])
        result = bytearray(w)
        for k in compressed:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[:1]
            else:
                raise ValueError('Bad code')
            result.extend(entry)
            dictionary[dict_size] = w + entry[:1]
            dict_size += 1
            w = entry
        with open(out_path, 'wb') as f:
            f.write(result)
