from collections import deque

n, m, start = map(int, input().split())


graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    if (a not in graph.keys()):
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)


def dfs(graph, start):
    need_visited = deque()
    visited = []

    need_visited.append(start)

    while need_visited:
        if need_visited[-1] not in graph.keys():
            visited.append(need_visited[-1])
            break

        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            need_visited.extend(graph[node])

    print(' '.join(map(str, visited)))


def bfs(graph, start):
    need_visited = deque()
    visited = []

    need_visited.append(start)

    while need_visited:
        if need_visited[0] not in graph.keys():
            visited.append(need_visited[0])

            break

        node = need_visited.popleft()

        if node not in graph.keys():
            break

        if node not in visited:
            visited.append(node)

            graph[node].sort()
            need_visited.extend(graph[node])

    print(' '.join(map(str, visited)))


dfs(graph, start)
bfs(graph, start)
