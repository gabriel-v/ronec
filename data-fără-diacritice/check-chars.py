import sys
import string


def charset(filenames):
    b = set()
    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f.readlines():
                for ch in line:
                    b.add(ch)
    return b - set(string.printable)


assert len(sys.argv) >= 2
filenames = sys.argv[1:]
print('reading', filenames)
print('non-ascii charset in file:', charset(filenames))
