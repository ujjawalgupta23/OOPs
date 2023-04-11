from phone_builder import *

phone1 = Phone()
# print(phone1)

phone2 = PhoneBuilder().set_os("Android").set_ram(8).set_processor("M1")\
    .set_battery(4000)\
    .get_phone()
    # .set_screen_size(6.2)\
print(phone2)

# print(phone1)