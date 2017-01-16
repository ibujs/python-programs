from subprocess import call
predef = [None, None, None, None]
def pyscp(file=predef[0], username=predef[1], ip=predef[2], destination=predef[3]):
    if len(predef) != 3:
        raise Exception("PySCP didn't recieve an argument or a predef list.")
    print("Initiating transfer. Please enter your password when asked.")
    call("scp %s %s@%s:%s" % (file, username, ip, destination), shell=True)