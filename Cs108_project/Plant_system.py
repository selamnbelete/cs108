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

        self.was_watered = False
        self.got_sunlight = False

    def water_plant(self):
        if self.stage == DEAD:
            return

        self.water += 15
        if self.water > 100:
            self.water = 100

        self.was_watered = True
        print("You watered the plant.")

        self.try_to_grow()

    def give_sunlight(self):
        if self.stage == DEAD:
            return

        self.sunlight += 15
        if self.sunlight > 100:
            self.sunlight = 100

        self.got_sunlight = True
        print("You gave sunlight to the plant.")

        self.try_to_grow()

    def try_to_grow(self):
        if self.stage == DEAD or self.stage == FULLY_GROWN:
            return

        if self.was_watered and self.got_sunlight:
            if self.stage == SEED:
                self.stage = GROWING
                self.size = 1
            elif self.stage == GROWING:
                self.size += 1

                if self.size >= 10:
                    self.stage = FULLY_GROWN

            self.water -= 10
            self.sunlight -= 10

            self.was_watered = False
            self.got_sunlight = False

    def update(self):
        if self.stage == DEAD:
            return

        self.water -= 0.005
        self.sunlight -= 0.003

        if self.water < 0:
            self.water = 0
        if self.sunlight < 0:
            self.sunlight = 0

        if self.water <= 5 or self.sunlight <= 5:
            self.health -= 0.01

        if self.health <= 0:
            self.health = 0
            self.stage = DEAD
            