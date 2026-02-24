import random
import time

print("------ Temperature Monitoring System ------")

# Accept minimum and maximum temperature from user
min_limit = float(input("Enter Minimum Temperature Limit: "))
max_limit = float(input("Enter Maximum Temperature Limit: "))

# Check if limits are valid
if min_limit >= max_limit:
    print("Error: Minimum limit must be less than Maximum limit.")
else:
    print("\nMonitoring started...\nPress Ctrl+C to stop.\n")

    try:
        while True:
            # Generate random temperature between 0 and 100
            temperature = random.uniform(0, 100)

            print(f"Current Temperature: {temperature:.2f}°C")

            # Compare with limits
            if temperature < min_limit:
                print("⚠️ Alert! Temperature is BELOW minimum limit.\n")
            elif temperature > max_limit:
                print("⚠️ Alert! Temperature is ABOVE maximum limit.\n")
            else:
                print("✅ Temperature is within safe range.\n")

            # Wait for 2 seconds
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring Stopped.")