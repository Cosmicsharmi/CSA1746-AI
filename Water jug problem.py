from collections import deque
def water_jug():
    q = deque()
    visited = set()
    q.append(((0, 0), [])) 
    while q:
        (a, b), path = q.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        if a == 2:
            for step in path:
                print(f"A: {step[0]}, B: {step[1]}")
            return 
        next_states = [
            (4, b),     
            (a, 3),     
            (0, b),    
            (a, 0),     
            (min(a + b, 4), b - (min(a + b, 4) - a)),  # B → A
            (a - (min(a + b, 3) - b), min(a + b, 3))   # A → B
        ]
        for state in next_states:
            if state not in visited:
                q.append((state, path))

water_jug()
