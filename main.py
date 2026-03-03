#Question 1

def highest_mark(plea):
  return max(plea, key=plea.get)
        
print(highest_mark( {'Tom':67, 'Jerry':89, 'Mickey':95, 'Donald':80} ))

#Question 2

def sort(plea):
   well = dict(sorted(plea.items(), key=lambda item: item[1]))
   return well
  
# print(sort( {'a':3, 'b':1, 'c':2}))


#Question 3

def merge(plea, pleas):
   plea.update(pleas)
   return plea

# print(merge({'a':1}, {'b':2}))

#Question 4 

def remove_key(plea, key):
    # del plea[key]
   for i, keys in plea.items():
      if key in plea:
         del plea[key]
         return plea
      else:
         return f'Key not found'


# print(remove_key( {'p':5, 'q':6}, key='z'))

#Question 5

def existence(plea, key):
    for keys, values in plea.items():
        if key in plea:
            return True
        else:
           return False
      
# print(existence( {'x':5}, key='y' ))

#Question 6

def summer(plea):
   return sum(plea.values())
   
# print(summer({'x':1, 'y':2}))

#Question 7

def invert(plea):
   
   return dict(reversed(list(plea.items())))

# print(invert( {'a':1, 'b':2}))

#Question 8

def common(first, second):
   wel = {ke for ke, values in second.items() if ke in first.keys()}
   return wel

# print(common({'a':1, 'b':2}, {'b':3, 'c':4}))

#Question 9

def convert(list1, list2):
   return dict(zip(list1, list2))
   
# print(convert(['a','b','c'], [1,2,3]))

#Question 10

def frequency(list1):
   new_dict = {}

   for i in list1:
      new_dict[i] = new_dict.get(i, 0) + 1
   return new_dict
# print(frequency([1,2,2,3,3,3]))
#Question 11

def find(dict, val):
   return [key for key, value in dict.items() if value == val]

# print(find({'a':10, 'b':20, 'c':10}, val=10 ))

#Question 12

def default(list1):
   new_dict = {}

   for i in list1:
      new_dict[i] = new_dict.get(i, 0)
   return new_dict

# print(default( ['a','b','c']))

#Question 13

def duplicate_dict(list1):
   ok = []
   new_dict = {}
   for item in list1:
      for i, x in item.items():
         new_dict[i] = x
   ok.append(new_dict)
   return ok
# print(duplicate_dict([{'x':10}, {'x':10}] ))


#Question 14

def tuple_dict(tuple):
  return dict(tuple)

# print(tuple_dict( [('a',1),('b',2)]))

#Question 15

def display(dict):

   for key, value in dict.items():
      ok = f"{key}: {value}"

   return ok
   
# print(display({'a':1, 'b':2}))







