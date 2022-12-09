data = []
with open("C:\\Repos\\AoC22\\input\\input9.txt", "r") as f:
    input = f.read()
    data = [x.split(" ") for x in input.split("\n")]

orientation = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0, -1)}

def translate_data_to_cord(d):   
    x, y = 0, 0
    pos = [(x,y)]
    for org, val in d:
        move_x, move_y = orientation[org]
        for _ in range(int(val)):
            x += move_x
            y += move_y
            pos.append((x,y))

    return pos

def sign(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    return 0

def move(route):
    x, y = 0, 0
    trail = []
    for haed in route:
        h_x = haed[0]
        h_y = haed[1]
        if abs(h_x - x) > 1:
            x += sign(h_x, x)
            if abs(h_y-y) >= 1:
                y += sign(h_y, y)
        elif abs(h_y - y) > 1:
            y += sign(h_y, y)
            if abs(h_x-x) >= 1:
                x += sign(h_x, x)
        trail.append((x,y))
    return trail

cordinates = translate_data_to_cord(data) 

# Part 1
trail = move(cordinates)
print(f"Result part 1: {len(set(trail))}")

#part 2
current_path = cordinates
alls = []
for _ in range(9):

    current_path = move(current_path)
    alls.append(current_path)

print(f"Result part 2: {len(set(current_path))}")

