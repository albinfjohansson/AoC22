data = []
with open("C:\\Repos\\AoC22\\input\\input14.txt", 'r') as f:
    data = f.read().split("\n")

def sign(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    return -1
 
cave_and_sand = set()
for val in data:
    itirator = val.split(" -> ")
    old_x, old_y = (None, None)

    for part in itirator:
        x, y = [int(i) for i in part.split(",")]
        if old_x is not None:
            distance_x = abs(x - old_x)
            distance_y = abs(y - old_y)
            for i in range(distance_x + distance_y +1):
                new_x = old_x+i*sign(x, old_x)
                new_y = old_y+i*sign(y, old_y)
                cave_and_sand.add((new_x, new_y))
        old_x, old_y = (x,y)


abyss = 2+max(val[1] for val in cave_and_sand)
for x in range(-1000, (1600)):
    cave_and_sand.add((x, abyss))

 
part_1 = 0
part_2 = 0

for part in range(50000):
    sand = (500,0)

    while True:
        if sand[1]+1 >= abyss and part_1 == 0:
            part_1 = part
        if (sand[0], sand[1]+1) not in cave_and_sand:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in cave_and_sand:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in cave_and_sand:
            sand = (sand[0]+1, sand[1]+1)
        else:
            break
    if sand == (500, 0):
        part_2 = part + 1
        break
    cave_and_sand.add(sand)
 

print(part_1)
print(part_2)