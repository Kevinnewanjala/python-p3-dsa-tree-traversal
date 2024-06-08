class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None

        nodes_to_visit = [self.root]
        while nodes_to_visit:
            current = nodes_to_visit.pop()
            if current['id'] == id:
                return current
            nodes_to_visit.extend(current.get('children', []))
        return None
