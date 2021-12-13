
import sys
import subprocess
import os


a = subprocess.run(["tar","-xf","content.tar"])
print("Injected: " + sys.argv[0])



try:
    if sys.argv[0] == "read_EIO":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EIO.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    elif sys.argv[0] == "read_EINTR":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EINTR.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    elif sys.argv[0] == "write_ENOSPC":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EINTR.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    elif sys.argv[0] == "write_EIO":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EINTR.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    elif sys.argv[0] == "select_ENOMEM":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EINTR.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    elif sys.argv[0] == "select_ENOMEM":
        os.environ['LD_PRELOAD'] = 'faultinjection/fi_read_EINTR.so'
        x = subprocess.run(["tar", "-cf", "temp.tar", "content"], capture_output=True, timeout=5)
        if x.returncode  == 0:
            print("ProcessState: success")
        else:
            print("ProcessState: exited")
    else:
        print ("Incorrect input.")

except subprocess.TimeoutExpired:
    print("ProcessState: timeout")

finally:
    if os.path.isfile("temp.tar")==False:
        state = "no_tar"
    elif os.path.getsize("temp.tar") == 0:
        state = "empty"
    else:
        diff = subprocess.run(["tar","df","temp.tar","content"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if diff == None:
            state = "okay"
        else:
            state = "corrupted"
    
    print("TarState: " + state)