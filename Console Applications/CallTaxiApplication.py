"""
import math

# Define points
points = ['A', 'B', 'C', 'D', 'E', 'F']
distances = {points[i]: i * 15 for i in range(len(points))}  # Distance from point A

# Initialize taxis
n_taxis = 4
taxis = [{'id': i + 1, 'location': 'A', 'earnings': 0, 'status': 'free'} for i in range(n_taxis)]

def calculate_fare(pickup, drop):
    distance = abs(distances[drop] - distances[pickup])
    fare = 100 + max(0, distance - 5) * 10
    return fare

def find_nearest_free_taxi(pickup):
    nearest_taxi = None
    nearest_distance = float('inf')

    for taxi in taxis:
        if taxi['status'] == 'free':
            distance = abs(distances[taxi['location']] - distances[pickup])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_taxi = taxi
            elif distance == nearest_distance and taxi['earnings'] < nearest_taxi['earnings']:
                nearest_taxi = taxi

    return nearest_taxi

def book_taxi(pickup, drop):
    free_taxis = [taxi for taxi in taxis if taxi['location'] == pickup and taxi['status'] == 'free']
    
    if free_taxis:
        taxi = min(free_taxis, key=lambda t: t['earnings'])
    else:
        taxi = find_nearest_free_taxi(pickup)
    
    if taxi is None:
        print(f"Booking rejected for trip from {pickup} to {drop}: No free taxis available.")
        return False

    fare = calculate_fare(pickup, drop)
    travel_time = (distances[drop] - distances[pickup]) // 15 * 60
    taxi['location'] = drop
    taxi['earnings'] += fare
    taxi['status'] = 'occupied'
    
    print(f"Taxi {taxi['id']} booked for trip from {pickup} to {drop}. Fare: Rs.{fare}. Travel time: {travel_time} minutes.")
    
    # Simulate the taxi becoming free after the trip (in a real application, this would be based on time)
    taxi['status'] = 'free'
    return True

def display_taxis():
    for taxi in taxis:
        print(f"Taxi ID: {taxi['id']}, Location: {taxi['location']}, Earnings: Rs.{taxi['earnings']}, Status: {taxi['status']}")

def main():
    while True:
        print("\nCurrent status of taxis:")
        display_taxis()
        
        pickup = input("Enter pickup point (A, B, C, D, E, F) or 'exit' to quit: ").upper()
        if pickup == 'EXIT':
            break
        if pickup not in points:
            print("Invalid pickup point. Please enter a valid point (A, B, C, D, E, F).")
            continue

        drop = input("Enter drop point (A, B, C, D, E, F): ").upper()
        if drop not in points:
            print("Invalid drop point. Please enter a valid point (A, B, C, D, E, F).")
            continue

        if pickup == drop:
            print("Pickup and drop points cannot be the same.")
            continue

        success = book_taxi(pickup, drop)
        if not success:
            print("No taxis available for booking.")

if __name__ == "__main__":
    main()
"""
import time

# Define points
points = ['A', 'B', 'C', 'D', 'E', 'F']
distances = {points[i]: i * 15 for i in range(len(points))}  # Distance from point A

# Initialize taxis
n_taxis = 4
taxis = [{'id': i + 1, 'location': 'A', 'earnings': 0, 'status': 'free'} for i in range(n_taxis)]

def calculate_fare(pickup, drop):
    distance = abs(distances[drop] - distances[pickup])
    fare = 100 + max(0, distance - 5) * 10
    return fare

def find_nearest_free_taxi(pickup):
    nearest_taxi = None
    nearest_distance = float('inf')

    for taxi in taxis:
        if taxi['status'] == 'free':
            distance = abs(distances[taxi['location']] - distances[pickup])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_taxi = taxi
            elif distance == nearest_distance and taxi['earnings'] < nearest_taxi['earnings']:
                nearest_taxi = taxi

    return nearest_taxi

def book_taxi(pickup, drop):
    free_taxis = [taxi for taxi in taxis if taxi['location'] == pickup and taxi['status'] == 'free']
    
    if free_taxis:
        taxi = min(free_taxis, key=lambda t: t['earnings'])
    else:
        taxi = find_nearest_free_taxi(pickup)
    
    if taxi is None:
        print(f"Booking rejected for trip from {pickup} to {drop}: No free taxis available.")
        return False

    fare = calculate_fare(pickup, drop)
    travel_time = (distances[drop] - distances[pickup]) // 15 * 60
    taxi['location'] = drop
    taxi['earnings'] += fare
    taxi['status'] = 'busy'
    
    print(f"Taxi {taxi['id']} booked for trip from {pickup} to {drop}. Fare: Rs.{fare}. Travel time: {travel_time} minutes.")
    
    # Simulate the taxi becoming free after the trip
    time.sleep(travel_time / 10)  # Simulate the travel time (divided by 10 for faster simulation)
    taxi['status'] = 'free'
    print(f"Taxi {taxi['id']} is now free.")
    return True

def display_taxis():
    for taxi in taxis:
        print(f"Taxi ID: {taxi['id']}, Location: {taxi['location']}, Earnings: Rs.{taxi['earnings']}, Status: {taxi['status']}")

def main():
    while True:
        print("\nCurrent status of taxis:")
        display_taxis()
        
        pickup = input("Enter pickup point (A, B, C, D, E, F) or 'exit' to quit: ").upper()
        if pickup == 'EXIT':
            print("You are Welcome")
            break
        if pickup not in points:
            print("Invalid pickup point. Please enter a valid point (A, B, C, D, E, F).")
            continue

        drop = input("Enter drop point (A, B, C, D, E, F): ").upper()
        if drop not in points:
            print("Invalid drop point. Please enter a valid point (A, B, C, D, E, F).")
            continue

        if pickup == drop:
            print("Pickup and drop points cannot be the same.")
            continue

        success = book_taxi(pickup, drop)
        if not success:
            print("No taxis available for booking.")

if __name__ == "__main__":
    main()
