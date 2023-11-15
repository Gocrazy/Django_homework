FROM python:3.11
WORKDIR /app
COPY . .

RUN pip --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
