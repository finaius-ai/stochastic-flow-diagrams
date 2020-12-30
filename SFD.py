import networkx as nx
from matplotlib import pyplot as plt

def SFD_AR(p):
    """
    Generate autoregressive network
    :param p: lag length
    :return:
    """
    D = nx.DiGraph()

    for k in range(p):
        D.add_node('v%d'%(k+1), shape='diamond')
        D.add_edge('v%d'%k, 'v%d'%(k+1), weight=1,
                   label='o%d'%k, style='dashed', arrowhead='onormal'
                   )
        D.add_edge('v%d'%(k+1), 'v0', weight=1, label='a%d'%(k+1))
    return D


if __name__ == '__main__':
    graph = SFD_AR(3)
    nx.draw(graph, with_labels=True)
    plt.show()
