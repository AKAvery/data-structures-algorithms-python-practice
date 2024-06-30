dict = {}
count = 0
with open('poem.txt', 'r') as f:
    for line in f: 
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('/n', '')
            if token in dict:
                dict[token]+=1
            else:
                dict[token]=1
            
    
print(dict['diverged'])