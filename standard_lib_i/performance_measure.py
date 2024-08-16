from timeit import default_timer

start_time = default_timer()

for _ in range(100000):
    pass

end_time = default_timer()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")