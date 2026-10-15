# Hospital Management System (HMS)

A web-based Hospital Management System built using Flask and Vue.js to manage hospital operations, including patients, doctors, and appointments. The application uses session-based authentication and Celery for background task processing.

## Technologies Used

- **Frontend:** Vue.js, JavaScript, HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Authentication:** Session-Based Authentication
- **Background Tasks:** Celery
- **Message Broker:** Redis

## Features

- User login and session management
- Patient and doctor management
- Appointment management
- Background task processing using Celery
- Database operations using SQLAlchemy
- Interactive web interface

## Project Structure

```text
HMS/
├── Backend/
│   ├── app.py
│   ├── celery_worker.py
│   └── requirements.txt
└── Frontend/
    ├── src/
    ├── package.json
    └── ...
```

*Note: Update the structure to match your actual repository.*

## Prerequisites

Install the following tools:

- Python
- Node.js and npm
- Redis
- Git

Docker can be used to run Redis locally.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd HMS
```

### 2. Install Backend Dependencies

Open a terminal in the backend directory:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start Redis

If Docker is installed:

```bash
docker run --name hms-redis -p 6379:6379 -d redis
```

If the container already exists:

```bash
docker start hms-redis
```

### 4. Start the Celery Worker

Open a separate terminal in the backend directory and activate the virtual environment.

```bash
python -m celery -A celery_worker.celery worker --pool=solo --loglevel=info
```

The Celery worker processes background tasks submitted by the application. Keep this terminal running.

### 5. Start the Flask Backend

Open another terminal in the backend directory:

```bash
python app.py
```

The backend starts at the local address displayed in the terminal.

### 6. Start the Vue Frontend

Open another terminal in the frontend directory:

```bash
npm install
npm run dev
```

Open the frontend URL displayed in the terminal, typically `http://localhost:5173`.

## Running Order

1. Start Redis.
2. Start the Celery worker.
3. Start the Flask backend.
4. Start the Vue frontend.

Keep the required services running while using the application.

## Author

**Jeevan Jyoti**  

## Project Documentation

Refer to the project documentation for detailed information about the database schema, architecture, and implementation.
