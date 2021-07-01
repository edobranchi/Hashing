import random
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
        insert_value=random.randrange(40,50)
        h_k = insert_value % hash_dim  # calcolo h'(k)
        h_k = (h_k + linear_index) % hash_dim  # calcolo h(k)= (h'(k)+i)mod m

        while hash_table[h_k] != None:  # se la posizione h_k è occupata incrementa il contatore collisione
            collision += 1  # scorre alla posizione successiva
            h_k += 1

            if h_k >= hash_dim:  # se arriva in fondo alla tabella ricomincia dalla prima posizione
                h_k = 0

        hash_table[h_k] = insert_value
        load_factor= i/hash_dim
        load_factor=truncate(load_factor,3)
        print(i,"   ",load_factor,"   ",collision)
        result_list=[i,load_factor,collision]
        result_linear = open('Result/result_linear.txt', 'a')
        result_linear.writelines(str(result_list) + "\n")
        result_linear.close()

    with open('Result/result_linear.txt','r+') as f:
        lines = f.readlines()

        x_values = [line.split(",")[1] for line in lines]
        y_values = [line.split(",")[2] for line in lines]
        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace("'", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)


        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]

        # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
        fig, ax = plt.subplots()  # Create a figure and an axes.
        ax.plot(x_values, y_values, label='linear')  # Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Collision')  # Add a y-label to the axes.
        ax.set_title("Collisioni al variare del fattore di carico")  # Add a title to the axes.
        plt.yticks(np.arange(0,550000,step=50000))
        plt.xticks(np.arange(0,1.1, step=0.1))
        plt.savefig('result/load_factor_collision_linear_hash.png')
        plt.show()

        f.close()
        open('Result/result_linear.txt','w').close()


def chained_plot(num_ins,hash_dim):
        HashTable = [[] for _ in range(hash_dim)]
        chained_collision=0
        for i in range(num_ins):
            rand_keyvalue = random.randrange(1000, 2000)
            rand_value = random.randrange(100, 200)
            hash_key =  rand_keyvalue % len(HashTable)
            HashTable[hash_key].append(rand_value)
            chained_collision = chained_collision + HashTable.index(HashTable[-1])
            load_factor = (i + 1) / hash_dim

            print(rand_value,"    ", chained_collision,"      ",load_factor)
            result_list = [rand_value, chained_collision,truncate(float(load_factor),2)]
            result_linear = open('Result/result_chained.txt', 'a')
            result_linear.writelines(str(result_list) + "\n")
            result_linear.close()

        with open('Result/result_chained.txt','r+') as f:
            lines = f.readlines()

            x_values = [line.split(",")[2] for line in lines]
            y_values = [line.split(",")[1] for line in lines]


            x_values = [s.replace("(", "").replace("'", "").replace(" ", "").replace("]","").replace("\n","") for s in x_values]
            y_values = [s.replace(")", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

            x_values[:] = (elem[:5] for elem in x_values)


            x_values = [float(item) for item in x_values]
            y_values = [float(item) for item in y_values]

            # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
            fig, ax = plt.subplots()  # Create a figure and an axes.
            ax.plot(x_values, y_values, label='linear')  # Plot some data on the axes.
            ax.set_ylabel('Collisioni:')  # Add an x-label to the axes.
            ax.set_xlabel('Load Factor:')  # Add a y-label to the axes.
            ax.set_title("Collisioni con load factor = " +str(load_factor))  # Add a title to the axes.
            plt.xticks(np.arange(0,1.1,step=0.1))
            plt.yticks(np.arange(0,550000, step=50000))
            plt.savefig('Result/load_factor_collision_chained_hash.png')
            plt.show()

            f.close()
            open('Result/result_chained.txt','w').close()

def research_plot_linear_notsuccess(hash_dim):
    with open('Result/result_search_linear_notsuccess.txt', 'w') as f:
        f.write('')
        f.close()
    for num_ins in range(1, hash_dim, hash_dim // 100):
        print("numins",num_ins)
        print("hash_dim",hash_dim//100)
        hash_table = [None] * hash_dim
        collision = 0
        linear_index=0

        for i in range(num_ins):
            insert_value=random.randrange(1,10000,2)
            h_k = insert_value % hash_dim  # calcolo h'(k)
            h_k = (h_k + linear_index) % hash_dim  # calcolo h(k)= (h'(k)+i)mod m

            while hash_table[h_k] != None:  # se la posizione h_k è occupata incrementa il contatore collisione
                collision += 1  # scorre alla posizione successiva
                h_k += 1

                if h_k >= hash_dim:  # se arriva in fondo alla tabella ricomincia dalla prima posizione
                    h_k = 0

            hash_table[h_k] = insert_value


        load_factor=num_ins/hash_dim
        linear_index=0
        count=0
        times=0
        while times <= 200:
            print("ciclo " + str(times))

            search_value=random.randrange(1,10000,2)
            print("devo cercare" + str(search_value))
            h_k = search_value % hash_dim  # calcolo h'(k)
            h_k = (h_k + linear_index) % hash_dim
            print("count: " + str(count))
            i=0
            maybe=h_k-1
            counter=0
            while i <= hash_dim:
                print(h_k)
                print(hash_dim)
                print (i)
                if h_k == hash_dim or i == hash_dim:
                    h_k=0
                    i=0
                elif hash_table[h_k] == None:                   #ritorna il primo valore corrispondente che trova
                            print("non presente")
                            count=count+1
                            break
                elif hash_table[h_k] == search_value:
                             print("trovato")
                             count=count-counter
                             count=count+1
                             times=times-1
                             break
                elif maybe == h_k:
                    count=count+1
                    break
                else:
                    counter=counter+1
                    h_k=h_k+1
                    i=i+1
                    count = count + 1
            times=times+1


        count = count/200
        result_linear = open('Result/result_search_linear_notsuccess.txt', 'a')
        result_linear.writelines(str(count) + " ," + str(load_factor) +"\n")
        result_linear.close()
    with open('Result/result_search_linear_notsuccess.txt','r+') as f:
        lines = f.readlines()

        y_values = [line.split(",")[0] for line in lines]
        x_values = [line.split(",")[1] for line in lines]
        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace("'", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)


        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]


        # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
        fig, ax = plt.subplots()  # Create a figure and an axes.
        ax.plot(x_values, y_values,'orange',label='Ricerca senza successo')# Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Comparazioni medie per ricerca')  # Add a y-label to the axes.
        ax.set_title("Comparazioni medie necessarie per una ricerca \n al variare del fattore di carico")  # Add a title to the axes.
        plt.yticks(np.arange(0,1200,step=100))
        plt.xticks(np.arange(0,1.1, step=0.1))
        plt.legend(loc='upper left')
        plt.savefig('result/lineare_senzasuccesso.png')
        plt.show()

        f.close()


def research_plot_linear_success(hash_dim):
    with open('Result/result_search_linear_success.txt', 'w') as f:
        f.write('')
        f.close()
    for num_ins in range(1, hash_dim, hash_dim // 100):
        print("numins",num_ins)
        print("hash_dim",hash_dim//100)
        hash_table = [None] * hash_dim
        collision = 0
        linear_index=0

        for i in range(num_ins):
            insert_value=random.randrange(1,10000,2)
            h_k = insert_value % hash_dim  # calcolo h'(k)
            h_k = (h_k + linear_index) % hash_dim  # calcolo h(k)= (h'(k)+i)mod m

            while hash_table[h_k] != None:  # se la posizione h_k è occupata incrementa il contatore collisione
                collision += 1  # scorre alla posizione successiva
                h_k += 1

                if h_k >= hash_dim:  # se arriva in fondo alla tabella ricomincia dalla prima posizione
                    h_k = 0

            hash_table[h_k] = insert_value


        load_factor=num_ins/hash_dim
        linear_index=0
        count=0
        times=0
        while times <= 200:
            print("ciclo " + str(times))

            search_value=random.randrange(1,10000,2)
            print("devo cercare" + str(search_value))
            h_k = search_value % hash_dim  # calcolo h'(k)
            h_k = (h_k + linear_index) % hash_dim
            print("count: " + str(count))
            i=0
            counter=0
            maybe=h_k-1
            while i <= hash_dim:

                if h_k == hash_dim or i == hash_dim:
                    h_k=0
                    i=0
                elif hash_table[h_k] == None:                   #ritorna il primo valore corrispondente che trova
                            print("non presente")
                            count=count-counter
                            times=times-1
                            break
                elif hash_table[h_k] == search_value:
                            print("trovato")
                            count=count+1
                            break
                elif maybe == h_k:
                    count=count-counter
                    times=times-1
                    break
                else:
                    counter=counter+1
                    h_k=h_k+1
                    i=i+1
                    count = count + 1
            times=times+1


        count = count/200
        result_linear = open('Result/result_search_linear_success.txt', 'a')
        result_linear.writelines(str(count) + " ," + str(load_factor) +"\n")
        result_linear.close()
    with open('Result/result_search_linear_success.txt','r+') as f:
        lines = f.readlines()

        y_values = [line.split(",")[0] for line in lines]
        x_values = [line.split(",")[1] for line in lines]
        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace("'", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)


        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]

        fig, ax = plt.subplots()  # Create a figure and an axes.
        #ax.plot(x_values, y_values2, label='Ricerca senza successo')
        ax.plot(x_values, y_values,label='Ricerca con successo')# Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Comparazioni medie per ricerca')  # Add a y-label to the axes.
        ax.set_title("Comparazioni medie necessarie per una ricerca \n al variare del fattore di carico")  # Add a title to the axes.
        plt.yticks(np.arange(0,100,step=10))
        plt.xticks(np.arange(0,1.1, step=0.1))
        plt.legend(loc='upper left')
        plt.savefig('result/lineare_successo.png')
        plt.show()

        f.close()


def research_plot_chained_notsuccess(hash_dim):
    with open('Result/result_search_notsuccess_chained.txt', 'w') as f:
        f.write('')
        f.close()

    for num_ins in range(1,hash_dim,hash_dim//100):
        HashTable = [[] for _ in range(hash_dim)]
        load_factor = num_ins / hash_dim
        for ins in range(num_ins):
            rand_value = random.randrange(0, 10000,2)
            hash_key = rand_value % len(HashTable)
            HashTable[hash_key].append(rand_value)
        ricerca = 0
        i = 0
        while i < 200:
            print("entrato")
            search_value = random.randrange(0, 10000,2)
            hash_key = search_value % len(HashTable)
            list = HashTable[hash_key]
            edo=0
            if not list:
                print("lista vuota")
                ricerca=ricerca+1
                i=i+1

            else:
                for z,j in enumerate(list):
                    print(list)

                    if j == search_value:
                        print("cerco: ", search_value, "valore trovato in : ", hash_key, " alla posizione: ", z+1)
                        i = i-1
                        ricerca=ricerca-edo
                        break


                    else:
                        print("cerco : ", search_value, " non trovato")
                        ricerca = ricerca+1
                        edo=edo+1
                i=i+1

        print("Ricerca: ",ricerca)
        ricerca=ricerca/200
        result_linear = open('Result/result_search_notsuccess_chained.txt', 'a')
        result_linear.writelines(str(ricerca) + " ," + str(load_factor) + "\n")
        result_linear.close()
    with open('Result/result_search_notsuccess_chained.txt','r+') as f:
        lines = f.readlines()

        y_values = [line.split(",")[0] for line in lines]
        x_values = [line.split(",")[1] for line in lines]
        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace("'", "").replace("\n", "").replace(" ", "").replace("]","") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)


        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]

        # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
        fig, ax = plt.subplots()  # Create a figure and an axes.
        t1 =np.arange(0,1.1,0.1)
        t2 =np.arange(1,2.1,0.1)
        plt.plot(t1, t2,'red',label='1+α')
        ax.plot(x_values, y_values,'blue',label='Ricerca senza successo')# Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Comparazioni medie per ricerca')  # Add a y-label to the axes.
        ax.set_title("Comparazioni medie necessarie per una ricerca senza successo \n al variare del fattore di carico")  # Add a title to the axes.
        plt.yticks(np.arange(0,3,step=0.25))
        plt.xticks(np.arange(0,1.1, step=0.1))
        plt.legend(loc='upper left')
        plt.savefig('result/result_notsearch_combo.png')
        plt.show()

        f.close()


def research_plot_chained_success(hash_dim):
    with open('Result/result_search_success_chained.txt', 'w') as f:
        f.write('')
        f.close()

    for num_ins in range(1,hash_dim,hash_dim//100):
        HashTable = [[] for _ in range(hash_dim)]
        load_factor = num_ins / hash_dim
        for ins in range(num_ins):
            rand_value = random.randrange(0, 10000, 2)
            hash_key = rand_value % len(HashTable)
            HashTable[hash_key].append(rand_value)
        ricerca = 0
        i = 0
        while i < 200:

            search_value = random.randrange(0, 10000, 2)
            hash_key = search_value % len(HashTable)
            list = HashTable[hash_key]

            if not list:
                pass

            else:
                for z, j in enumerate(list):
                    print(list)

                    if j == search_value:
                        print("cerco: ", search_value, "valore trovato in : ", hash_key, " alla posizione: ", z + 1)
                        ricerca=ricerca+1
                        break


                    else:
                        print("cerco : ", search_value, " non trovato")
                        ricerca = ricerca + 1
                i = i + 1


        ricerca = ricerca / 200
        result_linear = open('Result/result_search_success_chained.txt', 'a')
        result_linear.writelines(str(ricerca) + " ," + str(load_factor) + "\n")
        result_linear.close()
    with open('Result/result_search_success_chained.txt', 'r+') as f:
        lines = f.readlines()

        y_values = [line.split(",")[0] for line in lines]
        x_values = [line.split(",")[1] for line in lines]
        x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
        y_values = [s.replace("'", "").replace("\n", "").replace(" ", "").replace("]", "") for s in y_values]

        x_values[:] = (elem[:5] for elem in x_values)

        x_values = [float(item) for item in x_values]
        y_values = [float(item) for item in y_values]


        fig, ax = plt.subplots()  # Create a figure and an axes.
        t1 = np.arange(0, 1.1, 0.1)
        t2 = np.arange(1, 2.1, 0.1)
        plt.plot(t1, t2, 'red', label='1+α')
        ax.plot(x_values, y_values, 'orange', label='Ricerca con successo')  # Plot some data on the axes.
        ax.set_xlabel('Load Factor:')  # Add an x-label to the axes.
        ax.set_ylabel('Comparazioni medie per ricerca')  # Add a y-label to the axes.
        ax.set_title("Comparazioni medie necessarie per una ricerca con successo \n al variare del fattore di carico")  # Add a title to the axes.
        plt.yticks(np.arange(0, 3, step=0.25))
        plt.xticks(np.arange(0, 1.1, step=0.1))
        plt.legend(loc='upper left')
        plt.savefig('result/result_success_chained_search.png')
        plt.show()

        f.close()
