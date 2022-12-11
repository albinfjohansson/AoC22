data = []
with open("C:\\Repos\\AoC22\\input\\input10.txt", "r") as f:
    input = f.read()
    data = input.split("\n")


def step_cycle(x, cycle, cycle_value):
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        cycle_value.append(x*cycle)
    return cycle

def iterate_lines(d):
    cycle = 0
    x = 1
    outputs = [] 

    for item in d:
        if "noop" in item:
            cycle = step_cycle(x, cycle, outputs)
        else:
            x_step = int(item.split(" ")[1])
            cycle = step_cycle(x, cycle, outputs)
            cycle = step_cycle(x, cycle, outputs)
            x += x_step
    return outputs
        
def paint_pixle(x, cycle):
    cycle_val = cycle%40 - 1
    if cycle_val == -1:
        cycle_val = 39
    if cycle_val in [x-1, x, x+1]:
        return '#'
    return '.'

def painter(d):
    cycle = 1
    x = 1
    pixlepainter = ""
    pixle = 0
    for item in d:
        pixlepainter += paint_pixle(x, cycle)
        cycle += 1

        if "noop" not in item:
            sub_x = int(item.split(" ")[1])
            pixlepainter += paint_pixle(x, cycle)
            cycle += 1
            x += sub_x
    return pixlepainter


# Part 1
_data = data

res = iterate_lines(_data)
print(f"resutl part 1 = {sum(res)}")


# Part 2
_data = data

res = painter(_data)
print("Result part 2")
pretty = ""
for idx, val in enumerate(res):
    if idx % 40 == 0 and idx > 0:
        print(pretty)
        pretty = ""
    pretty += val
print(res[len(res)-40:])
