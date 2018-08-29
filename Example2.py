from uarm.wrapper import SwiftAPI
swift = SwiftAPI()


swift.waiting_ready(timeout=10)
swift.set_position(140, 0, 10, wait=True)
swift.set_servo_detach()
test1=swift.get_position()
print(test1)
test2=swift.get_servo_angle()
print(test2)
test=input("now the uArm is detached, that mean you can freely move the arm without the servo-motors blocking it. for the next step, deplace the arm in another position than before and type enter to continue")
test1=swift.get_position()
print(test1)
test2=swift.get_servo_angle()
print(test2)
test=input("has you can see, the arm has moved but the position is the same : after detached the arm, if you move it you can only have the servo-motors angles. type enter to continue BUT be careful : the arm will be attach so don't block it in any way.")
swift.set_servo_attach()
swift.set_position(140, 0, 50, wait=True)


