# Lineup API

A Django REST Framework API for booking music gigs — connecting artists, venues, and performers.

## Prerequisites

- Python 3.10
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Setup

1. **Clone the repo and install dependencies**

   ```bash
   pipenv install
   pipenv shell
   ```

2. **Seed the database**

   ```bash
   chmod u+x ./seed_database.sh
   ./seed_database.sh
   ```

   This resets the database and loads fixtures for users, tokens, venues, instruments, profiles, and gigs.

3. **Start the development server**

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`.

## Authenticating Requests

This API uses token authentication. Include the token in the request header:

```
Authorization: Token <your-token>
```

Tokens are seeded via the `lineup_token` fixture. Check the fixture file for available test tokens.
