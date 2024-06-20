import random

class Cat:
    def __init__(self, name, age=1, fullness=40, happiness=40, sleeping=False):
        self.name = name
        self.age = age
        self.fullness = fullness
        self.happiness = happiness
        self.sleeping = sleeping

    def play(self):
        if self.sleeping:
            self.happiness -= 5
            self.wake_up()
        else:
            self.happiness += 15
            self.fullness -= 10
            if random.randint(1, 3) == 3:
                self.happiness = 0
        self._normalize()

    def feed(self):
        if not self.sleeping:
            self.fullness += 15
            self.happiness += 5
            if self.fullness > 100:
                self.happiness -= 30
        self._normalize()

    def sleep(self):
        self.sleeping = True

    def wake_up(self):
        self.sleeping = False

    def _normalize(self):
        self.fullness = max(0, min(self.fullness, 100))
        self.happiness = max(0, min(self.happiness, 100))

    def get_image_url(self):
        if self.happiness < 40:
            return '/static/images/sad_cat.png'
        elif self.happiness > 60:
            return '/static/images/happy_cat.png'
        else:
            return '/static/images/neutral_cat.jpeg'

    def to_dict(self):
        return {
            'cat_name': self.name,
            'cat_age': self.age,
            'cat_fullness': self.fullness,
            'cat_happiness': self.happiness,
            'cat_sleeping': self.sleeping,
            'cat_image_url': self.get_image_url()
        }

    @classmethod
    def from_dict(cls, data):
        cat = cls(
            name=data['cat_name'],
            age=data.get('cat_age', 1),
            fullness=data.get('cat_fullness', 40),
            happiness=data.get('cat_happiness', 40),
            sleeping=data.get('cat_sleeping', False)
        )
        return cat
