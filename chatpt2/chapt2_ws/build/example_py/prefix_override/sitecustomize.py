import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ying/ros2/chatpt2/chapt2_ws/install/example_py'
