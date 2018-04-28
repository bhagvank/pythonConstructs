def custom_map(transformation, array):
    return [transformation(e) for e in array]


def add_one(x): return x + 1


def test():
    my_array = [1, 2, 3, 4, 5]
    print(str(custom_map(add_one, my_array)))

if __name__ == "__main__":
    test()
