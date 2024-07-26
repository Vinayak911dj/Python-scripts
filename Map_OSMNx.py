import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place='Bremerhaven,Bremen'
G=ox.graph_from_place(place, network_type="walk")
orig_cord=[53.531418,8.599998]
dist_cord=[53.540442,8.583119]

orig_node=ox.distance.nearest_nodes(G,X=orig_cord[1],Y=orig_cord[0])
dist_node=ox.distance.nearest_nodes(G,X=dist_cord[1],Y=dist_cord[0])

routes_nodes=ox.shortest_path(G,orig_node,dist_node, weight='length')

fig,ax=ox.plot_graph_route(G,routes_nodes,route_color="r",route_linewidth=6,node_size=0)

# plt.show()
