Temperature Monitoring System
 Name: Khushi Kashyap
 Branch: Electronics & Communication Engineering
 Title: Temperature Monitoring System

Problem Statement:--

Build a Python program to simulate a Temperature Monitoring System for an assumed IoT environment.

The program should:

Accept maximum and minimum temperature limits from the user.

Generate random temperature values every 2 seconds.

Compare the generated temperature with the given limits.

Display appropriate alert messages based on the temperature condition.

 Approach:--

The program first takes the minimum and maximum temperature limits as input from the user.

It checks whether the minimum limit is less than the maximum limit.

Using the random module, the program generates a random temperature between 0 and 100.

The system updates the temperature every 2 seconds using the time.sleep(2) function.

The generated temperature is compared with the user-defined limits:

If temperature is below minimum → Display LOW temperature alert.

If temperature is above maximum → Display HIGH temperature alert.

Otherwise → Display temperature is within safe range.

The system continues monitoring until the user stops the program manually.


------ Temperature Monitoring System ------

Enter Minimum Temperature Limit: 20
Enter Maximum Temperature Limit: 60

Monitoring started...
Press Ctrl+C to stop.

Current Temperature: 45.67°C
Temperature is within safe range.

Current Temperature: 12.34°C
Alert! Temperature is BELOW minimum limit.

Current Temperature: 75.89°C
Alert! Temperature is ABOVE maximum limit.
