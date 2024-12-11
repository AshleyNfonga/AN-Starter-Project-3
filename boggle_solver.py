
"""
Ashley Nfonga
SID: @03081115
"""

class Boggle:
    def __init__(self, grid, dictionary):
        if not self.is_valid_grid(grid):
            self.grid = []
            self.rows = 0
            self.cols = 0
        else:
            self.setGrid(grid)
            self.rows = len(self.grid)
            self.cols = len(self.grid[0]) if self.rows > 0 else 0
            self.setDictionary(dictionary)
            self.prefixes = self.build_prefixes(self.dictionary)
            self.solution = set()

    def is_valid_grid(self, grid):
        if not grid or not all(grid):
            return False
        return len(set(len(row) for row in grid)) == 1

    def setGrid(self, grid):
        self.grid = [[ele.upper() for ele in row] for row in grid]

    def setDictionary(self, dictionary):
        self.dictionary = set(word.upper() for word in dictionary)

    def build_prefixes(self, dictionary):
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def dfs(self, i, j, visited, path):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or visited[i][j]:
            return

        path += self.grid[i][j]
        extra_chars = 0

        if self.grid[i][j] == 'Q':
            path += 'U'
            extra_chars += 1
        elif self.grid[i][j] == 'S' and (len(path) < 2 or path[-2] != 'Q'):
            path += 'T'
            extra_chars += 1

        if path not in self.prefixes and path not in self.dictionary:
            return

        if len(path) >= 3 and path in self.dictionary:
            self.solution.add(path)

        visited[i][j] = True

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di != 0 or dj != 0:
                    self.dfs(i + di, j + dj, visited, path)

        visited[i][j] = False

    def getSolution(self):
        self.solution = set()
        if self.rows == 0 or self.cols == 0:
            return []

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, visited, "")

        return sorted(list(self.solution))

def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
