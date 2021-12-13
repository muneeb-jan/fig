#!/bin/sh

python3 test_fault.py read_EIO
python3 test_fault.py read_EINTR
python3 test_fault.py write_ENOSPC
python3 test_fault.py write_EIO
python3 test_fault.py select_ENOMEM
python3 test_fault.py malloc_ENOMEM
