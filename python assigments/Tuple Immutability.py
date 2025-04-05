my_tuple = (1, "surya", 3.14, 42, "sai")
try:
    my_tuple[1] = "changed"
except TypeError as e:
    print(e)
