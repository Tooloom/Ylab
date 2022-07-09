class CyclicIterator:
    def __init__(self, obj):
        self.obj = obj
        self.it = iter(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            self.it = iter(self.obj)
            return next(self.it)


# --------------------- Main ---------------------
if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
