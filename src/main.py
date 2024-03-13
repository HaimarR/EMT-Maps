import os
import osmnx as ox
from file_handler import FileHandler

def save_graph_to_file(G, filename):
    ox.save_graphml(G, filename)

def load_graph_from_file(filename):
    general_path = "local_maps/"
    full_path = general_path + filename
    if os.path.exists(full_path):
        return ox.load_graphml(full_path)
    else:
        return None

def main():
    # Define the place name
    place_name = "San Sebastian,Guipuzcoa,Spain"
    filename = "san_sebastian_graph.graphml"

    # Try to load the graph from file
    G = load_graph_from_file(filename)

    fh = FileHandler(place_name)
    G = fh.load_graph_from_file()

    # Plot the graph
    ox.plot_graph(G)

if __name__ == "__main__":
    main()
