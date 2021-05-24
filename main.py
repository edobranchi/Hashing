import Linear_Hash
import Chained_Hash
import plot

def print_menu():  ## Your menu design here

    print(30 * "-", "MENU", 30 * "-")
    print("1. Popolazione Hash Lineare")
    print("2. Popolazione Hash Concatenato")
    print("3. Grafici Hash Lineare")
    print("4. Grafici Hash Concatenato")
    print("5. exit")
    print(67 * "-")

def print_sub_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Ricerca Valore:")
    print("2. Cancella valore:")
    print("3. Stampa la tabella")
    print("4. Uscita")
    print(67 * "-")
loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        print("Creazione Hash lineare")
        hash_dim = int(input("Dimensione tabella hash desiderata:"))
        num_ins = int(input("Numero di inserimenti: "))
        success_bool = Linear_Hash.insert_generation(hash_dim,num_ins)
        if success_bool==True:
            annidated_loop = True
        else:
            annidated_loop= False

        while annidated_loop:
            print_sub_menu()
            choice_linear= int(input("Enter your choice [1-3]: "))

            if choice_linear == 1:
                search_value = int(input("Inserire il valore da cercare:"))
                Linear_Hash.linear_search(search_value)

            elif choice_linear == 2:
                delete_value = int(input("Inserire il valore da eliminare:"))
                Linear_Hash.linear_delete(delete_value)

            elif choice_linear == 3:
                Linear_Hash.linear_display()

            elif choice_linear==4:
                print("Torno al menu precedente")
                annidated_loop=False

            else:
                print("Nessuna scelta corrispondente riprovare...")


    if choice == 2:
        print("Creazione Hash concatenato")
        hash_dim = int(input("Dimensione tabella hash desiderata:"))
        num_ins = int(input("Numero di inserimenti: "))
        Chained_Hash.list_creation(hash_dim)
        Chained_Hash.insert(num_ins)
        annidated_loop=True

        while annidated_loop:
            print_sub_menu()
            choice_linear= int(input("Enter your choice [1-3]: "))

            if choice_linear == 1:
                search_num = int(input("Inserisci il valore da cercare: "))
                Chained_Hash.hash_search(search_num)

            elif choice_linear == 2:
                del_num = int(input("Inserisci il valore da eliminare: "))
                Chained_Hash.hash_delete(del_num)

            elif choice_linear == 3:
                Chained_Hash.display_hash()

            elif choice_linear==4:
                print("Torno al menu precedente")
                annidated_loop=False

            else:
                input("Nessuna scelta corrispondente riprovare")

    if choice == 3:
        hash_dim = int(input("Inserisci la dimensione della tabella:"))
        num_ins = int(input("Inserisci il numero di inserimenti da creare:"))
        plot.linear_plot(hash_dim,num_ins)

    if choice == 4:
        hash_dim = int(input("Inserisci la dimensione della tabella:"))
        num_ins = int(input("Inserisci il numero di inserimenti da creare:"))
        plot.chained_plot(num_ins,hash_dim)

    elif choice==5:
        print("Fine programma, esco.")
        loop=False

