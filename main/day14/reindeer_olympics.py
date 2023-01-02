def solve_p1(reindeers, num_seconds) -> int:
    return max(move_reindeer(reindeer, num_seconds) for reindeer in reindeers)


def move_reindeer(reindeer, num_seconds):
    name, speed, move_time, rest_time = reindeer
    current_second = distance_travelled = 0
    while current_second < num_seconds:
        distance_travelled += int(speed) * int(move_time)
        current_second += int(move_time)
        if current_second > num_seconds:
            return distance_travelled - (int(current_second) - int(num_seconds)) * int(speed)
        current_second += int(rest_time)
    return distance_travelled


def solve_p2(reindeers, num_seconds) -> int:
    points = [0] * len(reindeers)
    for second in range(1, num_seconds + 1):
        round_results = [(i, move_reindeer(reindeer, second)) for i, reindeer in enumerate(reindeers)]
        max_distance_travelled = max(r[1] for r in round_results)
        for r in round_results:
            if r[1] == max_distance_travelled:
                points[r[0]] += 1
    return max(points)
