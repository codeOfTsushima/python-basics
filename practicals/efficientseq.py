def exrtoddnum(datastr):
    oddcoll = [num for num in datastr if num % 2!= 0]
    return oddcoll

sensordata = [12, 3,1,2,3,4,2,1,23,1]
print(f"filtered odd elements; {exrtoddnum(sensordata)}")