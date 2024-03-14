import os
import unittest
from unittest.mock import patch, MagicMock
from src.model.file_handler import FileHandler

SAVE_FOLDER = "local_maps/"
PLACE_NAME = "San Sebastian, Guipuzcoa, Spain"
FILENAME = "San_Sebastian-Guipuzcoa-Spain"
FILE_EXT = ".graphml"
FULL_PATH = f"{SAVE_FOLDER}{FILENAME}{FILE_EXT}"

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.place_name = PLACE_NAME
        self.file_handler = FileHandler(self.place_name)

    def tearDown(self):
        pass

    def test_get_save_folder(self):
        self.assertEqual(self.file_handler.getSaveFolder(), "local_maps/")

    def test_get_filename(self):
        self.assertEqual(self.file_handler.getFilename(), f"{FILENAME}{FILE_EXT}")

    def test_get_full_path(self):
        self.assertEqual(self.file_handler.getFullPath(), FULL_PATH)

    @patch('src.model.file_handler.ox.save_graphml')
    def test_save_graph_to_file(self, mock_save_graphml):
        graph = MagicMock()
        self.file_handler.save_graph_to_file(graph)
        mock_save_graphml.assert_called_once_with(graph, "local_maps/San_Sebastian-Guipuzcoa-Spain.graphml")

    @patch('src.model.file_handler.ox.load_graphml')
    @patch('src.model.file_handler.os.path.exists')
    @patch('src.model.file_handler.ox.graph_from_place')
    def test_load_graph_from_file_existing(self, mock_graph_from_place, mock_exists, mock_load_graphml):
        mock_exists.return_value = True
        graph = MagicMock()
        mock_load_graphml.return_value = graph
        self.assertEqual(self.file_handler.load_graph_from_file(), graph)

    @patch('src.model.file_handler.ox.load_graphml')
    @patch('src.model.file_handler.os.path.exists')
    @patch('src.model.file_handler.ox.graph_from_place')
    def test_load_graph_from_file_non_existing(self, mock_graph_from_place, mock_exists, mock_load_graphml):
        mock_exists.return_value = False
        graph = MagicMock()
        mock_graph_from_place.return_value = graph
        self.assertEqual(self.file_handler.load_graph_from_file(), graph)