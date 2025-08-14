# Temperature Tracker - Certura Internship Task 1
# Author: Muzamal Asghar
# Date: August 14, 2025
# Objective: Track daily temperatures for a week and calculate weekly stats (average, max, min).
# Usage: Run, input 7 temperatures, view results.
# Details: Lists for storage, functions for calculations, validation, formatted output.

def get_temperatures():
    """
    Collect 7 daily temperatures with validation.
    Returns: List of floats.
    """
    temperatures = []
    for day in range(1, 8):
        while True:
            try:
                temp = float(input(f"Enter temperature for Day {day} (in Celsius): "))
                temperatures.append(temp)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return temperatures

def calculate_average(temps):
    """
    Compute average.
    Returns: Float (0 if empty).
    """
    return sum(temps) / len(temps) if temps else 0

def calculate_max(temps):
    """
    Find max.
    Returns: Max or None if empty.
    """
    return max(temps) if temps else None

def calculate_min(temps):
    """
    Find min.
    Returns: Min or None if empty.
    """
    return min(temps) if temps else None

def display_results(temps, avg, max_temp, min_temp):
    """
    Display formatted results.
    """
    print("\nWeekly Temperature Stats:")
    print("Daily Temperatures:", temps)
    print(f"Average Temperature: {avg:.2f}°C")
    if max_temp is not None:
        print(f"Maximum Temperature: {max_temp:.2f}°C")
    if min_temp is not None:
        print(f"Minimum Temperature: {min_temp:.2f}°C")

if __name__ == "__main__":
    print("Welcome to Temperature Tracker! 📊")
    temperatures = get_temperatures()
    avg = calculate_average(temperatures)
    max_temp = calculate_max(temperatures)
    min_temp = calculate_min(temperatures)
    display_results(temperatures, avg, max_temp, min_temp)
    print("\nTask completed successfully! 🚀")