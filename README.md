# CDP martech

This system collects events sent by users from their phones and computers and routes them to different destinations like analytics or notifications.

How It Works?

Users on phones and computers send events (like actions or clicks) to a central API.

The API puts these events into a queue (AWS SQS)

A background processor (AWS Lambda) reads events from the queue and sends them to the right places:

Some events go to an analytics system to track user behavior.

Others go to a notification system to send alerts or messages.

You can new destinations with a simple API call, this will ocurr at the moment without needing to redeploy the lambda function!

In a nutshell the funcionality is:

1. User sends events through API
2. API call goes through api gateway
3. Api gateway sends the event to labda marterch
4. Martech lambda process the event and sends it to a queue
5. Queue sends event a destination lambda
6. Destination lambda process the events for communication and analytics and send the events
7. In DynamoDB the status of the delivery is saved, false if not success, and true if success

### Below steps are not implemente

8. If delivery is not success the message will be send to a DLQ
9. Message will be send to a different lambda that will try to send the message to the destination that returned the error, N times
10. If success, change status in database
11. If fail, delete message and do not change status in database

### Communication calls:

- When a call goes to communication flow, depending the preferredChannel, thats where the mock route will assign.
  Example:
  If preferredChannel is email, the enpoint will be send with /email

### Analytics calls

- The call will be send as it is to the analytics software

# Diagram

![Diagram](image.png)

# Requirements

- [Python 3.13](https://www.python.org/downloads/release/python-3919/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Sam CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Docker](https://www.docker.com/products/docker-desktop/)

# Installation

## Test current implementation

If you do not want to install all the necesarry dependencies you can test asking @caposcar for the current URLs

1. In the current implementation there 3 beeceptor created, 2 of them function as analytics and one as communication.

1. [analytics](https://app.beeceptor.com/console/testoscar)
1. [analytics](https://app.beeceptor.com/console/testcomms)
1. [comms](https://app.beeceptor.com/console/testsrive)

## Mount the project in the cloud (Recommended)

Mounting the project needs an AWS accountt configured in the CLI , and SAM installed

1. Build the project using

```bash
sam build
```

2. Deploy using

```bash
make deploy
```

3. You can find your api URl entering api gateway and look for the MartechApi.

4. AWS SQS will be created with the name "events"

5. DynamoDB tables will be created with the names:

- Destinations: All the destinations the events can go to
- Responses: Logs if the CDP calls are succesfull or not.

6. Create destinations using the endopoint /destinations

7. Send track events using /track

## Locally (Not recommended as it depends in AWS SQS and dybamoDB)

Running the project localy needs an AWS accountt configured in the CLI , and a queue created in AWS

1. Create an SQS queue called events in AWS
2. Create two
3. Build the project using

```bash
sam local start-api
```

3. Run the local api using:

```bash
sam local start-api
```

4. Run a function individually

```bash
sam local invoke <FunctionLogicalID> -e <event_file.json>
```

# API Endpoints

### `POST /track`

Receive user events from phones and computers.

- **Request Body:**

  ```json
  {
    "userId": "12345",
    "event": "user_clicked_promo",
    "timestamp": "2025-08-08T16:30:00Z",
    "metadata": {
      "promoId": "PROMO_001",
      "device": "mobile",
      "preferredChannel": "email"
    }
  }
  ```

- **Request Response:**

200

```json
{
  "body": "{\"messageId\": \"messageId 45633db4-50c5-45db-bce0-8641da6a6efc\"}"
}
```

500

```json
{
  "error": ""
}
```

### `POST /destinations`

Create a new destination for the events

- **Request Body:**

  ```json
  {
  "destinationName": "Braze12",
  "url": "https://testsrive.free.beeceptor.com",
  "type":"CDP" "OR" "analytics",
  "headers": "",
  }
  ```

- **Request Response:**

200

```json
{
  "body": "{\"Destination created status\": \"success\"}"
}
```

500

```json
{
  "error": ""
}
```

# Databases schema

### Destinations

| Attribute       | Type                     | Description                       |
| --------------- | ------------------------ | --------------------------------- |
| destinationName | string                   | Name of the destination           |
| headers         | object                   | Headers needed for the API call   |
| Type            | string (CDP or analytcs) | Will tell the type of call needed |
| Url             | string                   | Where the call be made            |

### Responses

| Attribute    | Type   | Description                                          |
| ------------ | ------ | ---------------------------------------------------- |
| responseId   | string | Message Id                                           |
| responseBody | object | Payload send                                         |
| destinations | object | Status of each destination status {destiny: boolean} |
