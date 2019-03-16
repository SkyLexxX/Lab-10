class ArtificialChristmasTree:
    amount_of_trees = 0

    def __init__(self, name="ChristmasTree", height=200, price=157, material="Polyvinyl_Chloride", radius=4,
                 country="Poland", fire_proof=False):
        self.name = name
        self.height = height
        self.price = price
        self.material = material
        self.radius = radius
        self.country = country
        self.fireProof = fire_proof

    def __del__(self):
        print("Destructor " + self.name + " deleted")

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def output_static_field():
        return ArtificialChristmasTree.amount_of_trees


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
