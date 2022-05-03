def printChar(arr, Len):
    occ = {}
    for i in range(Len):
         
        if(arr[i] in occ):
            occ[arr[i]] = occ[arr[i]] + 1 
        else:
            occ[arr[i]] = 1

    size = len(occ)
  
    while (size > 0):
  
        current_max = 0
        ar_max = 0
        for key, value in occ.items():
 
            if ((value > current_max) or (value == current_max and key > ar_max)):
                ar_max = key
                current_max = value
  
        # Print the character
        print(f"{ar_max} - {current_max}")

        occ.pop(ar_max)
        size -= 1
 
Str = input("Enter a string: ")
Len = len(Str)
 
 
printChar(list(Str), Len)