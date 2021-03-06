class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.value_length = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.slots)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.value_length / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        algorithm fnv-1 is
    hash := FNV_offset_basis do

    for each byte_of_data to be hashed
        hash := hash × FNV_prime
        hash := hash XOR byte_of_data

    return hash 
        """
        offset_basis = 14695981039346656037
        prime_value = 1099511628211
        hashkey = offset_basis
        for byte in key.encode():
            hashkey *= prime_value
            hashkey = hashkey ^ byte
        return hashkey


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashkey = 5381
        for char in key.encode():
            hashkey = ((hashkey << 5) + hashkey) + char
        return hashkey


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Check if key already in hashtable
        if self.slots[self.hash_index(key)]:
            cur_node = self.slots[self.hash_index(key)]
            # Traverse through HashTableEntries at that key
            while cur_node is not None:
                if cur_node.key == key:
                    cur_node.value = value
                    self.value_length += 1
                    return
                
                cur_node = self.slots[self.hash_index(key)].next
            # Use cur_node.next to point to key/value pair
            old_head = self.slots[self.hash_index(key)]
            new_head = HashTableEntry(key, value)
            new_head.next = old_head
            self.slots[self.hash_index(key)] = new_head 

        else:
            self.slots[self.hash_index(key)] = HashTableEntry(key, value)
            self.value_length += 1
        
        if self.get_load_factor() >= 0.7:
            self.resize(self.get_num_slots()*2)   





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        try:
            cur_node = self.slots[self.hash_index(key)]
            if cur_node.key == key:
                self.slots[self.hash_index(key)] = cur_node.next
                self.value_length -= 1
                return
            prev = cur_node
            cur_node = cur_node.next
            while cur_node is not None:
                if cur_node.key == key:
                    prev.next = cur_node.next
                    self.value_length -= 1
                    break
                prev = cur_node
                cur_node = cur_node.next
        except IndexError as e:
            "WARNING: That key wasn't found."


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        cur_node = self.slots[self.hash_index(key)]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
        
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        temp = []
        for item in self.slots:
            if item is not None:
                temp.append((item.key, item.value))
            else:
                pass
        self.slots = [None] * new_capacity
        self.capacity = self.get_num_slots()
        for ii in temp:
            self.put(ii[0], ii[1])
        
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
