# TimestampedValues API

A Django REST Framework application for managing and retrieving timestamped values with efficient caching.

## Features

- CRUD operations for TimestampedValues
- Structured data representation by year and month
- Efficient caching strategy with automatic invalidation
- Pagination, filtering, and ordering
- Bulk creation support

## Setup

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Set up a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Set up the database

#### Option 1: Using an existing PostgreSQL Database

If you already have a PostgreSQL database:

1. Update the `.env` file with your database credentials:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost  # Or your database host
   DB_PORT=5432       # Default PostgreSQL port
   ```

2. Run the database migrations to set up the necessary tables:
   ```bash
   python manage.py migrate
   ```

#### Option 2: Create a new PostgreSQL Database

If you want to set up your own PostgreSQL database locally:

1. **Install PostgreSQL**:

   - **Mac OS**: Install using Homebrew:
     ```bash
     brew install postgresql
     brew services start postgresql
     ```
   - **Windows**: Download and install PostgreSQL from [here](https://www.postgresql.org/download/).
   - **Linux**: Install PostgreSQL using:
     ```bash
     sudo apt-get install postgresql postgresql-contrib
     sudo service postgresql start
     ```

2. **Create a new PostgreSQL database and user**:

   Open the PostgreSQL shell:
   ```bash
   psql postgres
   ```

   Then, create the database and user:
   ```sql
   CREATE DATABASE your_db_name;
   CREATE USER your_db_user WITH PASSWORD 'your_db_password';
   ALTER ROLE your_db_user SET client_encoding TO 'utf8';
   ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_db_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
   ```

   Replace `your_db_name`, `your_db_user`, and `your_db_password` with the values you wish to use.

3. **Update your `.env` file** with the database connection details:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Run migrations** to create the necessary tables in your new database:
   ```bash
   python manage.py migrate
   ```

### 4. Run the development server

Once the database is set up and migrations are applied, you can start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/candidate_test/fronted/`.

### 5. Create initial data in the database

To quickly insert some data into the `TimestampedValues` API, you can use the following `curl` command:

```bash
curl --location 'http://localhost:8000/candidate_test/fronted' \
--header 'Content-Type: application/json' \
--data '[
  { "timestamp": "2024-01-01 00:00:00", "value": 300 },
  { "timestamp": "2024-01-02 00:00:00", "value": 400 },
  { "timestamp": "2024-01-03 00:00:00", "value": 550 },
  { "timestamp": "2024-02-01 00:00:00", "value": 300 },
  { "timestamp": "2024-02-02 00:00:00", "value": 400 },
  { "timestamp": "2024-02-03 00:00:00", "value": 550 }
]'
```

### 6. API Endpoints

Here are the available API endpoints:

1. `GET /candidate_test/fronted/`
   - List all timestamp-value pairs (paginated)
   - Supports filtering and ordering
   - Query parameters:
     - `year`: Filter by year
     - `month`: Filter by month (takes values from 1 to 12)

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

### 7. Starting the Frontend

To start the React frontend for this project:

1. Navigate to the frontend directory:
   ```bash
   cd timestamped-values-frontend
   ```

2. Install the required Node modules:
   ```bash
   npm install
   ```

3. Start the React project:
   ```bash
   npm start
   ```

The React app should now be running on `http://localhost:3000`.

## Usage

Access the API at `/candidate_test/fronted/` to interact with the TimestampedValues data.

## Caching

The application implements a caching strategy to improve performance:
- Cache is automatically warmed on the first request.
- Cached data is used for subsequent requests.
- Cache is automatically updated when new data is added, updated, or deleted.

## Configuration

- Database and cache settings can be configured in `settings.py`.
- Environment-specific variables (like secret keys, debug settings, and database credentials) are managed via the `.env` file.
