class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will call the setter
        self.condition = "New"  # Initialize condition attribute

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")  # Message when cobbling
        self.condition = "New"  # Set condition to "New" after repair

# Example usage:
stan_smith = Shoe("Adidas", 9)
stan_smith.cobble()
print(stan_smith.condition)  # Output: New
