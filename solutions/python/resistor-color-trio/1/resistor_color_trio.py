def label(colors):
    coding = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3 ,
        'yellow': 4 ,
        'green': 5,
        'blue': 6 ,
        'violet': 7,
        'grey': 8,
        'white': 9,
    }
    ans = 0 
    for color in colors[:2]:
         ans = ans * 10 + coding[color]
    ans = ans * 10 ** coding[colors[2]]

    if ans >= 1_000_000_000:
        return f"{ans // 1_000_000_000} gigaohms"
    elif ans >= 1_000_000:
        return f"{ans // 1_000_000} megaohms"
    elif ans >= 1_000:
        return f"{ans // 1_000} kiloohms"
    else:
        return f"{ans} ohms"
      


         
         
         
