def solve(places, find_max=False) -> int:
    if find_max:
        return max(dfs(starting, places, {starting}, 0, True) for starting in places.keys())
    else:
        return min(dfs(starting, places, {starting}, 0, False) for starting in places.keys())


def dfs(current, places, visited, distance, find_max):
    if len(visited) == len(places.keys()):
        return distance
    if find_max:
        return max(
            dfs(neighbour, places, visited | {neighbour}, distance + dist_to_neighbour, find_max) for
            neighbour, dist_to_neighbour in
            places[current] if neighbour not in visited)
    else:
        return min(
            dfs(neighbour, places, visited | {neighbour}, distance + dist_to_neighbour, find_max) for
            neighbour, dist_to_neighbour in
            places[current] if neighbour not in visited)
