class UndirectedRobertsFlores:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.am = None

        self.current_path = []
        self.path = []
        self.visited = 0

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

    def __hamiltonian(self, v, start):
        self.current_path[v] = True
        self.visited += 1

        for i in range(self.v):
            if self.am[v][i] == 1:
                if i == start and self.visited == self.v:
                    self.path.append(v)
                    return True

                if not self.current_path[i]:
                    if self.__hamiltonian(i, start):
                        self.path.append(v)
                        return True

        self.current_path[v] = False
        self.visited -= 1

        return False

    def find(self):
        self.current_path = [False] * self.v
        start = 0
        self.path.append(start)

        HCycle = self.__hamiltonian(start, start)
        path = self.path[::-1]

        return HCycle, path


if __name__ == "__main__":
    rf = UndirectedRobertsFlores()

    # rf.create_from_input()
    rf.create_from_file()

    HC, Path = rf.find()

    if HC:
        print("Hamiltonian Cycle exists")
        print("Path: ", Path)
    else:
        print("Hamiltonian Cycle does not exist")
