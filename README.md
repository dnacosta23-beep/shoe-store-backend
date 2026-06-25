# Shoe Store Backend

## What the App Does

This Flask application serves as the backend for the Shoe Store project. It provides an API that stores a list of shoes and allows the React frontend to retrieve and add shoes.

## How to Run the Backend

1. Open a terminal.
2. Navigate to the backend project folder.
3. Activate the virtual environment.

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

4. Install the required packages (first time only):

```bash
pip install flask flask-cors
```

5. Start the Flask server:

```bash
python3 app.py
```

The backend will run at:

```
http://127.0.0.1:5000
```