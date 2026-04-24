SEED = 0
GROWING = 1
FULLY_GROWN = 2

class Plant:
    def __init__(self):
        self.stage = SEED
        # Add other attributes here, such as health, size, etc.
        self.health = 100
        self.size = 0

    def grow(self):
        if self.stage == SEED:
            self.stage = GROWING
            print("The plant has sprouted from a seed.")
        elif self.stage == GROWING:
            self.size += 1
            self.health -= 5
            if self.size >= 10:
                self.stage = FULLY_GROWN
                print("The plant has fully grown.")

    def age(self):
        if self.stage != FULLY_GROWN:
            self.health -= 2
            if self.health <= 0:
                self.die()

    def die(self):
        print("The plant has died.")

# Main block to test the Plant class
if __name__ == "__main__":
    my_plant = Plant()
    
    for _ in range(15):
        my_plant.grow()
        print(f"Stage: {my_plant.stage}, Health: {my_plant.health}, Size: {my_plant.size}")
        my_plant.age()
