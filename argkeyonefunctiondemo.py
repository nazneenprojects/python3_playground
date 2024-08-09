def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(f"pos1: {pos1}")
    print(f"pos2: {pos2}")
    print(f"pos_or_kwd: {pos_or_kwd}")
    print(f"kwd1: {kwd1}")
    print(f"kwd2: {kwd2}")

# Calling the function with the required parameters
f(1, 2, 3, kwd1="a", kwd2="b")

# The following would also be valid calls:
# f(1, 2, pos_or_kwd=3, kwd1="a", kwd2="b")

# The following would raise a TypeError:
# f(pos1=1, pos2=2, pos_or_kwd=3, kwd1="a", kwd2="b")  # TypeError: f() got some positional-only arguments passed as keyword arguments: 'pos1, pos2'
# f(1, 2, 3, "a", "b")  # TypeError: f() takes 3 positional arguments but 5 were given
