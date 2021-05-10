from matplotlib import pyplot as plt
import numpy as np

#TODO: menu per scelta hash lineare o hash concatenato
#TODO: sotto menù per inserimento cancellazzione e ricerca di entrambi i tipi di hash
#TODO:vedere come genera i file di test
#TODO:grafici per lineare e concatenato
#TODO: Commentare le parti importanti

with open("result.txt") as f:
    i = 0
    j = 0
    collision = []
    print(collision)
    load_factor1 = []
    load_factor2 = []

    for x in sorted(f):
        if 'srt' in x:
            break
        load_factor1.append(x.split(" ")[0])
        collision.append(x.split(" ")[1])

    for elem in load_factor1:
        load_factor2.append(elem[:3])

plt.xlabel("collision")
plt.ylabel("loadfactor")

plt.xticks(rotation='vertical')
plt.plot(collision, load_factor2)

# function to show the plot
plt.show()