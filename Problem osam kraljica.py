import numpy as np
import matplotlib.pyplot as plt


tabla = np.matrix([
      [0,0,0,0,0,0,0,0], 
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]
    ])


napadi = np.matrix([
      [0,0,0,0,0,0,0,0], 
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]
    ])


def draw_board(rasporedjene_kraljice):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, 9, 1))
    ax.set_yticks(np.arange(0, 9, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, color='black', linewidth=1, which='both')

    for i in range(0, 8):
        for j in range(0, 8):

            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color='white'))
            else:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color='gray'))
            
            if rasporedjene_kraljice[i,j]==1:
                ax.text(i+0.5, j+0.5, "♛", ha='center', va='center', fontsize=20)
                
    plt.show()    
            
def susjedi(tabla_dva):
    brojac=0
    
    for red in tabla_dva:
        count=0
        for j in np.nditer(red):
            if j == 1:
                count=count+1
        count=count-1
        if count>0:
            brojac=brojac + (count*count+count)/2
            
    diagonale = [tabla_dva[::-1,:].diagonal(i) for i in range(-tabla_dva.shape[0]+1, tabla_dva.shape[1])]
    diagonale.extend(tabla_dva.diagonal(i) for i in range(tabla_dva.shape[1]-1,-tabla_dva.shape[0],-1))
    lista_diagonala =  [n.tolist() for n in diagonale]
    
    for d in lista_diagonala:
        count=0
        for j in np.nditer(d):
            if j == 1:
                count=count+1
        count=count-1
        if count>0:
            brojac= brojac + (count*count+count)/2

    return brojac
    
def generisanje_napadi_matrice(tabla):
    lista = np.where(tabla==1)
    rasporedjeni_brojevi = np.array([], dtype='int16')
    for x in range(np.shape(tabla)[0]):
        for i in lista[1]:
            if x==i:
                rasporedjeni_brojevi= np.append(rasporedjeni_brojevi, lista[0][np.where(lista[1]==x)])
        
    i=0 
    while i<np.shape(tabla)[0]:
        tabla.itemset((rasporedjeni_brojevi[i], i),0)
        for x in range (np.shape(tabla)[0]):
            tabla.itemset((x,i),1)
            napadi.itemset((x,i), susjedi(tabla))
            tabla.itemset((x,i),0)
        tabla.itemset((rasporedjeni_brojevi[i], i),1)
        i=i+1
    
    return napadi

def generisanje_nasumicne_table(nasumicno):
    j=0
    for i in nasumicno:
        tabla.itemset((i,j), 1)
        j=j+1
    return tabla
  
    
def rasporedi(tabla, matrica_napadi):
    
    rng = np.random.default_rng()
    mjesta_minimuma = []
    min =  np.amin(matrica_napadi)

    i=0
    for x in matrica_napadi:
        j=0
        for y in np.nditer(x):
            if min == y:
                mjesta_minimuma.append((i,j))
            j=j+1
        i=i+1
    
    kordinate = mjesta_minimuma[int(rng.integers(low=0, high= len(mjesta_minimuma), size= 1 ))]
    kolona = tabla[:, kordinate[1]]
    kolona = np.asarray(kolona).reshape(-1)
    b = np.where(kolona==1)

    tabla.itemset((int(b[0]),kordinate[1]),0)
    tabla.itemset(kordinate[0],kordinate[1], 1)


    return tabla



def algoritam():
    tacna_resenja=0
    brojac=0
    while brojac<=100:
        print(brojac)
        brojac=brojac+1
        rng = np.random.default_rng()
        nova_tabla = generisanje_nasumicne_table(rng.integers(low=0, high=np.shape(tabla)[0], size=np.shape(tabla)[0]))
        matrica_napadi = generisanje_napadi_matrice(nova_tabla)
        for p in range(8):
            rasporedjene_kraljice = rasporedi(nova_tabla, matrica_napadi)
                        
            matricaNapadaRasporedjenihKraljica=generisanje_napadi_matrice(rasporedjene_kraljice)
            count = np.count_nonzero(matricaNapadaRasporedjenihKraljica == 0)
            if count == 8:
                
                tacna_resenja=tacna_resenja+1
                draw_board(rasporedjene_kraljice)
                print(rasporedjene_kraljice)    

                break

               
            nova_tabla = rasporedjene_kraljice
            matrica_napadi = generisanje_napadi_matrice(nova_tabla)
      
    print(tacna_resenja)      

algoritam()








