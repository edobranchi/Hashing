from random import randint

global HashTable

def list_creation(hash_dim):
    global HashTable
    HashTable = [[] for _ in range(hash_dim)]
  
#funzione di hash
def Hashing(rand_keyvalue):
    return rand_keyvalue % len(HashTable) 
  
#inserimento
def insert(num_ins):

    for i in range(num_ins):
        rand_keyvalue = randint(0, 100)
        rand_value = randint(0, 300)
        hash_key = Hashing(rand_keyvalue)
        HashTable[hash_key].append(rand_value)

#Stampa della lista

def display_hash():
    global HashTable

    for i in range(len(HashTable)):
        print(i, end=" ")

        for j in HashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

def hash_search(search_value):

    for index1,list in enumerate(HashTable):

        for index,element in enumerate(list):

            if element == search_value:

                print("valore trovato in : ",index1," alla posizione: ",index+1)
                return (index1,index)

    print("valore non trovato")

#cancellazzione elemento
def hash_delete(delete_value):
    index=hash_search(delete_value)

    try:
        HashTable[index[0]].pop(index[1])

    except:
        print("Impossibile cancellare")
