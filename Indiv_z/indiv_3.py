#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_depth(a, n = 1):
    depth = n
    for i in a:
        if type(i) is list:
            n += 1
            depth = max(depth, max_depth(i, n))
    return depth

if __name__ == '__main__':
    print(max_depth([1,[2,[3,[4]]]]))
    print(max_depth([1, 2, [3, 4]]))