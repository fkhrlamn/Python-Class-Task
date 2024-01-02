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

            

    def hash(self, string_key):
        return hash(string_key) % self.size

    def rehash(self, hashed_index):
        return (hashed_index + 1) % self.size



Hash = HT()
Hash['name'] = 'Zikri'
Hash['age'] = 20
Hash['gender'] = 'M'

print(Hash['name'])
print(Hash['age'])
print(Hash['gender'])
print(Hash.keys)
print(Hash.values)

Hash['birthdate'] = '4 December'
print(Hash.keys)
print(Hash.values)
print(Hash['birthdate'])

Hash['name'] = 'Hakim'
print(Hash['name'])

Hash.delete('age')
print(Hash.keys)
print(Hash.values)
print(Hash['age'])
print(Hash['birthdate'])