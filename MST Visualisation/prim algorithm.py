import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def prim_mst(graph):
    mst = nx.Graph()
    start_node = list(graph.nodes())[0]
    visited = set([start_node])

    while len(visited) < len(graph.nodes()):
        edge_candidates = []
        for node in visited:
            edge_candidates.extend(graph.edges(node, data=True))

        edge_candidates = sorted(edge_candidates, key=lambda x: x[2]['weight'])
        for edge in edge_candidates:
            if edge[1] not in visited:
                mst.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
                visited.add(edge[1])
                break

    return mst

def update(frame):
    plt.clf()
    current_edges = list(mst.edges())[:frame]
    
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold', node_size=700, font_size=8, node_color='skyblue')
    nx.draw_networkx_edges(G, pos=pos, edgelist=current_edges, edge_color='r', width=2)
    
    edge_labels = {(edge[0], edge[1]): edge[2]['weight'] for edge in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='green')
    
    
    
    plt.title("Prim's Algorithm - Step {}".format(frame))
    plt.pause(1)


G = nx.Graph()
G.add_edges_from([(0, 1, {'weight': 2}), (0, 2, {'weight': 3}), (1, 2, {'weight': 1}), (1, 3, {'weight': 1}),
                     (2, 3, {'weight': 4}), (2, 4, {'weight': 5}), (3, 4, {'weight': 2})])


pos = nx.spring_layout(G)
mst = prim_mst(G)

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=len(mst.edges()) + 1, repeat=True)
plt.show()
