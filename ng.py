from pathlib import Path


class Source:
    def __init__(self, name, compiler='', defines=[]):
        pass

class Library:
    def __init__(self, name, compiler='', defines=[]):
        pass

class Compiler:
    def __init__(self, name, version='*', flags=[], raw_flags=[]):
        pass


def app(name, srcs=[], libs=[], compiler=''):
    pass


def lib(name, srcs=[], libs=[], compiler=''):
    pass


def glob(*args):
    patterns = []
    for p in args:
        patterns.append(p)

    print(patterns)

    p = Path.cwd()
    print(p)

    for pattern in patterns:
        print(list(p.glob(pattern)))

    pass


def main():
    glob('**/*.cpp')
    
    pass


if __name__ == '__main__':
    main()
