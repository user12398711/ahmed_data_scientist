# DFS PRAC 1
graph = {
  '5' : ['3','7'],
  '3' : ['2','4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
visited = set()
dfs(visited, graph, '5')


# BFS PRAC 2
graph = {
  '5' : ['3','7'],
  '3' : ['2','4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print (m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
visited = []
queue = []
bfs(visited, graph, '5')
print()


# MINMAX and Alpha Beta Pruning
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
pruned = 0
def minmax(pos, depth, max_player):
    if depth == 0:
        return pos[0]

    if max_player:
        max_eval = -100
        for child in pos:
            max_eval = max(max_eval, minmax(child, depth-1, False))
        return max_eval
    else:
        max_eval = 100
        for child in pos:
            max_eval = min(max_eval, minmax(child, depth-1, True))
        return max_eval

def minmax_ab(pos, depth, max_player, alpha=-100, beta=100):
    global pruned
    if depth == 0:
        return pos[0]

    if max_player:
        max_eval = -100
        for child in pos:
            node_eval = minmax_ab(child, depth-1, False, alpha, beta)
            max_eval = max(max_eval, node_eval)
            alpha = max(alpha, node_eval)
            if beta <= alpha:
                pruned += 1
                break
        return max_eval
    else:
        min_eval = 100
        for child in pos:
            node_eval = minmax_ab(child, depth-1, True, alpha, beta)
            min_eval = min(min_eval, node_eval)
            beta = min(beta, node_eval)
            if beta <= alpha:
                pruned += 1
                break
        return min_eval

print(f"MinMax {minmax(tree, 2, True)}")
print(f"MinMax With AB Pruning {minmax_ab(tree, 2, True)}, Pruned {pruned}")


# TIC TAC TOE
class TicTacToe:
    player_moves_1 = 0
    player_moves_2 = 0
    player_key_1 = "X"
    player_key_2 = "O"
    matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __init__(self) -> None:
        pass

    def valid(self):
        # Verticle
        for indx in [0, 3, 6]:
            if (self.matrix[indx] == self.matrix[indx + 1] and self.matrix[indx + 1] == self.matrix[indx + 2] and self.matrix[indx] != ' '):
                win = self.matrix[indx]
                if win == "X":
                    print("Win Player X")
                    return True
                else:
                    print("Win Player O")
                    return True

        # Horizontal
        for indx in [0, 1, 2]:
            if (self.matrix[indx] == self.matrix[indx + 3] and self.matrix[indx + 3] == self.matrix[indx + 6] and self.matrix[indx] != ' '):
                win = self.matrix[indx]
                if win == "X":
                    print("Win Player X")
                    return True
                else:
                    print("Win Player O")
                    return True

        # Diagonal
        if self.matrix[4] != ' ':
            if (self.matrix[0] == self.matrix[4] and self.matrix[4] == self.matrix[8]):
                win = self.matrix[4]
                if win == "X":
                    print("Win Player X")
                    return True
                else:
                    print("Win Player O")
                    return True
            if (self.matrix[2] == self.matrix[4] and self.matrix[4] == self.matrix[6]):
                win = self.matrix[4]
                if win == "X":
                    print("Win Player X")
                    return True
                else:
                    print("Win Player O")
                    return True

        if self.player_moves_1 + self.player_moves_2 == len(self.matrix):
            print("Draw")
            return True

        return False

    def run(self):
        turn = 0
        self.draw()
        while 0 <= turn <= len(self.matrix):
            if turn % 2 == 0:
                pos = int(input("Enter postion player X"))
                if self.play("X", pos):
                    self.draw()
                    turn += 1

            else:
                pos = int(input("Enter postion player O"))
                if self.play("O", pos):
                    self.draw()
                    turn += 1

            if self.valid():
                break

    def draw(self):
        print(f"-------------")
        print(f"| {self.matrix[0]} | {self.matrix[1]} | {self.matrix[2]} |")
        print(f"-------------")
        print(f"| {self.matrix[3]} | {self.matrix[4]} | {self.matrix[5]} |")
        print(f"-------------")
        print(f"| {self.matrix[6]} | {self.matrix[7]} | {self.matrix[8]} |")
        print(f"-------------")

    def play(self, symbol, pos):
        if 0 <= pos <= len(self.matrix) and self.matrix[pos] == " ":
            self.matrix[pos] = symbol.upper()
            return True
        else:
            print("Invalid Position")
            return False

TicTacToe().run()

# A* Alg
from collections import deque

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')


# P6
# batsman(sachin).
# cricketer(X) :- batsman(X).
# is_cricketer(X) :- cricketer(X).
# P7
# male(john).
# male(jim).
# male(bob).
# male(sam).
# male(joe).
# male(jack).
# female(jane).
# female(jenny).
# female(sue).
# female(mary).
# female(kim).
# parent(john, jim).
# parent(john, jane).
# parent(jim, jenny).
# parent(jim, bob).
# parent(bob, sam).
# parent(bob, sue).
# parent(jane, joe).
# parent(joe, jack).
# parent(sam, mary).
# parent(sam, kim).

# father(F, C) :- male(F), parent(F, C).
# mother(M, C) :- female(M), parent(M, C).
# grandfather(GF, GC) :- male(GF), parent(GF, P), parent(P, GC).
# grandmother(GM, GC) :- female(GM), parent(GM, P), parent(P, GC).
# brother(B, S) :- male(B), parent(P, B), parent(P, S), B \= S.
# sister(S, B) :- female(S), parent(P, S), parent(P, B), S \= B.
# uncle(U, N) :- male(U), parent(P, N), brother(U, P).
# aunt(A, N) :- female(A), parent(P, N), sister(A, P).
# nephew(N, U) :- male(N), parent(P, N), brother(U, P).
# niece(N, A) :- female(N), parent(P, N), sister(A, P).
# cousin(C1, C2) :- parent(P1, C1), parent(P2, C2), (brother(P1, P2); sister(P1, P2)).