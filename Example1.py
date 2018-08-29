from uarm.wrapper import SwiftAPI
swift = SwiftAPI()


swift.waiting_ready(timeout=10)
swift.set_position(100, -120, 50, wait=True)
test=swift.get_position()
print(test)
swift.set_position(300, -120, 50, wait=True)
test=swift.get_position()
print(test)
swift.set_position(300, 120, 100, wait=True)
test=swift.get_position()
print(test)
swift.set_position(100, 120, 100, wait=True)
test=swift.get_position()
print(test)
swift.set_position(120, 0, 50, wait=True)
test=input("the pump will be set on, press enter to continue")
swift.set_pump(on=True)
swift.set_position(200, 0, 50, wait=True)
test=input("the pump will be set off, press enter to continue")
swift.set_pump(on=False)
swift.set_position(120, 0, 50, wait=True)





