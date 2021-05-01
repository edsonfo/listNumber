from ListNumber import ListNumber
from Linked import linked

class Main(object):
  def main(self):
    a = ListNumber([1,2,3,4])
    b = a.addNum()
    # print(b)
    c= a.addNum()
    # print(c)
    e = Linked(3)
    f = e.insert_at_end(1)
    g = e.insert_at_end(2)
    h = e.insert_at_end(3)
    e.traverse_list()
    e.delete_at_start()
    e.delete_at_start()
    e.delete_at_start()
    e.traverse_list()

if __name__ == "__main__":
    Main().main()
