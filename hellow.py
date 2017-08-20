#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-


def consumer():
    r = ''
    while True:
        
        r = 'yield %s' % r
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consumer %s' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        try:
            n = n + 1
            print('[PRODUCER] Producing %s ...' % n)
            r = c.send(n)
            print('[PRODUCER] Consumer return: %s' % r)
        except StopIteration as e:
            print('Exception ')
            break
    c.close()

c = consumer()
produce(c)

