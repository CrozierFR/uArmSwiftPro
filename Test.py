import functools
from uarm.wrapper import SwiftAPI
swift = SwiftAPI()



#def print_callback(ret, key=None):
#    print('{}: {}'.format(key, ret))

#swift.waiting_ready(timeout=10)
#ret = swift.get_device_info()
#print('device info: {}'.format(ret))
#ret = swift.get_limit_switch()
#print('limit switch: {}'.format(ret))

#test=swift.set_acceleration(0.0001)
#swift.set_speed_factor(3)
#swift.set_position(114, -100, 50, wait=True)
#n=0
#while n <=200 :
#    swift.set_position(0, 1, 0, relative=True, wait=True, )
#    swift.get_position(wait=False, callback=functools.partial(print_callback, key='position'))
#    n = n + 1
    





swift.waiting_ready(timeout=10)
swift.set_position(140, -80, 50, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(114, 122, 0, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(300, 120, 50, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(114, 122, 0, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(110, 120, 50, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(114, 122, 0, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(220, 0, 50, wait=True)
swift.set_position(114, 122, 50, wait=True)
swift.set_position(114, 122, 0, wait=True)
swift.set_position(114, 122, 50, wait=True)



