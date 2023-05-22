from PID_CPY import PID
pid = PID(1, 0.1, 0.05, setpoint=1)


while True:
    # Compute new output from the PID according to the systems current value
    control = pid(1)
    
    # Feed the PID output to the system and get its current value