def stats(self):
    """Return (word_count, height, node_count) as integers."""
    def count_nodes(node):
        count = 1
        for child in node.children.values():
            count += count_nodes(child)
        return count

    def get_height(node):
        if not node.children:
            return 1
        return 1 + max(get_height(child) for child in node.children.values())

    words = getattr(self, "word_count", 0)
    height = get_height(self.root)
    nodes = count_nodes(self.root)
    return (words, height, nodes)
