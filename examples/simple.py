from wldvl import WlDVL

dvl = WlDVL("/dev/ttyUSB0")
report = dvl.read()
print(report)

# Show data
print("Velocity ", report['vx'], report['vx'], report['vz'])
print("Altitude ", report['altitude'])
print("Valid measurement ", "Yes" if report['valid'] else "No")
