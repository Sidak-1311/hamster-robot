N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
print (graph)

# used to mark nodes that have been visited
visited = (N+1)*[False] 

def dfs(node):
	if (node == goal):
		print("goal found: ", node)
		return()
	print ("expanding ", node)
	connected_nodes = graph[node] # all the connected nodes
	for a_node in connected_nodes:
		if visited[a_node] == False:
			visited[a_node] = True
			dfs(a_node)

def dfs2(start_node):
	q = [start_node]
	visited[start_node] = True # which node has been visited
	while len(q) > 0:
		node = q.pop() # LIFO
		print("expanding node ", node)
		connected_nodes = graph[node] # all the connected nodes
		for a_node in connected_nodes:
			if a_node == goal: # found path
				print ("found goal ", a_node)
				return ()
			if visited[a_node] == False:
				q.append(a_node) # add to the explore list


start, goal = map(int, input("start, goal : ").split())
visited[start] = True 
dfs2(start)
