class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._dfs(self.root, target_id)

    def _dfs(self, node, target_id):
        if node is None:
            return None

        if node.get('id') == target_id:
            return node

        for child in node.get('children', []):
            found_node = self._dfs(child, target_id)
            if found_node:
                return found_node

        return None
