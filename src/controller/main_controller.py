from model.file_handler import FileHandler
from view.main_view import MainView
import osmnx as ox

class MainController:
    def __init__(self):
        self.view = MainView()

        # Configure event handlers
        self.view.search_button.config(command=self.search_city)

    def search_city(self):
        # Get the city name from the input field
        city_name = self.view.entry_city.get()

        # Create FileHandler instance with the city name
        file_handler = FileHandler(place_name=city_name)

        # Load or retrieve graph data
        graph = file_handler.load_graph_from_file()

        # If the graph data is not available, retrieve it using OSMnx
        if graph is None:
            graph = ox.graph_from_place(city_name, network_type='drive')
            file_handler.save_graph_to_file(graph)

        # Plot the graph
        ox.plot_graph(graph)

    # Add additional controller methods as needed
