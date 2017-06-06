#!/usr/bin/python3

import sys

   
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s : src file  dest file" % sys.argv[0])
        exit(1)

    fsrc = sys.argv[1]
    fdest = sys.argv[2]
            
    fr = open(fsrc, 'r')
    fw = open(fdest, 'w')
    baseline = 0

    line = fr.readline().strip()
    core = line.split(' ')[0]
    baseline = line.split(' ')[1]
    # first speedup factor
    print("%s %s" % (core, '1'), file=fw)

    while True:
        line = fr.readline().strip()
        if not line:
            break
        core = line.split(' ')[0]
        exetime = line.split(' ')[1]
        print(core)
        print(exetime)
        speedup = float(baseline) / float(exetime)
        print("%s %f" % (core, speedup), file=fw)

    fr.close()
    fw.close()
