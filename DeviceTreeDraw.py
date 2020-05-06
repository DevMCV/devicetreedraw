import sys
from anytree import Node, RenderTree, AsciiStyle


class DeviceTreeDraw():
    def draw_tree(self, tree):
        for prefix, _, node in RenderTree(tree, style=AsciiStyle()):
            print("%s%s" % (prefix.replace('+', '`'), node.name))
            
    def create(self, root_file):
        tree = self.tree_walker(root_file)
        self.draw_tree(tree)
        
    def tree_walker(self, file_name):
        root = self.read_file(file_name)
        if root is None:
            return None
        root_node = Node(file_name)
        for line in root:
            if '#include' in line:
                subfile_name = self.replace_all(line, {'#include ':'', '"':''})
                sub_node = self.tree_walker(subfile_name)
                if sub_node is not None:
                    sub_node.parent = root_node
                else:
                    Node(subfile_name, root_node)
        return root_node
    
    def replace_all(self, string, rep):
        for old, new in rep.items():
            string = string.replace(old, new)
        return string
    
    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as fp:
                lines = [line.rstrip() for line in fp]
            return lines
        except:
            return None


if __name__ == '__main__':
    dtd = DeviceTreeDraw()
    dtd.create(sys.argv[1])

