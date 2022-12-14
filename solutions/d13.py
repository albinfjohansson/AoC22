data = []
with open("C:\\Repos\\AoC22\\input\\input13.txt", 'r') as f:
    input = f.read().split("\n\n")
    data = [x.split("\n") for x in input]


def get_biggest(x, y):
    if type(x) is list or type(y) is list:
        if type(x) is not list:
            x = [x]
        if type(y) is not list:
            y = [y]
        for _x,_y in zip(x,y):
            ret = get_biggest(_x,_y)
            if ret != 0:
                return ret

        return len(x) - len(y)
    else:
        return x - y  

def set_package_correct(package, d):
    new_res = []
    if not d:
        return [package]
    for i, val in enumerate(d):
        if get_biggest(eval(package), eval(val)) <= 0:
            new_res.append(package)
            new_res += d[i:]
            return new_res
        else:
            new_res.append(val)
    new_res.append(package)
    return new_res

count = 0
for idx, (x, y) in enumerate(data):
    if get_biggest(eval(x), eval(y)) <= 0:
        count += idx + 1
print(count)

_data = ["[[2]]", "[[6]]"] 
for (x,y) in data:
    _data.append(x)
    _data.append(y)

res_data = []

for val in _data:
    res_data = set_package_correct(val, res_data)
 
part2 = (res_data.index('[[2]]')+1) *  (res_data.index('[[6]]')+1)
print(part2)