#ex3
#a

def read_line(n, file):
    
    file1=open(file)
    count = 0
    
    if type(n)!=int:
        return "invalid input detected"
    
    for line in file1:
       count = count+1
       if count == n:
           return line
        
    if n > count:
        return print("line" , n , "doesn't exist")
        


#b

def longest_words(file):

    try:
        file2=open(file)

    except:
        return "file not found"
    
    wlong = []

    for line in file2:
        
        data = line.replace('.',' ').replace('-',' ').split()
       
      
        for i in data:
            
            if len(wlong)<5:
                wlong.append(i)

            elif len(i) > len(wlong[0]):
                wlong[0] = i
                
            wlong = sorted(wlong, key=len)
            

    return wlong

                
                
        
