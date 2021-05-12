import random
import time
import math

import numpy as np
from matplotlib import pyplot as plt


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def linear_plot(hash_dim,num_ins):
    if num_ins>hash_dim:
        print("Il numero di inserimenti eccede la dimensione della tabella, riprova")
        return
    hash_table = [None] * hash_dim
    collision = 0
    linear_index=0
    for i in range(num_ins):
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
        load_factor=truncate(load_factor,3)
        print(hash_dim,"   ", insert_value,"    " ,i,"   ",load_factor,"    ",truncate(float(exec_time),4),"   ",collision)
        result_list=[hash_dim,insert_value,i,load_factor,truncate(float(exec_time),4),collision]
        result_linear = open('Result/result_linear.txt', 'a')
        result_linear.writelines(str(result_list) + "\n")
        result_linear.close()

    with open('Result/result_linear.txt','r+') as f:
        lines = f.readlines()

        x_values = [line.split(",")[3] for line in lines]
        y_values = [line.split(",")[4] for line in lines]


        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace(")", "").replace("\n", "").replace(" ", "") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)


        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]

        # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
        fig, ax = plt.subplots()  # Create a figure and an axes.
        ax.plot(x_values, y_values, label='linear')  # Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Tempo (s)')  # Add a y-label to the axes.
        ax.set_title("Tempo inserimenti al variare del fattore di carico:")  # Add a title to the axes.
        plt.yticks(np.arange(0.40,0.60,step=0.02))
        plt.xticks(np.arange(0,1.1, step=0.1))
        plt.savefig('result/load_factor_time_linear_hash.png')
        plt.show()



        f.close()
        open('Result/result_linear.txt','w').close()


def chained_plot(num_ins,hash_dim):
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
            load_factor = i / hash_dim
            print(hash_dim, "    ",rand_value,"    ", i,"      ", truncate(float(exec_time), 4), "   ",load_factor)
            result_list = [hash_dim, rand_value, i, truncate(float(exec_time), 4),truncate(float(load_factor),2)]
            result_linear = open('Result/result_chained.txt', 'a')
            result_linear.writelines(str(result_list) + "\n")
            result_linear.close()
        with open('Result/result_chained.txt','r+') as f:
            lines = f.readlines()

            x_values = [line.split(",")[4] for line in lines]
            y_values = [line.split(",")[3] for line in lines]


            x_values = [s.replace("(", "").replace("'", "").replace(" ", "").replace("]","").replace("\n","") for s in x_values]
            y_values = [s.replace(")", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

            x_values[:] = (elem[:5] for elem in x_values)


            x_values = [float(item) for item in x_values]
            y_values = [float(item) for item in y_values]

            # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
            fig, ax = plt.subplots()  # Create a figure and an axes.
            ax.plot(x_values, y_values, label='linear')  # Plot some data on the axes.
            ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
            ax.set_ylabel('Tempo (s)')  # Add a y-label to the axes.
            ax.set_title("Tempo inserimenti al variare del fattore di carico:")  # Add a title to the axes.
            plt.yticks(np.arange(0.40,0.60,step=0.02))
            plt.xticks(np.arange(0,11, step=1))
            plt.savefig('Result/load_factor_time_chained_hash.png')
            plt.show()



            f.close()
            open('Result/result_chained.txt','w').close()

