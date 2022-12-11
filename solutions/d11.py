data = []
with open("C:\\Repos\\AoC22\\input\\input11.txt", "r") as f:
    input = f.read()
    data = [x.split("\n") for x in input.split("\n\n")]
    

class Monkey:
    def __init__(self, name, items, iftrue, iffalse, operation, test):
        self.activity = 0
        self.name = name
        self.items = items
        self.items.reverse()
        self.test_value = (iffalse, iftrue)
        self.test = test
        self.received_items = []
        op = operation.split(" ")
        self.sign_of_operation = op[-2]
        self.val_of_operation = op[-1]

    def inspect_items(self, devisable_by_tree):
        item = self.items.pop()
        if "old" == self.val_of_operation:
            val = item
        else:
            val = int(self.val_of_operation)
        if self.sign_of_operation == "*":
            new_val = int(item * val)
        elif self.sign_of_operation == "+":
            new_val = item + val 
        elif self.sign_of_operation == "-":
            new_val = item - val
        elif self.sign_of_operation == "+":
            new_val = int(item / val)
        self.activity += 1
        if new_val % self.test == 0:
            if devisable_by_tree:
                new_val = int(new_val/3)
            return (self.test_value[1], new_val)
        if devisable_by_tree:
            new_val = int(new_val/3)
        return (self.test_value[0], new_val)

    def receive_item(self, item):
        self.items = [item] + self.items

def create_monkey_list(d):
    monkeys = {}
    max_worry_level = 1
    for monkey in d:
        name = monkey[0].split(" ")[-1][:-1]
        operation = monkey[2].split(":")[-1]
        test = monkey[3].split(":")[-1]
        test = int(test.split(" ")[-1])
        iftrue = monkey[4].split("throw to monkey ")[-1]
        iffalse = monkey[5].split("throw to monkey ")[-1]
        items = monkey[1].split("Starting items: ")[-1]
        items = [int(x) for x in items.split(", ")]
        m = Monkey(name, items, iftrue, iffalse, operation, test)
        max_worry_level = max_worry_level*test
        monkeys[name] = m
    return monkeys, max_worry_level


def test_throws(iterations, monkeys, max_worry_level, devisable_by_tree=True):
    for _ in range(iterations):
        for name, monkey in monkeys.items():
            for _ in range(len(monkey.items)):
                recipitor, thrown_item = monkey.inspect_items(devisable_by_tree)
                thrown_item = thrown_item%max_worry_level
                monkeys[recipitor].receive_item(thrown_item)

def calculate_max(msg, monkeys):
    max_level = []
    for name, monkey in monkeys.items():
        max_level.append(monkey.activity)

    max_level.sort()
    print(msg,max_level.pop()*max_level.pop())


monkeys, max_worry = create_monkey_list(data)
test_throws(20, monkeys, max_worry)
calculate_max("Part 1", monkeys)


monkeys, max_worry = create_monkey_list(data)
test_throws(1000, monkeys, max_worry, False)
calculate_max("Part 2", monkeys)

