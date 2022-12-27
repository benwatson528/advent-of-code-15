def solve(boxes) -> (int, int):
    wrapping = ribbon = 0
    for box in boxes:
        l, w, h = int(box[0]), int(box[1]), int(box[2])
        wrapping += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        ribbon += sum(map(lambda x: x*2, sorted([w, l, h])[:2])) + (l*w*h)
    return wrapping, ribbon
