# Ethereum-Miner-Keep-Alive
The script restarts your ethereum miner in case of crashes. The script checks for crashes every 5 seconds and restarts the miner if 
a crash has occured. Currently only compatible with Claymore's miner. There are plans to add support for other mining software if there
is enough interest.

## Usage
You must have python installed and in the path before usage. Run `python alive.py` and enter the absolute path to your mining batch script
when prompted. The miner will start and the script will run in the background.
