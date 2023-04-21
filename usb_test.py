import os

usb_path = "/media/pi//USB_DISK/test_folder/log.txt"

# your code to generate data here
data = "teasting about write in pi\n"

with open(usb_path, 'a') as f:
    f.write(data)
    f.write("\n")