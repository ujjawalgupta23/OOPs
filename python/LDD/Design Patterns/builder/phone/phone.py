class Phone:
    def __init__(self, os=None, ram=None, processor=None, screen_size=None, battery=None):
        self.os = os
        self.ram = ram
        self.processor = processor
        self.screen_size = screen_size
        self.battery = battery

    def __str__(self):
        return f"os= '{self.os}', ram= '{self.ram}', processor = '{self.processor}', " \
               f"screen size= '{self.screen_size}', battery= '{self.battery}'"
