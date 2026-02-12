# 1. Base Image: Use a light version of Python
FROM python:3.11-slim

# 2. Setup Work Directory
WORKDIR /app

# 3. Install Dependencies FIRST (Caching layer)
# If you change code but not requirements, Docker skips this slow step.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the code
COPY . .

# 5. Command to run the server
# host 0.0.0.0 is MANDATORY for containers to be accessible
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]