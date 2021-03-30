#Context: We want to make a pressurized speaker.

maximumPressure = 2.3
maximumVolume = 7.41

currentPressure = float(input("Enter the current speaker's pressure:\n"))
currentVolume = float(input("Enter the current speaker's volume:\n"))

if currentPressure > maximumPressure and currentVolume > maximumVolume:
    print("Both the current pressure and the current volume are too high, the device has been turned off.")
elif currentPressure > maximumPressure:
    print("Please turn up the speaker's volume.")
elif currentVolume > maximumVolume:
    print("Please lower the speaker's volume.")
else:
    print("Everything is fine, enjoy your sound!")