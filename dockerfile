FROM python:3.10.6

RUN pip install pandas

RUN pip install openpyxl

WORKDIR /app

ENV PORT 80

COPY . /app

CMD ["python", "-u", "Analyze.py"]