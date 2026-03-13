FROM python:3.10-slim
RUN pip install requests
COPY checker.py .
CMD ["python", "checker.py"]
