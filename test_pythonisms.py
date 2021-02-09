from pythonisms import IterThing, iter_test, my_gen_comp, print_list
import sys, types

def test_iter_test():
    assert iter_test

def test_gen_comp():
    assert my_gen_comp

def test_print_list():
    assert print_list

def test_iterthingy():
    assert IterThing

def test_iterthingy_example():
    actual = iter_test(8)
    expected = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    assert actual == expected

# generators save massive amounts of space when compared to returning a list that does the same thing. here I assert that the two functions that result in the same values differ in size.
def test_size_of_list_vs_generater_where_list_where_generator_should_be_smaller():
    a = my_gen_comp(3000)
    b = print_list(3000)
    x = sys.getsizeof(a)
    y = sys.getsizeof(b)
    actual = x < y
    expected = True
    assert actual == expected
