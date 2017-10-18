#!/usr/bin/python

class Stack:
    _stack = []

    def __init__(self):
        self._stack = []
    
    def size(self):
        return len(self._stack)
    
    def push(self, item):
        self._stack.append(item)
        
    def pop(self):
        if self.size() > 0:
            return self._stack.pop()
        return None
    
    def top(self):
        if self.size() > 0:
            return self._stack[-1]
        return None

def testStack():
    s = Stack()
    assert s.size() == 0
    assert s.pop() == None
    s.push(1)
    assert s.top() == 1
    s.push(3)
    assert s.top() == 3
    assert s.size() == 2
    assert s.pop() == 3
    assert s.top() == 1
    assert s.size() == 1
    s.pop()
    assert s.size() == 0
    assert s.pop() == None
    assert s.size() == 0
    print 'ok'

#testStack()
