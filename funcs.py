
def foo():
    print('foo')

if __name__ == "__main__":
    # will run only if I play this file!
    # NOT when import
    y = None
    print(y)
    foo()
    x: int = 1
    print(x)