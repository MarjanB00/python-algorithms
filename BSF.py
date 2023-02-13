import networkx as nx
import matplotlib.pyplot as py

# Pretrega po sirini (BFS Algoritam)  \  Marjan Bilafer 20/21

grafik={
        
        "A" : ["S", "B", "D"],
        "B" : ["A", "C", "D"],
        "C" : ["B"],
        "D" : ["A", "B", "E", "S"],
        "E" : ["D", "F"],
        "F" : ["E", "G"],
        "G" : ["F"],
        "S" : ["A", "D"]
}

vrijednosti={
    "G:F" : 3,
    "F:E" : 4,
    "E:D" : 2,
    "D:B" : 6,
    "D:A" : 5,
    "D:S" : 10,
    "A:B" : 4,
    "B:C" : 2,
    "A:S" :3
    }

def tezina(Roditelj, Dijete):
        try:
            vrijednosti[Dijete + ":" + Roditelj]
        except KeyError:
            broj = vrijednosti[Roditelj + ":" + Dijete]
        else: 
            broj=vrijednosti[Dijete + ":" + Roditelj]   
        return broj
    
    

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def crtanjeGrafa(grafik):
    
    Graph = nx.DiGraph()
    for x in grafik:
        for y in grafik[x]:
            Graph.add_edge(x, y)
    
        
    pos = nx.spring_layout(Graph)  
    nx.draw_networkx_nodes(Graph, pos, node_size=500)
    nx.draw_networkx_edges(Graph, pos, edgelist=Graph.edges(), edge_color="black")
    nx.draw_networkx_labels(Graph, pos)
    py.show()

def pretragaPoSirini(grafik, pocetniCvor, ciljaniCvor):
    provjeriti=[]
    provjeritiRoditelj=[]
    put={}
    D = nx.DiGraph()
    
    provjereno={pocetniCvor : 0,}
    for x in grafik[pocetniCvor]:
        provjeriti.append(x) 
        provjeritiRoditelj.append(pocetniCvor)
        put[x]=pocetniCvor
 
    

    while provjeriti:
        c = provjeriti.pop(0)
        if c != ciljaniCvor:
            if c not in list(provjereno.keys()):
                
                provjereno[c] = provjereno[provjeritiRoditelj[0]] + tezina(c, provjeritiRoditelj[0])
                put[c] = provjeritiRoditelj[0]

      
            elif provjereno[c] > provjereno[provjeritiRoditelj[0]] + tezina(c, provjeritiRoditelj[0]):
                provjereno[c] = provjereno[provjeritiRoditelj[0]] + tezina(c, provjeritiRoditelj[0])
                put[c] = provjeritiRoditelj[0]
                provjeritiRoditelj.pop(0)
                continue
            
            else:
                provjeritiRoditelj.pop(0)
                continue
            
            for x in grafik[c]:
                if x == provjeritiRoditelj[0]:
                    continue
                provjeritiRoditelj.append(c)
                provjeriti.append(x)
                
            provjeritiRoditelj.pop(0)

        else:
            put[c]=provjeritiRoditelj[0]
            provjereno[c] = provjereno[provjeritiRoditelj[0]] + tezina(c, provjeritiRoditelj[0])
            lista=(backtrace(put, pocetniCvor, ciljaniCvor))
            print(lista)
            print(provjereno)
            break

        
    for x in put:
        c = put[x]
        D.add_node(c)
        D.add_edge(c, x)
    pos = nx.nx_pydot.graphviz_layout(D, prog='dot')
    nx.draw(D, pos, with_labels=True, arrows=True)       
        
    

crtanjeGrafa(grafik)
pretragaPoSirini(grafik, "E", "C")


    


 
    