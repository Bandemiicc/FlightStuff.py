import requests

print("Hello CodeSandbox!")
API_key = 'a0b5f9dc7b86c8cd59be8c0f6609648b'

# Endpoint Route for Data!
url = f"http://api.aviationstack.com/v1/flights?access_key={API_key}"

response = requests.get(url)

# Parse and render some DATA!

if response.status_code == 200:
    flight_data = response.json()

    # Give me some flight data! Please
    for flight in flight_data['data'][:5]:
        print(f"Flight: {flight['flight']['iata']}")
        print(f"Airline: {flight['airline']['name']}")
        print(f"Departure Airport: {flight['departure']['airport']}")
        print(f"Arrival Airport: {flight['arrival']['airport']}")
        print(f"Status: {flight['flight_status']}")
        print("\n")
    else:
        print("this might not be for you - try again")