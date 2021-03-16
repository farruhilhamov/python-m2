
def main():
    table = [[[1],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[1],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[1],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0]],
            
     ]
    def tshower():
        global positions
        positions = []
        ls = -1
        for lines in table:
            ls += 1
            print(lines) 
            for i in lines:
                if i [0] == 1:
                    positions.append([ls ,lines.index([1])])

    
    def upright(pos):
        upr = [[pos [0] - 3] , [pos [1] +1]]
        return 
    def upleft(pos):
        upl = [[pos [0] - 3] , [pos [1] -1]]
        return 
    def downright(pos):
        downr = [[pos [0] + 3] , [pos [1] +1]]
        return 
    def downleft(pos):
        downl = [[pos [0] + 3] , [pos [1] -1]]
        return  
    def leftdown(pos):
        leftd = [[pos [0] + 1] , [pos [1] -3]]
        return 
    def leftup(pos):
        leftu = [[pos [0] - 1] , [pos [1] +3]]
        return 
    def rightdown(pos):
        rightd = [[pos [0] + 1] , [pos [1] +3]]
        print(rightd)
        return 
    def rightup(pos):
        rightu = [[pos [0] - 1] , [pos [1] +3]]
        return
        


    tshower()
    print(positions)
    position = positions [0] [len(positions) -2 ]
    print(position [0] +1)
    print(rightdown(position))

if __name__ == "__main__":
    main()