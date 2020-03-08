from pybtooth import BluetoothManager
bm = BluetoothManager()
connected = bm.getConnectedDevices()
print(connected)
