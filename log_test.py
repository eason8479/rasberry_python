import logging

# setting log, make it write to file with format, without showing on console

# set path of log file
log_file = '/media/pi/log_usb/test.log'
log_file = '/run/media/eason/log_usb/test.log'
# set format of log
log_format = '%(asctime)s  %(levelname)s %(message)s'
# set level of log
log_level = logging.DEBUG
# set log
logging.basicConfig(filename=log_file, format=log_format, level=log_level)

# write log
for i in range (100):
    logging.info(f'log message {i}')
