import heapq

def match_requests():
    # User input for requests
    num_requests = int(input("Enter number of requests: "))
    requests = []
    for _ in range(num_requests):
        equipment_type = input("Enter equipment type: ")
        max_price = int(input("Enter max price: "))
        requests.append((equipment_type, max_price))
    
    # User input for sellers
    num_sellers = int(input("Enter number of sellers: "))
    sellers = []
    for _ in range(num_sellers):
        equipment_type = input("Enter equipment type: ")
        price = int(input("Enter price: "))
        sellers.append((equipment_type, price))
    
    # Dictionary to store min-heaps for each equipment type
    equipment_heaps = {}
    
    # Populate the heaps with seller data
    for equipment_type, price in sellers:
        if equipment_type not in equipment_heaps:
            equipment_heaps[equipment_type] = []
        heapq.heappush(equipment_heaps[equipment_type], price)
    
    # Process each request
    result = []
    for equipment_type, max_price in requests:
        if equipment_type in equipment_heaps:
            while equipment_heaps[equipment_type]:
                lowest_price = heapq.heappop(equipment_heaps[equipment_type])
                if lowest_price <= max_price:
                    result.append(lowest_price)
                    break
            else:
                result.append(None)  # No valid seller found
        else:
            result.append(None)  # No sellers for this equipment
    
    print("Matched Prices:", result)

# Run the function
match_requests()
