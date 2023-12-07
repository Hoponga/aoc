with open('input', 'r') as f: 
    sum = 0 
    current = 0 
    
    for line in f.readlines(): 
        nums = [] 
        
        for i in range(len(line)): 
            if line[i].isdigit(): 
                nums.append(int(line[i])) 
        sum += nums[0]*10 + nums[-1]
           

print(sum)
                
