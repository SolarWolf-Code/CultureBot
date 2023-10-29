FROM python:3.11-slim-bullseye

# Path: /app
WORKDIR /app

# Copy over files
COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

# Run qbitbot.py
CMD ["python", "culture_bot.py"]