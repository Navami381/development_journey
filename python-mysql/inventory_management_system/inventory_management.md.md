# Practice Task: Inventory Stock Management System

## Project Abstract

Build an **Inventory Stock Management System** using **Python and MySQL**.

The purpose of this project is to simulate how a real-world backend application works before introducing Django, Django REST Framework, Gemini, and LangChain.

Warehouse managers and store supervisors can manage product stock levels, track reorder thresholds, update inventory counts, and monitor stock availability.

The system should support basic CRUD operations and gradually introduce filtering, searching, aggregation, validation, and AI-powered stock forecasting and anomaly detection.

---

## 1. Real-World Scenario

Imagine a retail warehouse application.

A store supervisor notices a stock issue:

> "Wireless Gaming Mouse stock is down to 5 units, which is below the reorder threshold."

The supervisor uses the **inventory management system**.

The inventory team should be able to:

- Create a new stock item entry
- View all inventory items
- View details of a specific item
- Update stock levels and item details
- Delete discontinued items
- Filter items by category or status
- Search items by name or SKU
- View inventory valuation statistics
- Assign warehouse storage zones

Later, AI can automatically analyze inventory patterns and determine:

- Optimal reorder quantity
- Category classification
- Stock depletion risk
- Summary report
- Suggested supplier reorder email

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
CREATE DATABASE inventory_db;

USE inventory_db;