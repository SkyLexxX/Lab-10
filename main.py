from ArtificialChristmasTree import ArtificialChristmasTree


def main():
    christmas_tree = ArtificialChristmasTree("Christmas_tree", 250, 169, "plastic", 5, "Germany", True)
    snow_christmas_tree = ArtificialChristmasTree("Christmas_tree_with_snow", 150, 100, "plastic")
    european_tree = ArtificialChristmasTree("European_tree")
    print(christmas_tree)
    print(snow_christmas_tree)
    print(european_tree)
    print(ArtificialChristmasTree.amount_of_trees)


if __name__ == '__main__':
    main()
