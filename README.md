# power_on_wheel


## Resources
* using l298n motor driver
http://www.piddlerintheroot.com/l298n-dual-h-bridge/ </br>
* automatically connect bluetooth on start up
https://dietpi.com/phpbb/viewtopic.php?t=2966 </br?
```shell
crontab -e
@reboot echo "connect MAC-ADDRESS-OF-KEYBOARD" | bluetoothctl
```

## Usage
```shell
python3 test.py
python3 clienty.py # in another shell
```
