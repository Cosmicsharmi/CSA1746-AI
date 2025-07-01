from collections import deque

def valid(m, c): return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

def next_states(m, c, b):
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    for dm, dc in moves:
        nm, nc, nb = (m - dm, c - dc, 0) if b else (m + dm, c + dc, 1)
        om, oc = 3 - nm, 3 - nc
        if valid(nm, nc) and valid(om, oc):
            yield (nm, nc, nb)

def solve():
    q = deque([((3,3,1), [])])
    seen = set()
    while q:
        state, path = q.popleft()
        if state in seen: continue
        seen.add(state)
        path = path + [state]
        if state == (0,0,0):
            for m,c,b in path:
                print(f"M:{m} C:{c} Boat:{'Left' if b else 'Right'}")
            return
        for nxt in next_states(*state):
            q.append((nxt, path))

solve()
