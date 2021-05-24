import random                                    #LIBRERIE E VARIABILI GLOBALI

global hash_table
collision=0                                      #collision counter
linear_index=0
                  #popolazione della tabella con placeholder

def insert_generation(hash_dim,insert_dim):
    global hash_table
    if insert_dim>hash_dim:
        print("Il numero di inserimenti eccede la dimensione della tabella, riprova")
        return False

    hash_table = [None] * hash_dim #GENERAZIONE INSERIMENTI

    for i in range (insert_dim):
        insert_value = random.randrange(0,100,1)
        linear_insert(hash_dim,insert_value,hash_table) #chiamata per inserire
    return True

def linear_display():
    global hash_table
    print(hash_table)

def linear_insert(hash_dim, insert_value,hash_table):     #INSERIMENTO
    global collision
    global linear_index
    h_k = insert_value % hash_dim                  #calcolo h'(k)
    h_k = (h_k + linear_index) % hash_dim          #calcolo h(k)= (h'(k)+i)mod m

    while hash_table[h_k] != None :                #se la posizione h_k è occupata incrementa il contatore collisione
        collision += 1                             #scorre alla posizione successiva
        h_k += 1

        if h_k >= hash_dim:                        #se arriva in fondo alla tabella ricomincia dalla prima posizione
            h_k = 0

    hash_table[h_k]= insert_value                  #se trova una posizione nuova inserisce il valore
def linear_delete(delete_value):                    #CANCELLAZIONE
    global hash_table
    i = linear_search(delete_value)        #cerca il valore da cancellare

    if i==None:
        print("impossibile cancellare")                        

    else:
        hash_table[i] = None
        print("valore cancellato in posizione: ", i,) 
    

def linear_search(search_value):         #RICERCA
    global hash_table
    hash_dim = len(hash_table)
    found = False

    for i in range(hash_dim):

        if hash_table[i] == search_value:                   #ritorna il primo valore corrispondente che trova
            print("trovato in posizione :  " , i)
            found = True
            return i

    if found == False:
        print ("Valore non presente ")
