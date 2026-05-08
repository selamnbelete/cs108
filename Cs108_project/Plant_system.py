SEED = 0
GROWING = 1
FULLY_GROWN = 2
DEAD = 3

class Plant:
    def __init__(self):
        self.stage = SEED
        
        self.health = 100
        self.size = 0
        self.water = 50
        self.sunlight = 50

    def water_plant(self):
        self.water += 15
        if self.water > 100:
            self.water = 100
        print("You watered the plant.")

    def give_sunlight(self):
        self.sunlight += 15
        if self.sunlight > 100:
            self.sunlight = 100
        print("You gave sunlight to the plant.")

    def grow(self):
        if self.stage == DEAD:
            return

        if self.water >= 20 and self.sunlight >= 20:
            if self.stage == SEED:
                self.stage = GROWING
                self.size = 1
                print("The plant has sprouted.")
            elif self.stage == GROWING:
                self.size += 1
                print("The plant is growing.")

                if self.size >= 10:
                    self.stage = FULLY_GROWN
                    print("The plant is fully grown.")

            self.water -= 10
            self.sunlight -= 10
        else:
            self.health -= 10
            print("The plant needs more water or sunlight.")

        if self.health <= 0:
            self.stage = DEAD

    def update(self):
        if self.stage == DEAD:
            return

    # water and sunlight slowly go down
        self.water -= 0.01
        self.sunlight -= 0.008

    # plant loses health if needs are low
        if self.water <= 10 or self.sunlight <= 10:
            self.health -= 0.03

    # automatic growth
        if self.water >= 30 and self.sunlight >= 30:
            self.size += 0.01

            if self.stage == SEED and self.size >= 1:
                self.stage = GROWING

            if self.stage == GROWING and self.size >= 10:
                self.stage = FULLY_GROWN
        # death
        if self.health <= 0:
            self.stage = DEAD
            