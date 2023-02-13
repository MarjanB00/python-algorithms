import networkx as nx
import matplotlib.pyplot as py
import sys

# Pretrega po tezini (Uniform-Cost Search or Dijikstra's algorithm)  \  Marjan Bilafer 20/21

grafik={
        
        "A" : ["S", "B", "D"],
        "B" : ["A", "C", "D","T"],
        "C" : ["B", "T"],
        "D" : ["A", "B", "E", "S"],
        "E" : ["D", "F"],
        "F" : ["E", "G"],
        "G" : ["F"],
        "S" : ["A", "D"],
        "T" : ["B","C"]
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
    "A:S" : 3,
    "T:B" :-10,
    "T:C" : 6
    }


#Vraća vrijednost izmedju dvije tacke
def tezina(Roditelj, Dijete):
        try:
            vrijednosti[Dijete + ":" + Roditelj]
        except KeyError:
            broj = vrijednosti[Roditelj + ":" + Dijete]
        else: 
            broj=vrijednosti[Dijete + ":" + Roditelj]   
        return broj

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

def uniforma_pretraga(pocetni_cvor, konacni_cvor):
    #tacke koje se trebaju provjeriti(tacka : tezina do te tacke)
   provjeriti= {}
   #tacke koje su provjerene(tacka i tezina do te tacke)
   provjereno={}
   #tacke i roditelji do tih tacaka
   put={}
   max= sys.maxsize
   c=""
   
   D = nx.DiGraph()
   #ucitavanje djece od pocetne tacke u listu 
   for x in grafik[pocetni_cvor]:
       provjeriti[x] = tezina(pocetni_cvor, x)
       put[x]=pocetni_cvor
   
   while True:
       print(provjeriti)
       print(provjereno)
       print(put)
       print("----------------------------------------")
       #ucitavanje prve tezine od tacke iz liste provjeriti
       min = provjeriti[list(provjeriti.keys())[0]]
       
       #odredjivanje minimuma
       for x in provjeriti:
           if provjeriti[x] <=min:
               min =provjeriti[x]
               c = x
              
      
       if c == konacni_cvor:

           provjereno[c] = provjereno[put[c]] + tezina(c, put[c])
           print(provjereno)
           break
       else: 
           #ucitavanje djece od c
           for x in grafik[c]:

               if x==put[c] or x == pocetni_cvor:
                   continue
               
               if x in list(provjeriti.keys()) and (provjeriti[x] <  provjeriti.get(c, max) +  tezina(c, x)):

                   continue                             
              
                
               if x in list(provjereno.keys()):
                   if(provjereno[x] >  provjereno.get(c, max) +  tezina(c, x)):
                       provjereno[x] = provjereno[c] + tezina(c, x)
                       put[x] = c
                   continue  
                  
               print(x)
               provjeriti[x] = provjeriti[c] +  tezina(c, x)
               put[x] = c
        
       #tacka c se cuva u listu provjereno
       provjereno[c] = provjeriti[c]
       #tacka c se brise iz liste provjeriti
       del provjeriti[c]
       
   for x in put:
        c = put[x]
        D.add_node(c)
        D.add_edge(c, x)
   pos = nx.nx_pydot.graphviz_layout(D, prog='dot')
   nx.draw(D, pos, with_labels=True, arrows=True)           

       
crtanjeGrafa(grafik)
uniforma_pretraga("G", "C")   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    