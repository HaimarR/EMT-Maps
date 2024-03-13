import os
import osmnx as ox

SAVE_FOLDER = "local_maps/"
FILE_EXTENSION = ".graphml"

class FileHandler:
    
    def __init__(self, place_name):
        self.__place_name = place_name
        self.__filename = None
        self.__save_folder = SAVE_FOLDER
        self.__file_ext = FILE_EXTENSION
        self.__full_path = None
    
    def getSaveFolder(self):
        return self.__save_folder
    
    def getFilename(self):
        if self.__filename == None:
            self.__filename = self.__place_name.replace(", ", "-")
            self.__filename = self.__filename.replace(" ", "_")
            self.__filename = self.__filename.replace(",", "-")
            self.__filename += self.__file_ext

        return self.__filename
    
    def getFullPath(self):
        if self.__full_path == None:
            self.__full_path = f"{self.__save_folder}{self.getFilename()}"
        return self.__full_path
    
    def save_graph_to_file(self, graph):
        ox.save_graphml(graph, self.getFullPath())

    def load_graph_from_file(self):
        path = self.getFullPath()
        if os.path.exists(path):
            return ox.load_graphml(path)
        else:
            graph = ox.graph_from_place(self.__place_name, network_type='drive')
            self.save_graph_to_file(graph)

        return graph