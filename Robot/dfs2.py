N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

print (graph)
# used to store parent information as well
visited = (N+1)*[-1] 

def bfs(start_node):
	q = [start_node]
	visited[start_node] = 0 # which node has been visited
	while len(q) > 0:
		print("nodes to explore: ", q)
		node = q.pop(0) # FIFO
		if node == goal: 
			print ("found goal ", node)
			return ()
		print("expanding node ", node)
		connected_nodes = graph[node] # all the connected nodes
		for a_node in connected_nodes:
			if visited[a_node] == -1:
				visited[a_node] = node # remember parent
				q.append(a_node) # add to explore list

def recover_path(node): # recover path by tracing parent 
	path = [node]
	while visited[node] != 0:
		node = visited[node]
		path.append(node)
		print (path)
	path.reverse()
	return (path)

start, goal = map(int, input("start, goal : ").split())
bfs(start)
print (visited)
path = recover_path(goal)
