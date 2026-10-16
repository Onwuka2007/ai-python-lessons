from operator import add


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # Overloaded (+) operators
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.sickles + other.sickles

        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 70)
weasly = Vault(100, 50, 50)

total = potter + weasly
print(total)
