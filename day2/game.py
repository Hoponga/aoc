with open('input', 'r') as f: 
    red = 12 
    green = 13
    blue = 14 
    id_sum = 0 
    counter = 1 
    for line in f.readlines(): 
        line = line[(line.index(': ')+2):].split('; ')
        #print(line)
        bad_game = False 
        this_red = this_green = this_blue = 0
        for sample in line: 
            sample = sample.split(', ')
            #print(sample)
            

            for thing in sample: 
                #print(thing)
                if 'green' in thing: 
                    current = int(thing.split()[0])
                    if current > this_green: 
                        this_green = current 
                elif 'red' in thing: 
                    current = int(thing.split()[0])
                    if current > this_red: 
                        this_red = current 
                elif 'blue' in thing: 
                    current = int(thing.split()[0])
                    if current > this_blue: 
                        this_blue = current 
            # print(this_red, this_blue, this_green, bad_game)
            
        id_sum += this_green*this_red*this_blue

        counter += 1
    print(id_sum)
