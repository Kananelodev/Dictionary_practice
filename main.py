#Question 1

def highest_mark(plea):
  return max(plea, key=plea.get)
        
# print(highest_mark( {'Tom':67, 'Jerry':89, 'Mickey':95, 'Donald':80} ))

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
   
# print(summer({}))

#Question 7

def invert(plea):
   
   return dict(reversed(list(plea.items())))

# print(invert( {'a':1, 'b':2}))

#Question 8

def common():
   pass



