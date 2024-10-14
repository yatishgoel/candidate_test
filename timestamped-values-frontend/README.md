# Candidate Test API

## Quick Start

1. Run migrations:
   ```
   python manage.py migrate
   ```

2. Start the development server:
   ```
   python manage.py runserver
   ```

## Functionality and Features

### Core Functionality
- CRUD operations for timestamp-value pairs
- Structured data retrieval with year and month grouping
- Filtering and ordering of data

### Unique Features
- Bulk creation of timestamp-value pairs
- Caching strategy for improved performance
- Automatic population of year, month, and day fields

## Caching Strategy
- Uses Django's built-in caching framework
- Default timeout: 5 minutes (configurable via `CACHE_TIMEOUT`)
- Caches list view results for quick retrieval
- Cache invalidation on new data creation

## Database Model

`CandidateTimestamp` model:
- `timestamp`: DateTimeField (unique, indexed)
- `value`: IntegerField
- `year`: IntegerField (auto-populated)
- `month`: IntegerField (auto-populated)
- `day`: IntegerField (auto-populated)
- `created_at`: DateTimeField (auto-populated)
- `updated_at`: DateTimeField (auto-populated)

## API Endpoints

1. `GET /candidate_test/fronted/`
   - List all timestamp-value pairs (paginated)
   - Supports filtering and ordering

2. `POST /candidate_test/fronted/`
   - Create a new timestamp-value pair
   - Supports bulk creation with a list of objects

3. `GET /candidate_test/fronted/<id>/`
   - Retrieve a specific timestamp-value pair

4. `PUT /candidate_test/fronted/<id>/`
   - Update a specific timestamp-value pair

5. `PATCH /candidate_test/fronted/<id>/`
   - Partially update a specific timestamp-value pair

6. `DELETE /candidate_test/fronted/<id>/`
   - Delete a specific timestamp-value pair

## Additional Information

- Uses Django Rest Framework for API development
- Implements custom pagination (100 items per page, configurable)
- Logging implemented for error tracking and cache operations
- Signal receiver for cache invalidation on model save
