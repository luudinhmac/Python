import subprocess
import platform


def check_card():
    system = platform.system()
    output = ''
    if system =='Linux':
    #execute command "ip link show" to list all card network 
        output = subprocess.check_output(['ip','link','show'])
    elif system =='Windows':
        output = subprocess.check_output(['ipconfig','/all'])
    elif system == 'Darwin':
        output = subprocess.check_output(['ifconfig'])
    else: print("Hệ điều hành không hỗ trợ")
    print(output.decode('utf-8'))

check_card()