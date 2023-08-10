import itertools
count_variants = 2
items = list(itertools.product([0, 1], repeat=count_variants))
print(items)
print(len(items))

if_statements = []
count_if = 2 

def simulate_state_space():
  for item in range(0, count_if):
    yield list(items)

def turn_to_lists(item):
  items = []
  for item in item:
    this_item = []
    items.append(this_item)
    for subitem in item:
      this_item.append(list(subitem))
  return items

def explore():
  state_space = list(simulate_state_space())
  state_space = turn_to_lists(state_space)
  for item in state_space:
    print(item)
  previous = state_space[0]
  print(previous)
  results = []

  for n in range(0, count_if):
    print("BATCH")
    
    for i4, candidate in enumerate(state_space[0]):
      new_items = []
      for i, item in enumerate(previous):
  
        me = []
        
        for i2, subitem in enumerate(item):
      
         
          
          
          me.append(previous[i][i2] - candidate[i2] - 1)
        print("previous was ", previous[i], "today", candidate, me)
        new_items.append(me)
      yield from new_items
      previous = new_items  
    
print("RESULT")      
for item in explore():
  print(item)



for statement in if_statements:
  print(statement)
                               
combinations = list(itertools.permutations(items, 2))
print(len(combinations))