class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]   

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
           new_h = self.find_slot(key, h)
           self.arr[new_h] = (key, val)


                
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        prob_range = [*range(h, len(self.arr))] + [*range(0, h)]
        
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return None
            if self.arr[prob_index][0] == key:
                return self.arr[prob_index][1]
           

    def find_slot(self, key, index):
        prob_range = [*range(index, len(self.arr))] + [*range(0, index)]
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                 return prob_index
        raise Exception('hashmap full')
    
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = [*range(h, len(self.arr))] + [*range(0, h)]
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
                return
    def tPrint(self):
        print(self.arr)

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 130
    t['march 6'] = 78
    t['march 8'] = 20
    t['march 9'] = 4
    t['march 17'] = 27
    del t['march 17']
    t.tPrint()
    