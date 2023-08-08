#Length of Flight | 2 Seater Plane | 4 Seater Plane | Historic Plane
#30 minutes       |       $100     |     $120       |       $300
#60 minutes       |       $150     |     $200       |       $500
# 8:00 to 18:00 = 10hours
plane_type = input("What type of plane did you fly (2-seater, 4-seater, historic plane)? >>>")

if plane_type == "2 seater" or plane_type == "2" or plane_type == "4 seater" or plane_type == "4" or plane_type == "historic plane" or plane_type == "H":
  flight_length = int(input("How long were your flights in minutes? (30 or 60)? >>>"))
  max_num_flights = flight_length/10
  print(int(max_num_flights))
  
  if flight_length == 60 and plane_type == "2 seater" or plane_type == "2":
      total_flight_profits = max_num_flights* 150
      print("The maximum profits that could be made is $", total_flight_profits)
  
  elif flight_length == 30 and plane_type == "2 seater" or plane_type == "2":
      total_flight_profits = max_num_flights* 100
      print("The maximum profits that could be made is $", total_flight_profits)

  elif flight_length == 60 and plane_type == "4 seater" or plane_type == "4":
      total_flight_profits = max_num_flights* 200
      print("The maximum profits that could be made is $", total_flight_profits)

  elif flight_length == 30 and plane_type == "4 seater" or plane_type == "4":
      total_flight_profits = max_num_flights* 120
      print("The maximum profits that could be made is $", total_flight_profits)

  elif flight_length == 60 and plane_type == "historic plane" or plane_type == "H":
      total_flight_profits = max_num_flights* 500
      print("The maximum profits that could be made is $", total_flight_profits)

  elif flight_length == 30 and plane_type == "historic plane" or plane_type == "H":
      total_flight_profits = max_num_flights* 300
      print("The maximum profits that could be made is $", total_flight_profits)
      
else:  
  print("Invalid plane type.")
