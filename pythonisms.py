# iterator

class IterThing:
    def __init__(self, max=0):
        self.max = max
    def __iter__(self):
        self.next = 0
        return self
    def __next__(self):
        if self.next <= self.max:
            result = 2 ** self.next
            self.next += 1
            return result
        else:
            raise StopIteration

def iter_test(num):
    result = []
    for number in IterThing(num):
        result.append(number)
    return result

def my_generator(num):
    for i in range(num):
        yield num * num

def my_gen_comp(num):
    return (x*x for x in range(num))

def print_my_gen(num):
    res = my_gen_comp(num)
    for num in res:
        print(num)

def print_list(input):
    res = []
    for num in range(input):
        res.append(num * num)
    return res
