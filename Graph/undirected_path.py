def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return explore(graph, node_A,node_B, set()) 
  
  
def build_graph(edges):
  graph = {}
  for edge in edges:
    s, d = edge
    if s not in graph:
      graph[s] = []
    if d not in graph:
      graph[d] = []
    
    graph[s].append(d)
    graph[d].append(s)
  return graph

def explore(graph, s, d , visited):
  if s == d :
    return True
  
  if s in visited:
    return False
  
  visited.add(s)
  
  for neighbor in graph[s]:
    if explore(graph, neighbor, d, visited) == True:
      return True
    
  return False
    