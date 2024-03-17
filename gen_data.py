

# import csv
# import random

# from flask import Flask
# app = Flask(__name__)

# @app.route('/generate_csv')
# def generate_csv():
#     # Generate random zipcodes
#     zipcodes = [random.randint(10000, 99999) for i in range(100)]

#     # Generate random water consumption values 
#     consumption = [random.randint(10, 100) for i in range(100)]

#     # Write data to CSV file
#     with open('consumption.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         # writer.writerow(['zipcode', 'average_consumption'])
#         for z, c in zip(zipcodes, consumption):
#             writer.writerow([z, c])

#     return 'CSV file generated successfully!'


# app.run(debug=True)