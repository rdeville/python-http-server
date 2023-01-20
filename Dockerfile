FROM python:alpine3.17
ENV PORT=9000
WORKDIR /app
COPY . .
ENTRYPOINT [ "python3" , "main.py"]