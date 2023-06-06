# create a tuple
# creation of tuple
tuple_ = ("john", "mark", 12, "14", "orange", 4.5)
print(tuple_)

def updateTuple(value,tuple_):
    # there are two methods to add values to tuple say jugar system
    # because tuple is immutable
    # 1) add a value to new tuple then concatenate tuples
    # 2) Convert tuple to list ,add value to list ,convert list to tuple
    # adding value to tuple and then adding concatenating this
    newtuple_ = value,
    tuple_ = tuple_+newtuple_
    print("After adding 6.5...")
    print(tuple_)

def counterFun(tuple_):
    # Checking for int float and strings
    stringCount = 0
    intCount = 0
    floatCount = 0
    tupleCount = len(tuple_)
    for i in range(tupleCount):
        if isinstance(tuple_[i], int):
            intCount = intCount + 1
        elif isinstance(tuple_[i], float):
            floatCount = floatCount + 1
        else:
            stringCount = stringCount + 1
    print("Integer Count : ", intCount)
    print("Float Count   : ", floatCount)
    print("String Count : ", stringCount)

updateTuple (6.5,tuple_)
counterFun (tuple_)