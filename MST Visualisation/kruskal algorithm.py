import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def kruskal_mst(graph):
    mst = nx.Graph()
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    disjoint_sets = {node: {node} for node in graph.nodes()}

    for edge in edges:
        u, v, weight = edge
        if disjoint_sets[u] != disjoint_sets[v]:
            mst.add_edge(u, v, weight=weight['weight'])
            union_set = disjoint_sets[u].union(disjoint_sets[v])
            for node in union_set:
                disjoint_sets[node] = union_set

    return mst

def update(frame):
    plt.clf()
    current_edges = list(mst.edges())[:frame]
    all_edges = G.edges(data=True)
    
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold', node_size=700, font_size=8, node_color='skyblue')
    nx.draw_networkx_edges(G, pos=pos, edgelist=all_edges, edge_color='gray', width=1, alpha=0.5)
    nx.draw_networkx_edges(G, pos=pos, edgelist=current_edges, edge_color='r', width=2)
    
    edge_labels = {(edge[0], edge[1]): str(edge[2]['weight']) for edge in all_edges}
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='green')
    
    plt.title("Kruskal's Algorithm - Step {}".format(frame))
    plt.pause(1)

# Example usage
G = nx.Graph()
G.add_edges_from([(0, 1, {'weight': 2}), (0, 2, {'weight': 3}), (1, 2, {'weight': 1}), (1, 3, {'weight': 1}),
                     (2, 3, {'weight': 4}), (2, 4, {'weight': 5}), (3, 4, {'weight': 2})])

pos = nx.spring_layout(G)
mst = kruskal_mst(G)

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=len(mst.edges()) + 1, repeat=True)
plt.show()
