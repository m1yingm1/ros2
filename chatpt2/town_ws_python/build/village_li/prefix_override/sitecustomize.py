import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ying/d2lros2/chatpt2/town_ws_python/install/village_li'
