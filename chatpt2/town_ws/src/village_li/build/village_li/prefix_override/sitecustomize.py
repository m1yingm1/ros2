import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ying/ros2/chatpt2/town_ws/src/village_li/install/village_li'
