# Use official Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project into the container
COPY . /app

# Install dependencies from `requirements.txt`
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port (8501)
EXPOSE 8501

# Run Streamlit app when the container starts
CMD ["streamlit", "run", "forecast_app.py", "--server.port=8501"]
