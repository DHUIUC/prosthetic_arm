from time import sleep
import pi_arm as arm


def main():
    # Assuming arm is an instance of a class with the read_muscle_signal method

    # Collect readings for 5 seconds
    duration = 5  # in seconds

    readings = []

    # Record start time
    start_time = time.time()

    while time.time() - start_time < duration:
        # Read muscle signal
        reading = arm.read_muscle_signal()

        # Store the reading in the list
        readings.append(reading)

    # Calculate the average value
    if readings:
        average_value = sum(readings) / len(readings)
        print(f"Average value over {duration} seconds: {average_value}")
    else:
        print("No readings collected.")


if __name__ == "__main__":
    try:
        main()
    finally:
        #arm.stop()
