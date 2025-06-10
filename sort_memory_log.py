memories = [("that was hard", 2), ("I loved that moment", 9), ("I'm okay", 5)]

sorted = sorted(memories, key = lambda x: x[1]) # sorts by tuple x[1] so automatically goes from 2, 5, 9 . 

print(sorted)