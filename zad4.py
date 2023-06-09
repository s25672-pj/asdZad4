import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = []
    for symbol, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(symbol, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]


def traverse_huffman_tree(node, code, code_dict):
    if node.symbol is not None:
        code_dict[node.symbol] = code
        return

    traverse_huffman_tree(node.left, code + '0', code_dict)
    traverse_huffman_tree(node.right, code + '1', code_dict)


def huffman_encoding(text):
    text = text.replace(" ", "")  # Usunięcie spacji z tekstu
    frequencies = defaultdict(int)
    for symbol in text:
        frequencies[symbol] += 1

    huffman_tree = build_huffman_tree(frequencies)
    code_dict = {}
    traverse_huffman_tree(huffman_tree, '', code_dict)

    encoded_text = [(symbol, code_dict[symbol]) for symbol in text]

    return encoded_text, frequencies, code_dict


def main():
    text = input("Podaj tekst do zakodowania: ")
    encoded_text, frequencies, code_dict = huffman_encoding(text)
    print("Znak\t| Liczba wystąpień\t| Kodowanie")
    print("------------------------------------------")
    for symbol, count in sorted(frequencies.items(), key=lambda x: x[1]):
        code = code_dict[symbol]
        print(f"{symbol}\t| {count}\t\t| {code}")
    encoded_string = ''.join(code for symbol, code in encoded_text)
    print("Zakodowany tekst:", encoded_string)


main()
