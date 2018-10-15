import os


def check_ping():
    hostname = "www.google.com"
    response = os.system("ping -c 5 " + hostname)
    # and then check the response...
    if response == 0:
        print(True)
    else:
        print(False)
