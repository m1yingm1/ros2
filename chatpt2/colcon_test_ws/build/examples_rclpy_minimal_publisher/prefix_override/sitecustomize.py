import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ying/d2lros2/chatpt2/colcon_test_ws/install/examples_rclpy_minimal_publisher'
