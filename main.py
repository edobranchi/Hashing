from matplotlib import pyplot as plt
import numpy as np
import Linear_Hash
import Chained_Hash

#TODO:vedere come genera i file di test
#TODO:grafici per lineare e concatenato
#TODO: Commentare le parti importanti

def print_menu():  ## Your menu design here

    print(30 * "-", "MENU", 30 * "-")
    print("1. Popolazione Hash Lineare")
    print("2. Popolazione Hash Concatenato")
    print("3. exit")
    print(67 * "-")
def print_sub_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Search")
    print("2. Delete")
    print("3. Display")
    print("4. exit")
    print(67 * "-")
loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = int(input("Enter your choice [1-7]: "))

    if choice == 1:
        print("Creazione Hash lineare")
        Linear_Hash.insert_generation(50)
        annidated_loop= True
        while annidated_loop:
            print_sub_menu()
            choice_linear= int(input("Enter your choice [1-7]: "))
            if choice_linear == 1:
                search_value = int(input("Inserire il valore da cercare:"))
                Linear_Hash.linear_search(search_value)
            elif choice_linear == 2:
                Linear_Hash.linear_delete()
            elif choice_linear == 3:
                Linear_Hash.linear_display()
            elif choice_linear==4:
                print("Torno al menu precedente")
                annidated_loop=False
            else:
                input("Nessuna scelta corrispondente riprovare")



    if choice == 2:
        print("Creazione Hash concatenato")
        # TODO:Chiamare creazione
        annidated_loop=True
        while annidated_loop:
            print_sub_menu()
            choice_linear= int(input("Enter your choice [1-7]: "))
            if choice_linear == 1:
                Chained_Hash.hash_search()
            elif choice_linear == 2:
                Chained_Hash.hash_delete()
            elif choice_linear == 3:
                Chained_Hash.display_hash()
            elif choice_linear==4:
                print("Torno al menu precedente")
                annidated_loop=False
            else:
                input("Nessuna scelta corrispondente riprovare")
    elif choice==3:
        print("Fine programma, esco.")
        loop=False

# with open("result.txt") as f:
#     i = 0
#     j = 0
#     collision = []
#     print(collision)
#     load_factor1 = []
#     load_factor2 = []
#
#     for x in sorted(f):
#         if 'srt' in x:
#             break
#         load_factor1.append(x.split(" ")[0])
#         collision.append(x.split(" ")[1])
#
#     for elem in load_factor1:
#         load_factor2.append(elem[:3])
#
# plt.xlabel("collision")
# plt.ylabel("loadfactor")
#
# plt.xticks(rotation='vertical')
# plt.plot(collision, load_factor2)
#
# # function to show the plot
# plt.show()