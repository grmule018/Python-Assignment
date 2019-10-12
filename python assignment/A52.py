from __future__ import print_function
import sys
def sprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
sprint("abc","efg","xyz",sep="--")
