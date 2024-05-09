class DirectedFleury:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.gm = None

        self.path = []

    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.gm = [[0 for _ in range(self.v)] for _ in range(self.v)]

        ln = [[] for _ in range(self.v)]
        lp = [[] for _ in range(self.v)]
        lb = [[] for _ in range(self.v)]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            ln[a].append(b)
            lp[b].append(a)

        self.create_gm(ln, lp, lb)

    def create_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())

            ln = [[] for _ in range(self.v)]
            lp = [[] for _ in range(self.v)]
            lb = [[] for _ in range(self.v)]

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                ln[a].append(b)
                lp[b].append(a)

        self.create_gm(ln, lp, lb)

    def create_gm(self, ln, lp, lb):
        self.gm = [[0 for _ in range(self.v + 3)] for _ in range(self.v)]

        for i in range(self.v):
            for j in range(self.v):
                if j not in ln[i] and j not in lp[i]:
                    lb[i].append(j)

        for i in range(self.v):
            if not ln[i]:
                ln[i].append(-1)
            if not lp[i]:
                lp[i].append(-1)
            if not lb[i]:
                lb[i].append(-1)
            ln[i].sort()
            lp[i].sort()

        for i in range(self.v):
            self.gm[i][self.v] = ln[i][0]
            self.gm[i][self.v + 1] = lp[i][0]
            self.gm[i][self.v + 2] = lb[i][0]

            num_ln = len(ln[i])
            num_lp = len(lp[i])
            num_lb = len(lb[i])

            for j in range(self.v):
                for k in range(num_ln):
                    if j == ln[i][k]:
                        if k == num_ln - 1:
                            self.gm[i][j] = ln[i][k]
                        else:
                            self.gm[i][j] = ln[i][k + 1]

            for j in range(self.v):
                for k in range(num_lp):
                    if j == lp[i][k]:
                        if k == num_lp - 1:
                            self.gm[i][j] = lp[i][k] + self.e
                        else:
                            self.gm[i][j] = lp[i][k + 1] + self.e

            for j in range(self.v):
                for k in range(num_lb):
                    if j == lb[i][k]:
                        if k == num_lb - 1:
                            self.gm[i][j] = -lb[i][k] - 1
                        else:
                            self.gm[i][j] = -(lb[i][k] + lb[i][k + 1])

    def __eulerian(self, v, start):
        for i in range(self.v):
            if 0 <= self.gm[v][i] <= self.v:
                self.gm[v][i] = -1
                self.gm[i][v] = -1

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
    f = DirectedFleury()

    # f.create_from_input()
    f.create_from_file()

    EC, Path = f.find()

    if EC:
        print("Eulerian Cycle exists")
        print("Path: ", Path)
    else:
        print("Eulerian Cycle does not exist")