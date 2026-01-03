from file_parsing.FileParser import FileParser as file_parser
from algorithms.DecisionTree import DecisionTree as decision_tree

def main():
    fp = file_parser("data/spliceDTrainKIS.dat.txt")
    tree = decision_tree(fp.parse())

main()