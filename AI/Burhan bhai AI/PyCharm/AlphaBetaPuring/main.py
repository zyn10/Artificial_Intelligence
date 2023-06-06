maxlist=[]
minlist=[]

def minimaxalgo(boardvalues,turn, alpha, beta):

    if len(boardvalues)==1:
        print("Optimal value",boardvalues)

    elif turn==True:
        #MAx turn
        maxlist=boardvalues.copy()
        boardvalues.clear()
        print("this is max function")
        i=0
        while i<len(maxlist):
            eval = max(maxlist[i], maxlist[i + 1])
            alpha = max(alpha, eval)
            #print("Alpha:",alpha)
            boardvalues.append(eval)
            i+=2
        print('max function return',boardvalues)
        minimaxalgo(boardvalues,False, alpha, beta)

    elif turn==False:
        #MIn turn
        minlist=boardvalues.copy()
        boardvalues.clear()
        print('this is min Function')
        i = 0
        while i < len(minlist):
            eval = min(minlist[i], minlist[i + 1])
            beta = min(beta, eval)
            #print("Beta:", beta)
            boardvalues.append(eval)

            i += 2
        print('min function return',boardvalues)

        minimaxalgo(boardvalues,True, alpha, beta)

    else:
        print("non veg")

def minimaxAlphaBetaalgo(boardvalues,turn, alpha, beta, index, depth):


    if depth==3:
        return boardvalues[index]
    elif turn==True:
        #MAx turn
        val = -999

        for x in range(2):
            print(index * 2 + x)
            valueGet = minimaxAlphaBetaalgo(boardvalues,False, alpha, beta, index * 2 + x, depth+1)
            val = max(val, valueGet)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return val

    elif turn==False:
        #MIn turn
        val = 999
        for x in range(2):
            print(index * 2 + x)
            valueGet = minimaxAlphaBetaalgo(boardvalues, True, alpha, beta, index * 2 + x, depth + 1)
            val = min(val, valueGet)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return val

    else:
        print("non veg")

#driver code
boardvalues=[4,6,2,10,14,6,22,21]
print('these are board values', boardvalues)
v = minimaxAlphaBetaalgo(boardvalues,True, -999,999, 0,0)
print("Optimal value by alpha-beta puring is: [",v,"]")