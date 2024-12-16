# Step 1: Use an official Python base image
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements.txt into the container
COPY requirements.txt /app/

# Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy all the project files into the container
COPY . /app/

# Step 7: Expose the port the app will run on
EXPOSE 8000

# Step 8: Start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
