import csv
from django.shortcuts import render,HttpResponse

import pandas as pd
from django.conf import settings
import os
from django.http import JsonResponse


def show_data(request):
    # Use the absolute path to the CSV file
    excel_file_path = r'D:\Users\X510U\Documents\programming files\programming files\Data analyze projects\analyze_sales\dataview\dataseen\static\supermarket_sales.csv'

    # Debugging: Print the file path to ensure it's correct
    print(f"CSV file path: {excel_file_path}")

    try:
        # Read the CSV file
        df = pd.read_csv(excel_file_path)
    except FileNotFoundError:
        return render(request, 'show_data.html', {'data': 'File not found.'})
    except Exception as e:
        return render(request, 'show_data.html', {'data': f'An error occurred: {e}'})

    # Convert DataFrame to HTML
    data_html = df.to_html(index=False)

    # Pass the HTML to the template
    context = {
        'data': data_html,
    }

    return render(request, 'show_data.html', context)


def home(request):
    return  HttpResponse("hello world") 


def read_csv_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def dashboard(request):
    file_path =  r'D:\Users\X510U\Documents\programming files\programming files\Data analyze projects\analyze_sales\dataview\dataseen\static\supermarket_sales.csv'
    data = read_csv_data(file_path)
    return render(request, 'dashboard.html', {'data': data})

def get_data(request):
    file_path =  r'D:\Users\X510U\Documents\programming files\programming files\Data analyze projects\analyze_sales\dataview\dataseen\static\supermarket_sales.csv'
    data = read_csv_data(file_path)
    return JsonResponse(data, safe=False)
