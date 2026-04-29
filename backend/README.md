# Symptom Intake App - Backend

## Local Setup

Run all the commands in /backend directory.

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file based on its provided example - copy it with the following command and fill in needed variables:**
    ```bash
   cp .env.example .env

4. **Run the development server:
   ```bash
   fastapi dev
   # or
   uvicorn main:app --reload
   ```