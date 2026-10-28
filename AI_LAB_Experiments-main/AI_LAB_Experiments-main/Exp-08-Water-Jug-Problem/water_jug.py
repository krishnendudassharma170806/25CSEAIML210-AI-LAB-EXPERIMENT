from collections import deque

def water_jug(capacity_a, capacity_b, target):
    
    queue = deque()
    visited = set()
    parent = {}

    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        a, b = current

        if a == target or b == target:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Solution Path (Jug A, Jug B):")
            for step, state in enumerate(path):
                print(f"  Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L")
            return path

        # Possible operations:
        # 1. Fill Jug A completely
        # 2. Fill Jug B completely
        # 3. Empty Jug A
        # 4. Empty Jug B
        states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0)
        ]

        # 5. Pour Jug A -> Jug B
        amount_a_to_b = min(a, capacity_b - b)
        states.append((a - amount_a_to_b, b + amount_a_to_b))

        # 6. Pour Jug B -> Jug A
        amount_b_to_a = min(b, capacity_a - a)
        states.append((a + amount_b_to_a, b - amount_b_to_a))

        for new_state in states:
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    print("No solution exists")
    return None


if __name__ == "__main__":
    capacity_a = 4
    capacity_b = 3
    target = 2

    print("Water Jug Problem Configuration:")
    print(f"  Jug A Capacity : {capacity_a} Liters")
    print(f"  Jug B Capacity : {capacity_b} Liters")
    print(f"  Target Volume  : {target} Liters")
    print()

    water_jug(capacity_a, capacity_b, target)
