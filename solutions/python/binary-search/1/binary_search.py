def find(search_list, value):
    search_list = sorted(search_list)
    i = 0 
    j = len(search_list) - 1

    while(i <= j ):
        m = (i + j) // 2
        if search_list[m] == value:
            return m
        elif(search_list[m] > value):
            j = m - 1 
        else:
            i = m + 1 


    raise ValueError("value not in array")
        

    
