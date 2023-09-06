#!/bin/bash

# Apply database migrations
python manage.py migrate

# # # Start background task processing
# cd Pizzeria_App/management/command/
# python manage.py update_status_order.py

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
