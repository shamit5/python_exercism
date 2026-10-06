def value(colors):
    list = {
            'black': 0,
            'brown': 1,
            'red': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9,
          }

    sum  = 0 
    for color in colors[:2]:
        sum = sum*10 + list[color]
       

     
    return sum           
