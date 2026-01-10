from file_parsing.FileParser import FileParser as file_parser
from algorithms.DecisionTree import DecisionTree

def main():
    #fp = file_parser("data/spliceDTrainKIS.dat.txt")
    #dt = DecisionTree(fp.parse(), 5)
    #root = dt.train()
    training_data = [
        (1, "AAGCT"),
        (1, "AAGGT"),
        (0, "CCGCT"),
        (0, "TTGCT"),
        (1, "ACCCC"),
    ]

    dt = DecisionTree(training_data, max_depth=3)
    root = dt.train()

    print("--- WYNIK ---")
    print(f"Najlepsze pierwsze pytanie: Sprawdź pozycję {root.attribute_pos}")
    print(f"Jeśli litera to {root.split_condition_group} -> Idź w LEWO")
    print(f"W przeciwnym razie -> Idź w PRAWO")
main()