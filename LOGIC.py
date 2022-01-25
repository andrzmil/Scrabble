import itertools

red = (255,0,0)
blue = (0,50,255)
light_blue = (0,230,255)
pink = (234,161,236)
white = (255,255,255)
black = (0,0,0)

letters_freq = {'@': 2,
                'E': 12, 'A': 9, 'I': 9, 'O':8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4,
                'D': 4, 'G': 3,
                'B': 2, 'C': 2, 'M': 2, 'P': 2,
                'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2,
                'K': 1,
                'J': 1, 'X':1,
                'Q': 1, 'Z': 1
}

def generate_letterset():
    letterset = list()
    for k,v in letters_freq.items():
        tmp_lt = list(itertools.repeat(k,v))
        letterset.append(tmp_lt)
    letterset = [item for sublist in letterset for item in sublist]
    print(letterset)
    return list(letterset)



letters_points = {'@': 0,
                'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1,
                'D': 2, 'G': 2,
                'B': 3, 'C': 3, 'M': 3, 'P': 3,
                'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                'K': 5,
                'J': 8, 'X':8,
                'Q': 10, 'Z': 10
}

special_score = [
    [1,1,"TWS"],[1,8,"TWS"],[1,15,"TWS"],[8,1,"TWS"],[8,15,"TWS"],[15,1,"TWS"],[15,8,"TWS"],[15,15,"TWS"],
    [1,4,"DLS"],[1,12,"DLS"],[3,7,"DLS"],[3,9,"DLS"],[4,1,"DLS"],[4,8,"DLS"],[4,15,"DLS"],[7,3,"DLS"],[7,7,"DLS"],[7,9,"DLS"],[7,13,"DLS"],
    [8,4,"DLS"],[8,12,"DLS"],[9,3,"DLS"],[9,7,"DLS"],[9,9,"DLS"],[9,13,"DLS"],[12,1,"DLS"],[12,8,"DLS"],[12,15,"DLS"],[13,7,"DLS"],[13,9,"DLS"],[15,4,"DLS"],[15,12,"DLS"],
    [2,2,"DWS"],[2,14,"DWS"],[3,3,"DWS"],[3,13,"DWS"],[4,4,"DWS"],[4,12,"DWS"],[5,5,"DWS"],[5,11,"DWS"],
    [2,2,"DWS"],[2,14,"DWS"],[3,3,"DWS"],[3,13,"DWS"],[4,4,"DWS"],[4,12,"DWS"],[5,5,"DWS"],[5,11,"DWS"],
    [11,5,"DWS"],[11,11,"DWS"],[12,4,"DWS"],[12,12,"DWS"],[13,3,"DWS"],[13,13,"DWS"],[14,2,"DWS"],[14,14,"DWS"],
    [2,6,"TLS"],[2,10,"TLS"],[6,2,"TLS"],[6,6,"TLS"],[6,10,"TLS"],[6,14,"TLS"],
    [10,2,"TLS"],[10,6,"TLS"],[10,10,"TLS"],[10,14,"TLS"],[14,6,"TLS"],[14,10,"TLS"],
    [8,8,"CNT"]
]              

def special_field(i,j):
    for lst in special_score:
        if(i==lst[0] and j==lst[1]):
            return lst[2]


