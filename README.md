# UOPP: TELEGRAM SCRAPPER

## About

**Description**

to be added...

**Technologies**

Python, Telethon, RabbitMQ, Docker

## Local setup

**Prerequisites**

- Python 3, pip
- Docker

**Installation**

1. Clone and open project
2. Create .env file as an example below (specify you configs)

   ```dotenv
   TELEGRAM_API_NAME=<TELEGRAM_API_NAME>
   TELEGRAM_API_ID=<TELEGRAM_API_ID>
   TELEGRAM_API_HASH=<TELEGRAM_API_HASH>
   RABBIT_RAW_QUEUE_NAME=<RABBIT_RAW_QUEUE_NAME>
   RABBIT_DELIVERY_MODE=<RABBIT_DELIVERY_MODE>
   RABBIT_HOST=<RABBIT_HOST>
   RABBIT_PORT=<RABBIT_PORT>
   RABBIT_UI_PORT=<RABBIT_UI_PORT>
   RABBIT_USERNAME=<RABBIT_USERNAME>
   RABBIT_PASSWORD=<RABBIT_PASSWORD>
   RABBIT_MAX_RETRIES=<RABBIT_MAX_RETRIES>
   RABBIT_RETRY_DELAY=<RABBIT_RETRY_DELAY>
   ```

3. Up used containers
    ```bash
    docker-compose up -d
    ```
4. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
5. Launch the program
    ```bash
    python main.py
    ```
   *during the first launch you need to authorize to create telegram session
