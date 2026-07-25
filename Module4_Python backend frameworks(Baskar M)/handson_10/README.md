# Course Management System - Microservices Architecture

## Service Decomposition

| Service Name | Responsibility | Endpoints Owned | Database |
|--------------|---------------|-----------------|----------|
| Course Service | Manage departments and courses | GET/POST/PUT/DELETE /api/courses | course.db |
| Student Service | Manage students and enrollments | GET/POST/PUT/DELETE /api/students, POST /api/students/<id>/enroll | student.db |
| Auth Service | User registration, login, JWT validation | /api/auth/register, /api/auth/login | auth.db |
| Notification Service | Send email notifications for enrollments | /api/notifications/send | notification.db |

## Why split into Microservices?

- Independent deployment
- Independent scaling
- Separate databases
- Better fault isolation
- Easier maintenance

# Inter-Service Communication

## Synchronous Communication (HTTP)

### Advantages
- Immediate response between services.
- Easy to implement using REST APIs.
- Suitable when the client requires an instant result.
- Simple to debug and test.

### Disadvantages
- Services are tightly coupled.
- If one service is unavailable, dependent services fail.
- Increased response time due to network calls.
- Poor fault tolerance.

---

## Asynchronous Communication (Message Queue)

Examples:
- RabbitMQ
- Apache Kafka

### Advantages
- Services are loosely coupled.
- Better scalability.
- Improved fault tolerance.
- Messages are stored until the receiving service is available.
- Supports high-volume event processing.

### Disadvantages
- Eventual consistency (data may not update immediately).
- More complex architecture.
- Requires additional infrastructure such as RabbitMQ or Kafka.

---

## When to Use Each

### Use Synchronous (HTTP) when:
- An immediate response is required.
- The client cannot continue without the result.
- Examples:
  - Login
  - Course lookup
  - Payment verification
  - User authentication

### Use Asynchronous (RabbitMQ/Kafka) when:
- The task can be processed later.
- High reliability is required.
- Examples:
  - Sending emails
  - Notifications
  - Report generation
  - Audit logging
  - Processing large data streams

---

## API Gateway

The API Gateway acts as the single entry point for all client requests.

Responsibilities:
- Route requests to the appropriate microservice.
- Hide internal service locations.
- Centralize authentication.
- Apply rate limiting.
- Handle logging and monitoring.
- Simplify client communication.

Example Flow:

Client
        │
        ▼
API Gateway (Port 5000)
        │
 ┌──────┴────────┐
 ▼               ▼
Course Service   Student Service
(Port 5001)      (Port 5002)