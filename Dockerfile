FROM python:3.11-slim

WORKDIR /app

COPY packages.txt .
RUN pip install --no-cache-dir -r packages.txt

COPY app.py config.yaml ./
COPY src ./src

ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
