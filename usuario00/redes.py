# coding: utf-8
import networkx as nx            # biblioteca de redes
import numpy as np               # biblioteca numérica
import matplotlib.pyplot as plt  # biblioteca para graficar

# muestra los dibujos dentro de esta ventana y no en una nueva
get_ipython().magic('matplotlib inline')

def a_matriz(G):
    "Devuelve nodos_ordenados, matriz de 0s y 1s."
    nodos_ordenados = np.sort(G.nodes())
    return {"nodos":nodos_ordenados,
            "matriz":np.array(nx.to_numpy_matrix(G, nodelist=nodos_ordenados))}

def a_lista(G):
    "Devuelve nodos_ordenados, lista de listas de etiquetas."
    orden_nodos = np.array(G.nodes()).argsort()
    return {"nodos":np.array(G.nodes())[orden_nodos],
            "lista":np.array(G.adjacency_list())[orden_nodos]}

def imprime_matriz_de_adyacencia(G):
    # Matriz de adyacencia
    m = a_matriz(G)
    ## imprimimos la matriz con los nodos en orden
    print("    ", end="")
    for i in m["nodos"]:
        print(i, end="   ")
    print()
    for nodo, renglon in zip(m["nodos"], m["matriz"]):
        print(str(nodo), str(renglon))

def imprime_lista_de_adyacencia(G):
    # Lista de adyacencia
    m = a_lista(G)
    ## imprimimos la lista con nodos en orden
    for nodo, lista in zip(m["nodos"], m["lista"]):
        print(str(nodo) + " : " + str(lista))

def imprime_adyacencia(G):
    print("Matriz de Adyacencia:")
    imprime_matriz_de_adyacencia(G)
    print("Lista de Adyacencia:")
    imprime_lista_de_adyacencia(G)
    
def desde(dic, digráfica=False):
    "Construye (di)gráfica a partir de una lista, una matriz o un dic."
    G = nx.DiGraph() if digráfica else nx.Graph()
    if isinstance(dic, dict): # es diccionario?
        if "nodos" in dic.keys(): # esta el item "nodos"?
            nodos = dic["nodos"]
        else:
            nodos = range(len(dic["lista"]))
        if "lista" in dic.keys(): # esta el item "lista"?
            aristas = ((nodos[i], vecino) for i in range(len(nodos)) for vecino in dic["lista"][i])
        else:  # matriz
            bmat = dic["matriz"]==1  # arreglo booleano
            aristas = ((nodos[i], vecino) for i in range(len(nodos)) for vecino in nodos[bmat[i]])
    else: # asumimos que se dá la lista o la matriz directo, etiquetas son enteros de 0 a n-1
        nodos = range(len(dic))
        m = len(dic[0])
        if all(len(dic[i]) == m for i in range(len(nodos))) and             set(e for l in dic for e in set(l)) == {0,1}: # reng de la misma long y conteniendo sólo 0,1
                bmat = dic == 1
                n=range(len(nodos))
                aristas =((nodos[a], nodos[b]) for a in n for b in n if bmat[a,b])
                #aristas = ((nodos[i], vecino) for i in range(len(nodos)) for vecino in nodos[bmat[i]])
        else:
            aristas = ((nodos[i], vecino) for i in range(len(nodos)) for vecino in dic[i])
    G.add_nodes_from(nodos)
    G.add_edges_from(aristas)
    return G
