import subprocess
import threading

minerLocation = raw_input('Enter an absolute path to your mining batch file: ')

def checkAlive():
    #Checks if there is a process with the miner's name
    status = str(subprocess.check_output(['tasklist', '/fi', 'IMAGENAME eq EthDcrMiner64.exe']))

    #If our miner is not running, start it
    if 'No tasks are running' in status:
        subprocess.call([minerLocation])

    threading.Timer(5, checkAlive).start()

threading.Timer(5, checkAlive).start()
