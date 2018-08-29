from uarm.wrapper import SwiftAPI
swift = SwiftAPI()


swift.waiting_ready(timeout=10)
swift.set_position(140, 0, 10, wait=True)
swift.set_position(320, 0, 10, wait=True)
swift.set_position(140, 0, 10, wait=True)
swift.set_speed_factor(4)
input("now the speed of the arm has been multiply by 4, it will move faster. press enter to continue")
swift.set_position(140, 0, 10, wait=True)
swift.set_position(320, 0, 10, wait=True)
swift.set_position(140, 0, 10, wait=True)
swift.set_speed_factor(1)

