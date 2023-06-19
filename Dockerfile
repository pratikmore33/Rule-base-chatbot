FROM python:3.9

WORKDIR /app

# upgrade pip 
RUN pip install --upgrade pip 

# copy requirement.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy main code 
COPY ./main.py /app/main.py 

# run fastapi code 
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
