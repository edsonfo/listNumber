#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import unittest
from Linked import Linked

class TestLinkedMethods(unittest.TestCase):
  def testInsertAtEnd(self):
    linked = Linked(3)
    linked.insert_at_end(1)
    self.assertEqual(linked.start_node.item, 1)


  def testdeleteAtStart(self):
    linked = Linked(3)
    linked.insert_at_end(1)
    linked.delete_at_start()
    self.assertEqual(linked.start_node, None)

  def testLimitLinkend(self):
    linked = Linked(3)
    linked.insert_at_end(1)
    linked.insert_at_end(2)
    linked.insert_at_end(3)
    linked.insert_at_end(4)
    self.assertEqual(linked.getItem(), [2,3,4])
    
        
if __name__ == '__main__':
  unittest.main()
