from src.trie import Trie
from src.cli import run_cli
from src.io_utils import load_csv


def run_cli(input_text):
    trie = Trie()
    outputs = []
    for line in input_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        if cmd == "quit":
            break
        elif cmd == "load":
            if len(parts) < 2:
                outputs.append("ERR")
                continue
            path = parts[1]
            try:
                for word, score in load_csv(path):
                    trie.insert(word, score)
                outputs.append("OK")
            except Exception:
                outputs.append("ERR")
        elif cmd == "contains":
            word = parts[1]
            outputs.append("YES" if trie.contains(word) else "NO")
        elif cmd == "remove":
            word = parts[1]
            outputs.append("OK" if trie.remove(word) else "MISS")
        elif cmd == "complete":
            prefix, n = parts[1], int(parts[2])
            completions = trie.complete(prefix, n)
            for w, s in completions:
                outputs.append(f"{w},{s}")
        elif cmd == "stats":
            words, height, nodes = trie.stats()
            outputs.append(f"{words},{height},{nodes}")
        else:
            outputs.append("ERR")
    return outputs

if __name__ == "__main__":
    text = sys.stdin.read()
    for line in run_cli(text):
        print(line)
    print("Break time!")
