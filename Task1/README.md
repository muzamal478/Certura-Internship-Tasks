# Task 1: Temperature Tracker 📊

## Description
Python program tracks 7 daily temperatures via user input, stores in a list, and computes stats (average, max, min) using functions. Displays formatted results. Handles invalid inputs and empty cases.

## Objective
Practice list usage, functions, and stats for real-world data tracking.

## Features
- Input validation (numbers only).
- Functions: get_temperatures(), calculate_average(), calculate_max(), calculate_min(), display_results().
- Edge cases: Empty list (avg=0, max/min=None), negatives, decimals.

## Usage
Run: `python temperature_tracker.py`
Input: e.g., 25.5 for each day.

## Example Input/Output
Input: 20, 22, 24, 26, 28, 30, 18
Output:
Weekly Temperature Stats:
Daily Temperatures: [20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 18.0]
Average Temperature: 24.00°C
Maximum Temperature: 30.00°C
Minimum Temperature: 18.00°C

## Edge Cases
- Invalid: Reprompts.
- Zeros: Avg 0.00.
- Negatives: Handles (e.g., -5.0).

Video demo on LinkedIn. Expand by adding more weeks.

"The only place success comes before work is in the dictionary" - Vidal Sassoon

Author: Muzamal Asghar | Date: August 14, 2025