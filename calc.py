#!/usr/bin/env python3
import sys
from datetime import datetime

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("err: invalid args")
        sys.exit(-1)
    
    t1 = datetime.strptime(sys.argv[1], "%Y-%m-%d_%H:%M:%S.%f")
    t2 = datetime.strptime(sys.argv[2], "%Y-%m-%d_%H:%M:%S.%f")

    if t1 > t2:
        print("err: invalid datetime")
        sys.exit(-1)

    diff = (t2 - t1).total_seconds()
    print(diff)
