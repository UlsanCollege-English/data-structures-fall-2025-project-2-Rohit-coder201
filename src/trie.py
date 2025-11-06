class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0.0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
        self.node_count = 1  # count root

    def insert(self, word, freq):
        """Insert or update a word with given frequency."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                self.node_count += 1
            node = node.children[ch]
        if not node.is_end:
            self.word_count += 1
        node.is_end = True
        node.freq = freq

    def contains(self, word):
        """Return True if word exists in the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def remove(self, word):
        """Remove a word if it exists."""
        def _remove(node, w, depth):
            if depth == len(w):
                if not node.is_end:
                    return False
                node.is_end = False
                node.freq = 0
                self.word_count -= 1
                return len(node.children) == 0
            ch = w[depth]
            if ch not in node.children:
                return False
            should_delete = _remove(node.children[ch], w, depth + 1)
            if should_delete:
                del node.children[ch]
                self.node_count -= 1
                return not node.is_end and len(node.children) == 0
            return False

        return _remove(self.root, word, 0)

    def complete(self, prefix, k):
        """Return up to k words starting with prefix, ranked by freq (then lexicographically)."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []

        def dfs(n, path):
            if n.is_end:
                results.append(("".join(path), n.freq))
            for c in n.children:
                dfs(n.children[c], path + [c])

        dfs(node, list(prefix))
        results.sort(key=lambda x: (-x[1], x[0]))
        return [w for w, _ in results[:k]]

    def stats(self):
        """Return simple stats: number of words, height, and nodes."""
        def height(node):
            if not node.children:
                return 1
            return 1 + max(height(child) for child in node.children.values())
        return {
            "words": self.word_count,
            "nodes": self.node_count,
            "height": height(self.root)
        }
