import csv
import os
import sys
import django
from datetime import datetime

# The absolute path to the project 
sys.path.append(r"C:\Users\user\amazon_stock_api")

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_api.settings')
django.setup()

from stocks.models import StockPrice

# Path to CSV file 
csv_file_path = os.path.join(os.path.dirname(__file__), 'Amazon.csv')

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        StockPrice.objects.create(
            date=datetime.strptime(row['Date'], '%Y-%m-%d'),
            open=float(row['Open']) if row['Open'] else None,
            high=float(row['High']) if row['High'] else None,
            low=float(row['Low']) if row['Low'] else None,
            close=float(row['Close']) if row['Close'] else None,
            adj_close=float(row['Adj Close']) if row['Adj Close'] else None,
            volume=int(row['Volume']) if row['Volume'] else None,
        )

print("Data imported successfully.")