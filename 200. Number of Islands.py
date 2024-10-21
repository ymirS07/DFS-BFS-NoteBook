from collections import deque
R, C = map(int, input().strip().split())
matrix = []
for _ in range(R):
    line = list(map(int, input().strip().split()))
    matrix.append(line)
visited = [[False]*C for _ in range(R)]
directions = [[1,0], [0,1], [-1,0], [0,-1]]
cnt = 0

def dfs(r, c):
    visited[r][c] = True
    for d in directions:
        nx = r + d[0]
        ny = c + d[1]
        if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

def bfs(q):
    while q:
        cur = q.popleft()
        x, y = cur
        if visited[x][y]:  # 防止重复访问
            continue
        visited[x][y] = True
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            bfs(q)
            cnt += 1

print(cnt)
