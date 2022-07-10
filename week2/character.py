class Character():
    def __init__(self, character_name, real_name, super_power, weakness):
        self.name = character_name
        self.real_name = real_name
        self.super_power = super_power
        self.weakness = weakness

    def original(self, original_name):
            self.name = original_name


