import random
import time
import math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def linear_plot():
    hash_dim = random.randrange(1000,2000)
    max_number_of_insertion = hash_dim-1
    hash_table = [None] * hash_dim
    collision = 0
    linear_index=0
    for i in range(random.randrange(1000,hash_dim)):
        start_time = time.time()
        time.sleep(0.5)
        insert_value=random.randrange(40,50)
        h_k = insert_value % hash_dim  # calcolo h'(k)
        h_k = (h_k + linear_index) % hash_dim  # calcolo h(k)= (h'(k)+i)mod m

        while hash_table[h_k] != None:  # se la posizione h_k è occupata incrementa il contatore collisione
            collision += 1  # scorre alla posizione successiva
            h_k += 1
            if h_k >= hash_dim:  # se arriva in fondo alla tabella ricomincia dalla prima posizione
                h_k = 0
        hash_table[h_k] = insert_value
        exec_time = time.time() - start_time
        exec_time = exec_time % 1
        exec_time = f'{exec_time:.10f}'
        load_factor= i/hash_dim
        print(hash_dim,"   ", insert_value,"    " ,i,"   ",truncate(load_factor,4),"    ",truncate(float(exec_time),4),"   ",collision)
        result_list=[hash_dim,insert_value,i,truncate(load_factor,4),truncate(float(exec_time),4),collision]
        result_linear = open('Result/result_linear.txt', 'a')
        result_linear.writelines(str(result_list) + "\n")
        result_linear.close()


def chained_plot(num_ins):
        hash_dim = random.randrange(100, 200)
        HashTable = [[] for _ in range(hash_dim)]
        for i in range(num_ins):
            start_time = time.time()
            time.sleep(0.5)
            rand_keyvalue = random.randrange(1000, 2000)
            rand_value = random.randrange(100, 200)
            hash_key =  rand_keyvalue % len(HashTable)
            HashTable[hash_key].append(rand_value)
            exec_time = time.time() - start_time
            exec_time = exec_time % 1
            exec_time = f'{exec_time:.10f}'
            print(hash_dim, "    ",rand_value,"    ", i,"      ", truncate(float(exec_time), 4))
            result_list = [hash_dim, rand_value, i, truncate(float(exec_time), 4)]
            result_linear = open('Result/result_chained.txt', 'a')
            result_linear.writelines(str(result_list) + "\n")
            result_linear.close()


