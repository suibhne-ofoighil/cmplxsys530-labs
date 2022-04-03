import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    g = nx.read_gml('polbooks/polbooks.gml')
    # pos = nx.kamada_kawai_layout(g)  # positions for all nodes
    # nx.draw_networkx(g, pos, with_labels=False, node_size=100)  # draw network
    # plt.show()

    #problem 3a
    # deg_seq = np.array([ d for n,d in g.degree() ])
    # (degrees, counts) = np.unique(ar=deg_seq, return_counts=True)
    #
    # plt.plot(degrees, counts)
    # plt.show()
    #
    # plt.loglog(degrees, counts)
    # plt.show()

    #problem 3b
    # cmap = 'magma'
    # pos = nx.kamada_kawai_layout(g)  # positions for all nodes
    # nx.draw_networkx_nodes(
    #     g, pos,
    #     node_color=list(nx.eigenvector_centrality(G=g, max_iter=600).values()),
    #     node_size=50,
    #     alpha=0.9,
    #     cmap=plt.get_cmap(cmap)
    # )
    # nx.draw_networkx_edges(g, pos)
    # plt.colorbar(mappable=plt.cm.ScalarMappable(cmap=cmap))
    # plt.show()

    #problem 3c
    # node_ideologies = [v['value'] for n, v in g.nodes(data=True)]
    #
    # def apply_color(value):
    #     if value == 'c':
    #         return 'red'
    #     elif value == 'l':
    #         return 'blue'
    #     else:
    #         return 'grey'
    #
    # node_colors = [ apply_color(v) for v in node_ideologies ]
    #
    # pos = nx.kamada_kawai_layout(g)  # positions for all nodes
    # nx.draw_networkx_nodes(
    #     g, pos,
    #     node_color=node_colors,
    #     node_size=50,
    #     alpha=0.8,
    # )
    # nx.draw_networkx_edges(g, pos)
    # plt.show()
    #
    # print(nx.attribute_assortativity_coefficient(g, 'value'))

    # problem 3d
    communities = nx.community.greedy_modularity_communities(g)

    colors = ['red', 'blue', 'violet', 'orange']

    community_mapping = {}

    for i,c in enumerate(communities):
        for n in c:
            community_mapping[n] = i

    nx.set_node_attributes(g, community_mapping, name='community')
    node_colors = [ colors[v['community']] for n,v in g.nodes(data=True) ]

    pos = nx.kamada_kawai_layout(g)  # positions for all nodes
    nx.draw_networkx_nodes(
        g, pos,
        node_color=node_colors,
        node_size=50,
        alpha=0.8,
    )
    nx.draw_networkx_edges(g, pos)
    plt.show()



