class A:
    foo = "a"

    def __init__(self):
        self.foo = "b"

    def __getattribute__(self, name):
        if name != "bar":
            return super().__getattribute__(name)
        return "c"

    def __getattr__(self, name):
        if name != "bar":
            return super().__getattribute__(name)
        return "d"


a = A()
print(f"{A.foo=}, {a.foo=}, {a.bar=}")
