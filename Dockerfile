FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y git && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y git && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

ENV BACKEND_URI=http://agixt-dev:7437

EXPOSE 8501

CMD ["streamlit", "run", "Main.py", "--server.port=8501", "--server.address=0.0.0.0"]
