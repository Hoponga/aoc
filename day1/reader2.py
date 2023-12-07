with open('input', 'r') as f: 
    sum = 0 
    current = 0 
    valid_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for line in f.readlines(): 
        nums = [] 
        
        i = 0 
        while i < len(line): 
            if line[i].isdigit(): 
                nums.append(int(line[i]))
                
            else: 
                found = False 
                for number in valid_map:
                    if not found and line[i:].startswith(number): 
                        nums.append(valid_map[number])
                        found = True 
                        
                        
                
            i += 1
        #print(line, nums)
        print(nums[0]*10 + nums[-1])
        sum += nums[0]*10 + nums[-1]
           

print(sum)
                
