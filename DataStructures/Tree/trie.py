# TAKEN FROM SHUBHADEEP ROYCHOWDHURY
# https://tinyurl.com/trie-py
from typing import Tuple
class Trie():
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
    

def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = Trie(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                
                char_not_found = False
                
                node = child
                break
    
        if char_not_found:
            return False, 0
    return True, node.counter


myTrie = Trie('*')

add(myTrie, 'test')
add(myTrie, 'bull')
add(myTrie, 'testing')


print(find_prefix(myTrie, 'te'))
print(find_prefix(myTrie, 'testi'))
print(find_prefix(myTrie, 'bu'))
print(find_prefix(myTrie, 'hello'))
