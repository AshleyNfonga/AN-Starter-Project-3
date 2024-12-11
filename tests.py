import re


class TrieNode:
   def __init__(self):
       self.children = {}
       self.is_end_of_word = False


class Trie:
   def __init__(self):
       self.root = TrieNode()

   def insert(self, word):
       node = self.root
       for char in word:
           if char not in node.children:
               node.children[char] = TrieNode()
           node = node.children[char]
       node.is_end_of_word = True

   def starts_with(self, prefix):
       node = self.root
       for char in prefix:
           if char not in node.children:
               return False
           node = node.children[char]
       return True

   def is_word(self, word):
       node = self.root
       for char in word:
           if char not in node.children:
               return False
           node = node.children[char]
       return node.is_end_of_word


class Boggle:
   def __init__(self, grid, dictionary):
       self.grid = [[c.upper() for c in row] for row in grid]
       self.rows = len(grid)
       self.cols = len(grid[0])
       self.found_words = set()
       self.trie = Trie()
       for word in dictionary:
           self.trie.insert(word.upper())  # Insert words in uppercase

   def find_words(self):
       for i in range(self.rows):
           for j in range(self.cols):
               self._dfs(i, j, self.grid[i][j], {(i, j)})

   def _dfs(self, x, y, path, visited):
       if not self.trie.starts_with(path):
           return

       if (len(path) >= 3
               and self.trie.is_word(path)
               and not path.endswith(("Q", "S"))):
           self.found_words.add(path)

       directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                     (-1, -1), (-1, 1), (1, -1), (1, 1)]

       for dx, dy in directions:
           new_x, new_y = x + dx, y + dy
           if (0 <= new_x < self.rows and
                   0 <= new_y < self.cols and
                   (new_x, new_y) not in visited):

               new_char = self.grid[new_x][new_y]
               next_path = path + new_char
               self._dfs(new_x, new_y, next_path, visited | {(new_x, new_y)})

   def getSolution(self):
       self.find_words()
       return sorted(list(self.found_words))


def main():
   grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
           ["G", "Z", "QU", "R"], ["O", "N", "T", "A"]]
   dictionary = ["art", "ego", "gent", "get", "net", "new",
                 "newt", "prat", "pry", "qua", "quart",
                 "quartz", "rat", "tar", "tarp", "ten",
                 "went", "wet", "arty", "rhr", "not", "quar"]
   mygame = Boggle(grid, dictionary)
   print(mygame.getSolution())


if __name__ == "__main__":
   main()

