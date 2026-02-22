# 3.1
import sys
import networkx as nx
from PyQt6.QtWidgets import QApplication
from visualiser import Visualiser

def main():
    G = nx.Graph()
    edges = [ # real distances
        ("A", "B", 1),
        ("A", "C", 10),
        ("B", "D", 2),
        ("C", "D", 1),
        ("B", "E", 5),
        ("C", "F", 2),
        ("D", "E", 3),
        ("D", "F", 8),
        ("E", "G", 1),
        ("F", "G", 1),
        ("F", "H", 2),
        ("G", "H", 1),
    ]
    for from_node, to_node, weight in edges:
        G.add_edge(from_node, to_node, weight=weight)

    heuristic = {  # direction distances
        "A": 10,
        "B": 8,
        "C": 5,
        "D": 7,
        "E": 3,
        "F": 6,
        "G": 1,
        "H": 0,
    }

    app = QApplication(sys.argv)
    viz = Visualiser(G, edges, heuristic, fixed_start='A', fixed_end='H')
    viz.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()
