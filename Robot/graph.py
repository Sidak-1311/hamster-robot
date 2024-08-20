N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
visited = (N+1)*[False]

def bfs(start_node):
    q = [start_node]
    visited[start_node] = True
    while len(q) > 0:
        print("nodes to explore: ", q)
        node = q.pop(0)
        if node == goal:
            print("found goal: ", node)
            return ()
        print("expanding node ", node)
        connected_nodes = graph[node]

        for a_node in connected_nodes:
            if visited[a_node] == False:
                visited[a_node] = True
                q.append(a_node)

start, goal = map(int, input("start goal: ").split())
bfs(start)
