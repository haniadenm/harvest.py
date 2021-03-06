############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
# We need to add pairing in the def_init function.

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

    def __repr__(self):
        return f"<{self.color}>"


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk_melon = MelonType("musk", 1998, "green", True, True, "muskmelon")
    musk_melon.add_pairing("mint")
    all_melon_types.append(musk_melon)

    casaba_melon = MelonType("cas", 2003, "orange", True, False, "casaba")
    casaba_melon.add_pairing("strawberries")
    casaba_melon.add_pairing("mint")
    all_melon_types.append(casaba_melon)

    crenshaw_melon = MelonType("cren", 1996, "green", True, False, "crenshaw")
    crenshaw_melon.add_pairing("proscuitto")
    all_melon_types.append(crenshaw_melon)

    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, 
                                  "yellow watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    # iterate through list of melons
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for i in range(len(melon.pairings)):
            print(f"-{melon.pairings[i]}")


print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    all_melon_dictonary = {}

    for melon in melon_types:
        all_melon_dictonary[melon.code] = melon.name

    return all_melon_dictonary


make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, code, color_rating, shape_rating, field, harvestor):

        self.sellable = None
        self.color_rating = color_rating
        self.shape_rating = shape_rating
        self.field = field
        self.harvestor = harvestor
        self.code = code

    def __repr__(self):
        return f'<{self.field}>'

    def is_sellable(self, sellable):
        for melon in object:
            if self.color_rating > 5 and self.shape_rating > 5 and self.field != 3:
                self.sellable = True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_dictionary = make_melon_type_lookup(melon_types)

    melon1 = Melon(melon_dictionary["yw"], 7, 8, 2, "Sheila")
    melon2 = Melon(melon_dictionary["yw"], 4, 3, 2, "Sheila")
    melon3 = Melon(melon_dictionary["yw"], 8, 9, 3, "SHeila")
    melon4 = Melon(melon_dictionary["cas"], 6, 10, 35, "Sheila")
    melon5 = Melon(melon_dictionary["cren"], 9, 8, 35, "Michael")
    melon6 = Melon(6, "cren", 2, 8, 35, "Michael")
    melon7 = Melon(7, "cren", 3, 2, 4, "Michael")
    melon8 = Melon(8, "musk", 7, 6, 5, "Michael")
    melon9 = Melon(9, "yw", 10, 7, 3, "Sheila")

    melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    return melons

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



