from phone import *


class PhoneBuilder:
    def __init__(self, phone=Phone()):
        self.phone = phone

    def set_os(self, os):
        self.phone.os = os
        return self

    def set_ram(self, ram):
        self.phone.ram = ram
        return self

    def set_processor(self, processor):
        self.phone.processor = processor
        return self

    def set_screen_size(self, screen_size):
        self.phone.screen_size = screen_size
        return self

    def set_battery(self, battery):
        self.phone.battery = battery
        return self

    def get_phone(self):
        # return Phone(self.os, self.ram, self.processor, self.screen_size, self.battery)
        return self.phone
