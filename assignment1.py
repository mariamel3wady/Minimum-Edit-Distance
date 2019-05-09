def minimumEditDistance(s1, s2):
    col=len(s1)+1
    row=len(s2)+1

    product=[[0 for x in range (col)]for y in range(row)]
    for i in range (1,row):
        product[i][0]=i
        
    for i in range (1,col):
        product[0][i]=i

    for i in range(1, row):
        for j in range(1, col):
            if s1[j-1] == s2[i-1]:      
                product[i][j]=min(product[i][j-1]+1, product[i-1][j]+1,product[i-1][j-1])
            else:
                product[i][j] = min(product[i][j-1]+1, product[i-1][j]+1,product[i-1][j-1]+1)

    print(product[i][j]) 
    i=row-1
    j=col-1
    result=""
    #print(i,j)
    while i>0 and j>0:
        
        up=product[i-1][j]+1
        left=product[i][j-1]+1
        if s1[j-1]!=s2[i-1]: 
            diagonal=product[i-1][j-1]+1
        else:
            diagonal=product[i-1][j-1]
        minimum=min(up,left,diagonal)
        if minimum==up:
            result+="insert"+str(s2[i-1])+"\n"
            i-=1
        elif minimum==left:
            result+="delete"+str(s1[j-1])+"\n"
            j-=1
        elif minimum==diagonal:
            if s1[j-1]!=s2[i-1]: 
                result+="exchange"+str(s1[j-1])+str(s2[i-1])+"\n"
            i-=1
            j-=1
    while(i >0):
        result+="insert"+str(s2[i-1])+"\n"
        i-=1
    while(j>0):
        result+="delete"+str(s1[j-1])+"\n"
        j-=1
    print(result)
print(minimumEditDistance("TTAACG","ATACG"))


        
        

