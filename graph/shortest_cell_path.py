from collections import deque
def shortestCellPath(grid, sr, sc, tr, tc):
  len_r = len(grid)
  len_c = len(grid[0])
  table = {(sr, sc) : 0}
  queue = deque()
  queue.append((sr, sc))
  while queue:
    print(queue[0])
    i, j = queue[0]
    dist = table[queue[0]]
    if i == tr and j == tc:
      return table[queue[0]]
    if i + 1 < len_r and grid[i + 1][j] and (i + 1, j) not in table:
      table[(i + 1, j)] = dist + 1
      queue.append((i + 1, j))
    if i - 1 > -1 and grid[i - 1][j] and (i - 1, j) not in table:
      table[(i - 1, j)] = dist + 1
      queue.append((i - 1, j))
    if j + 1 < len_c  and  grid[i][j + 1] and (i, j + 1) not in table:
      table[(i, j + 1)] = dist + 1
      queue.append((i, j + 1))
    if j - 1 > -1 and grid[i][j - 1] and (i, j - 1) not in table:
      table[(i, j - 1)] = dist + 1
      queue.append((i, j - 1))
    queue.popleft()
  print(table)
  print(queue)
  return False

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0

print(shortestCellPath(grid, sr, sc, tr, tc))
