n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(graph_matrix, x, y, color, cnt):
    graph_matrix[x][y] = 0  # visited
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):
            if (graph[ny][nx] == color):
                cnt = dfs(graph_matrix, nx, ny, color, cnt+1)
    return cnt


graph = []
visited = []
for _ in range(m):
    line = list(input())
    graph.append(line)


black = 0
white = 0

for i in range(m):
    for j in range(n):
        if (graph[i][j] == 'B'):
            black += dfs(graph, i, j, 'B', 1) ** 2
        if (graph[i][j] == 'W'):
            white += dfs(graph, i, j, 'W', 1) ** 2

print(white, black)
