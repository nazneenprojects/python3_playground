class Zoo:
    kind = 'carnivores'             # class variable shared by all instances

    def __init__(self, name):
        self.name = name            # instance variable unique to each instance


if __name__ == "__main__":
    d = Zoo('wolves')
    e = Zoo('lion')

    print(d.kind)                   # shared by all zoo animals
    print(e.kind)                   # shared by all zoo animals

    print(d.name)                   # unique to d
    print(e.name)                   # unique to e



