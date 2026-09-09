# Practice Task: Customer Support Ticket Management System

## Project Abstract

Build a **Customer Support Ticket Management System** using **Python and MySQL**.

The purpose of this project is to simulate how a real-world backend application works before introducing Django, Django REST Framework, Gemini, and LangChain.

Customers can create support tickets when they face issues such as payment failures, delivery problems, account issues, refunds, or technical problems.

The system should support basic CRUD operations and gradually introduce filtering, searching, aggregation, validation, and AI-powered ticket analysis.

---

## 1. Real-World Scenario

Imagine an e-commerce application.

A customer faces a problem:

> "I paid ₹2,500 but my order is still showing as pending."

The customer creates a **support ticket**.

The support team should be able to:

- Create a ticket
- View all tickets
- View a specific ticket
- Update a ticket
- Delete a ticket
- Filter tickets
- Search tickets
- View ticket statistics
- Assign tickets to support employees

Later, AI can automatically analyze the ticket and determine:

- Category
- Priority
- Sentiment
- Summary
- Suggested response

---

# 2. Technology

For the initial implementation:

- Python
- MySQL
- `mysql-connector-python`

Later, the same project can be extended with:

- Django
- Django REST Framework
- Gemini API
- Pydantic
- LangChain
- LangChain Tools / Agents

---

# 3. Database

Create the database:

```sql
CREATE DATABASE support_db;

USE support_db;
```

Create the table:

```sql
CREATE TABLE support_ticket (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    email VARCHAR(150),
    subject VARCHAR(200),
    description TEXT,
    category VARCHAR(50),
    priority VARCHAR(20),
    status VARCHAR(20),
    assigned_to VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 4. Allowed Values

### Category

```text
payment
delivery
account
technical
refund
other
```

### Priority

```text
low
medium
high
urgent
```

### Status

```text
open
in_progress
resolved
closed
```

---

# 5. Sample Data

Insert some sample tickets:

```sql
INSERT INTO support_ticket
(customer_name, email, subject, description, category, priority, status, assigned_to)
VALUES
(
    'Arun',
    'arun@gmail.com',
    'Payment deducted but order pending',
    'I made the payment yesterday but my order is still showing pending.',
    'payment',
    'high',
    'open',
    'Rahul'
),
(
    'Meera',
    'meera@gmail.com',
    'Unable to login',
    'I have forgotten my password and cannot login to my account.',
    'account',
    'medium',
    'open',
    'Anjali'
),
(
    'Vishnu',
    'vishnu@gmail.com',
    'Product not delivered',
    'My order was supposed to arrive three days ago but I still have not received it.',
    'delivery',
    'high',
    'in_progress',
    'Rahul'
);
```

---

# 6. Python Class

Create a class:

```python
class SupportTicketListCreateRetrieveUpdateDelete:
    pass
```

The class should establish a connection with MySQL.

The implementation should follow the same pattern as a backend API.

---

# 7. CRUD Operations

The Python methods should represent HTTP operations.

| Backend Operation | Python Method |
|---|---|
| POST | `post()` |
| GET | `get()` |
| GET /id | `retrieve()` |
| PUT | `put()` |
| DELETE | `delete()` |

Conceptually:

```text
POST        → Create ticket
GET         → List tickets
GET /id     → Retrieve ticket
PUT /id     → Update ticket
DELETE /id  → Delete ticket
```

---

# 8. POST - Create Ticket

Implement:

```python
ticket.post(
    customer_name="Arun",
    email="arun@gmail.com",
    subject="Payment problem",
    description="Payment was deducted but order is pending",
    category="payment",
    priority="high",
    status="open",
    assigned_to="Rahul"
)
```

Expected result:

```text
Ticket created successfully
```

Use parameterized SQL queries.

---

# 9. GET - List Tickets

Implement:

```python
ticket.get()
```

The method should retrieve all tickets.

Expected output:

```text
(1, 'Arun', 'arun@gmail.com', ...)
(2, 'Meera', 'meera@gmail.com', ...)
(3, 'Vishnu', 'vishnu@gmail.com', ...)
```

---

# 10. RETRIEVE - Single Ticket

Implement:

```python
ticket.retrieve(id=2)
```

The method should retrieve one ticket based on its ID.

If the ticket exists:

```text
Ticket details should be displayed
```

If it does not exist:

```text
Ticket not found
```

Do not simply display:

```text
None
```

---

# 11. PUT - Update Ticket

The update operation should support partial updates.

For example:

```python
ticket.put(
    id=1,
    priority="urgent"
)
```

Another example:

```python
ticket.put(
    id=1,
    status="in_progress",
    assigned_to="Vishnu"
)
```

Another example:

```python
ticket.put(
    id=1,
    priority="urgent",
    status="in_progress",
    assigned_to="Vishnu"
)
```

The SQL should be generated dynamically based on the fields supplied.

Example:

```sql
UPDATE support_ticket
SET priority=%s
WHERE id=%s;
```

Another example:

```sql
UPDATE support_ticket
SET status=%s, assigned_to=%s
WHERE id=%s;
```

---

