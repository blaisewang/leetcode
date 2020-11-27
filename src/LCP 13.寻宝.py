from collections import deque
from typing import List


class Solution:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def minimalSteps(self, maze: List[str]) -> int:
        m, n = len(maze[0]), len(maze)

        def in_bound(x, y):
            return 0 <= x < n and 0 <= y < m

        def bfs(x, y):
            r = [[-1 for _ in range(m)] for _ in range(n)]
            r[x][y] = 0
            q = deque()
            q.append((x, y))

            while len(q) > 0:
                x, y = q.popleft()
                for idx in range(4):
                    nx, ny = x + self.dx[idx], y + self.dy[idx]
                    if in_bound(nx, ny) and maze[nx][ny] != "#" and r[nx][ny] == -1:
                        r[nx][ny] = r[x][y] + 1
                        q.append((nx, ny))

            return r

        bs = []
        ss = []
        sx, sy, tx, ty = 0, 0, 0, 0
        for i in range(n):
            for j in range(m):
                if maze[i][j] == "M":
                    bs.append((i, j))
                elif maze[i][j] == "O":
                    ss.append((i, j))
                elif maze[i][j] == "S":
                    sx, sy = i, j
                elif maze[i][j] == "T":
                    tx, ty = i, j
        start_dist = bfs(sx, sy)
        nb = len(bs)
        if nb == 0:
            return start_dist[tx][ty]

        dist = [[-1 for _ in range(nb + 2)] for _ in range(nb)]
        dd = []
        for i in range(nb):
            d = bfs(bs[i][0], bs[i][1])
            dd.append(d)
            dist[i][nb + 1] = d[tx][ty]

        for i in range(nb):
            t = -1
            for k in range(len(ss)):
                mx = ss[k][0]
                my = ss[k][1]
                if dd[i][mx][my] != -1 and start_dist[mx][my] != -1:
                    if t == -1 or t > dd[i][mx][my] + start_dist[mx][my]:
                        t = dd[i][mx][my] + start_dist[mx][my]

            dist[i][nb] = t
            for j in range(i + 1, nb):
                mn = -1
                for k in range(len(ss)):
                    mx, my = ss[k][0], ss[k][1]
                    if dd[i][mx][my] != -1 and dd[j][mx][my] != -1:
                        if mn == -1 or mn > dd[i][mx][my] + dd[j][mx][my]:
                            mn = dd[i][mx][my] + dd[j][mx][my]
                dist[i][j] = mn
                dist[j][i] = mn

        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb + 1] == -1:
                return -1

        sn = 1 << nb
        dp = [[-1 for _ in range(nb)] for _ in range(sn)]
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        for mask in range(1, sn):
            for i in range(nb):
                if mask & (1 << i):
                    for j in range(nb):
                        if not (mask & (1 << j)):
                            np = mask | (1 << j)
                            if dp[np][j] == -1 or dp[np][j] > dp[mask][i] + dist[i][j]:
                                dp[np][j] = dp[mask][i] + dist[i][j]

        res = float("inf")
        final_mask = sn - 1
        for i in range(nb):
            if res > dp[final_mask][i] + dist[i][nb + 1]:
                res = dp[final_mask][i] + dist[i][nb + 1]

        return res
