# coding:utf-8

from random import randrange

MAX_HEIGHT=32
def pickHeight():
    h = 0
    z = randrange(1<<MAX_HEIGHT) # 32bitの乱数
    while z & (1<<h) != 0:
      h += 1
    return h

class SkiplistNode:
  def __init__(self, x, height):
    self.x = x
    self.next = [None] * (height+1)

class SkiplistSet:
  def __init__(self):
    self.sentinel = SkiplistNode(None, MAX_HEIGHT) # 番兵ノード
    self.h = 0
    self.stack = [self.sentinel] * (MAX_HEIGHT+1)
    self.length = 0

  def __len__(self):
    return self.length

  def find(self, x):
    u = self.sentinel
    for r in range(self.h, -1, -1):
      while u.next[r] is not None and u.next[r].x <= x:
        u = u.next[r]
      if u.x == x:
        return x
    return None

  def successor(self, x):
    u = self.sentinel
    for r in range(self.h, -1, -1):
      while u.next[r] is not None and u.next[r].x <= x:
        u = u.next[r]
      if u.x == x:
        break
    return u.next[0].x if u.next[0] is not None else None

  def predecessor(self, x):
    u = self.sentinel
    for r in range(self.h, -1, -1):
      while u.next[r] is not None and u.next[r].x < x:
        u = u.next[r]
    return u.x

  def add(self, x):
    u = self.sentinel
    for r in range(self.h, -1, -1):
      while u.next[r] is not None and u.next[r].x < x:
        u = u.next[r]
      if u.next[r] is not None and u.next[r].x == x:
        return
      self.stack[r] = u
    w_h = pickHeight()
    w = SkiplistNode(x, w_h)
    if self.h < w_h:
      self.h = w_h
    for r in range(w_h+1):
      v = self.stack[r]
      w.next[r] = v.next[r]
      v.next[r] = w
    self.length += 1

  def remove(self, x):
    u = self.sentinel
    removed = False
    for r in range(self.h, -1, -1):
      while u.next[r] is not None and u.next[r].x < x:
        u = u.next[r]
      if u.next[r] is not None and u.next[r].x == x:
        removed = True
        u.next[r] = u.next[r].next[r]
        if (u.x is None # When u is sentinel
            and u.next[r] is None):
          self.h -= 1
    if removed:
      self.length -= 1

