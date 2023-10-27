from Mylist import Mylist

lst = Mylist()
lst.insert_to_start(15)
lst.mylist_print() # -> 15
lst.insert_to_index(14, 1)
lst.mylist_print() # -> 15 14
lst.delete_at_index(0) # -> 14

