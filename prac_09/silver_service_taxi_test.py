from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(silver_taxi)
print(f"Current fare: ${silver_taxi.get_fare()}")
silver_taxi.drive(18)
# 4.50 + 1.23 * 2 * 18
current_fare = silver_taxi.get_fare()
EXPECTED_FARE = 4.50 + 1.23 * 2 * 18
assert current_fare == EXPECTED_FARE
print(silver_taxi)
print(f"Current fare: ${current_fare}")
