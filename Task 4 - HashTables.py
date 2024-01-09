#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 4 - Hash Table


class HT:
     # initialize the size of hash tables
    def __init__(self,size=5):
        self.size = size           
        self.keys = [None] * size
        self.values = [None] * size


    def __setitem__(self, key, value):
            index = self.hash(key)
            # If the key already exists, update the value
            if self.keys[index] is None or self.keys[index] is key:
                self.keys[index] = key
                self.values[index] = value
                return
            
            else: # Rehashing to maintain the sequence
                old_Hash = index
                index = self.rehash(index)
                while index is not old_Hash:
                    if self.keys[index] is None or self.keys[index] is key:
                        self.keys[index] = key
                        self.values[index] = value
                        return
                    else:
                        index = self.rehash(index)


    def __getitem__(self,key):
        index = self.hash(key)

        if self.keys[index] == key:
            return self.values[index]
        else:# Rehashing to maintain the sequence
            old_Hash = index
            index = self.rehash(index)
            while index is not old_Hash:
                if self.keys[index] == key:
                    return self.values[index]
                else:
                    index = self.rehash(index)
            print("The key of [", key, "] is not in the Table")
            return None

    def delete(self, key):
        index = self.hash(key)

        if self.keys[index] == key:
            self.values[index] = None
            return
        else:     
            old_Hash = index
            index = self.rehash(index)
            while index is not old_Hash:
                if self.keys[index] == key:
                    print("The element at key [", key, "] is deleted")
                    self.values[index] = None
                    self.keys[index] = None
                    return
                else:
                    index = self.rehash(index)

            

    def hash(self,key):
        return dict[key[0]] % self.size

    def rehash(self, index):
        return (index + 1) % self.size

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

hash = HT()
hash['name'] = 'Zikri'
hash['age'] = 20
hash['gender'] = 'M'

print(hash['name'])
print(hash['age'])
print(hash['gender'])
print(hash.keys)
print(hash.values)

hash['birthdate'] = '4 December'
print(hash.keys)
print(hash.values)
print(hash['birthdate'])

hash['name'] = 'Hakim'
print(hash['name'])

hash.delete('age')
print(hash.keys)
print(hash.values)
print(hash['age'])
print(hash['birthdate'])
