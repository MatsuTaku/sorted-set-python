import unittest
from sortedset import SkiplistSet
import random

class SortedSetTest(unittest.TestCase):
  def setUp(self):
    self.max_size = 100000
    while True:
      self.values = [i for i in range(self.max_size) if random.randrange(4) == 0]
      if len(self.values) > 0:
        break
    self.shuffled = random.sample(self.values, len(self.values))
    
  def __testSortedSet(self, S):
    for v in self.shuffled:
      S.add(v)
    n = len(self.values)
    target = None
    pred = None
    succ = self.values[0]
    k = 0
    for i in range(self.max_size):
      if k < n and self.values[k] == i:
        target = self.values[k]
        pred = self.values[k-1] if k-1 >= 0 else None
        succ = self.values[k+1] if k+1 < n else None
        k += 1
      else:
        pred = self.values[k-1] if k-1 >= 0 else None
        target = None
      self.assertEqual(S.find(i), target)
      self.assertEqual(S.successor(i), succ)
      self.assertEqual(S.predecessor(i), pred)

    size = n
    self.assertEqual(len(S), size)
    for v in self.shuffled:
      S.remove(v)
      size -= 1
      self.assertEqual(len(S), size)
      
  def testSkiplistSet(self):
    S = SkiplistSet()
    self.__testSortedSet(S)

if __name__ == '__main__':
  unittest.main()

