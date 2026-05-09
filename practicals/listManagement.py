# Problem Statement:
# Alex is developing an application to manage a warehouse inventory list. He requires a 
# Python function that appends multiple new items to an existing inventory list sequentially. 
# Following the concatenation, the function must attempt to remove an item from a user-
# index is passed, the system does not crash but instead handles the error gracefully and 
# returns a standardized warning.    
    
def managelist(initalist,newel,removeind):
    for element in newel:
        initalist.append(element)
    try:
        removeditem = initalist.pop(removeind)
        return initalist, removeditem
    except IndexError:
        return initalist, "Error: deletion index not available"
    
currentInv = ["Sword", "Shield"]
itemToadd = ["Potion", "Map"]
indexToDel = 2

updatedList, deletedItem = managelist(currentInv, itemToadd, indexToDel)
print(f"Final List: {updatedList}")
print(f"Removed entity: {deletedItem}")
