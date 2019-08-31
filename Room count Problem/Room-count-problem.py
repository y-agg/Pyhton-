def Sort_Tuple(tup):  
    return(sorted(tup, key = lambda x: x[0]))   

def countroom(tup):
    time=[tup[0][1]]
    
    for i in range(1,len(tup)):
        flag=0
        for j in range(len(time)):
            if tup[i][0] > time[j] :
                time[j]=tup[i][1]
                flag=1
                break
        if flag==0:
            time.append(tup[i][1])
    return len(time)

if __name__ == '__main__':
    tup=[]
    print("/*Enter Starting and ending time separted by space for each workshop*/".title())
    for i in range(int(input("Enter Number of WorkShops: "))):
        print(f"WorkShop {i+1} Timming",end="")
        asd=input("Time :").split(" ")
        print("\r")
        tup.append((asd[0],asd[1]))
    print(f"Total Room Required : {countroom(Sort_Tuple(tup))}")    
    
