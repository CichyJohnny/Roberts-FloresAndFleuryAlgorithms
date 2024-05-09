class UndirectedFleury:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.am = None

        self.path = []

    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            self.am[a][b] = 1
            self.am[b][a] = 1

    def create_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = 1

    def __eulerian(self, v, start):
        for i in range(self.v):
            if self.am[v][i] == 1:
                self.am[v][i] = 0
                self.am[i][v] = 0

                self.__eulerian(i, start)

        self.path.append(v)

    def find(self):
        start = 0

        self.__eulerian(start, start)
        path = self.path[::-1]

        if path[0] == path[-1] and len(path) == self.e + 1:
            return True, path
        else:
            return False, path


if __name__ == "__main__":
    f = UndirectedFleury()

    # f.create_from_input()
    f.create_from_file()

    EC, Path = f.find()

    if EC:
        print("Eulerian Cycle exists")
        print("Path: ", Path)
    else:
        print("Eulerian Cycle does not exist")
