from itertools import permutations


def solve(preferences) -> int:
    attendees = {p[0] for p in preferences}
    return max(score(seating_plan, preferences) for seating_plan in permutations(attendees))


def score(seating_plan, preferences):
    seating_score = 0
    for i, attendee in enumerate(seating_plan):
        attendee_to_left = seating_plan[(i-1) % len(seating_plan)]
        attendee_to_right = seating_plan[(i+1) % len(seating_plan)]
        left_preference = next(p for p in preferences if p[0] == attendee and p[3] == attendee_to_left)
        right_preference = next(p for p in preferences if p[0] == attendee and p[3] == attendee_to_right)
        left_score = int(left_preference[2]) if left_preference[1] == "gain" else -int(left_preference[2])
        right_score = int(right_preference[2]) if right_preference[1] == "gain" else -int(right_preference[2])
        seating_score += left_score + right_score
    return seating_score
