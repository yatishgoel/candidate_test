# TimestampedValues API

A Django REST Framework application for managing and retrieving timestamped values with efficient caching.

## Features

- CRUD operations for TimestampedValues
- Structured data representation by year and month
- Efficient caching strategy with automatic invalidation
- Pagination, filtering, and ordering
- Bulk creation support

## Setup

1. Set up a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

2. Set up the database:
   ```
   python manage.py migrate
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/candidate_test/frontend/`.

## Usage

Access the API at `/candidate_test/frontend/` to interact with the TimestampedValues data.

## Caching

The application implements a caching strategy to improve performance:
- Cache is automatically warmed on the first request
- Cached data is used for subsequent requests
- Cache is updated when new data is added or updated

## Configuration

Database and cache settings can be configured in `settings.py`.