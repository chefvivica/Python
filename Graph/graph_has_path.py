def has_path(graph, src, dst):
  stack = [src]
  while stack:
    current = stack.pop()
    if current == dst:
      return True
    for neighbor in graph[current]:
      stack.append(neighbor)    
  return False

#recursive
def _has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False