class ColdNoodles:
    def __init__(self, builder):
        self.egg = builder.egg
        self.beef = builder.beef

    def __str__(self):
        egg = "yes" if self.egg else "no"
        beef = "yes" if self.beef else "no"
        return f"egg: {egg}, beef: {beef}"
    class Builder:
        def __init__(self):
            self.egg = False
            self.beef = False

        def add_egg(self):
            self.egg = True
            return self

        def add_beef(self):
            self.beef = True
            return self
        def builder(self):
            return ColdNoodles(self)

cold_noodles = ColdNoodles.Builder().add_beef().add_egg().builder()
print(cold_noodles)






