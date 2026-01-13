# Personal Finance Tracker v2.0

Final Exam – Managing Database using Mongo Course  
Personal Finance Tracker v2.0

---

## 📌 Project Overview

This project is an enhanced version of **Personal Finance Tracker v1.0**, focusing on:
- Fixing **data integrity vulnerabilities**
- Completing missing CRUD operations
- Ensuring synchronization between **Categories** and **Transactions**

The application uses **MongoDB** as the primary database and supports multi-user personal finance tracking.

---

## 📂 Database Collections

### 1. `users`
- Multi-user support
- Full CRUD implemented

### 2. `categories`
- Expense / Income categories
- Default categories supported
- **Update operation added in v2.0**

### 3. `transactions`
- Financial records linked to users and categories
- Full CRUD implemented

---

## 🚨 Data Integrity Issues Addressed

### Issue 4: Category Update – Transaction Sync Problem  
**Priority:** High  
**Story Points:** 3  
**Requested by:** QA Team

---

## ❌ Problem Description

Previously, the system had **no Category Update operation**.  
Even if implemented naïvely, it introduced a critical data integrity issue:

### Scenario
1. User has category `"Food"` with 50 transactions
2. User renames category `"Food"` → `"Food & Dining"`
3. Transactions still reference old category name `"Food"`
4. Reports show:
   - `"Food & Dining"`: `$0`
   - Orphan `"Food"`: `$500`

This caused:
- Incorrect reports
- Broken filters
- Data inconsistency

---

## ✅ Implemented Solution

### 1️⃣ Category Rename with Transaction Synchronization

When a category is renamed:
- The system **updates all related transactions**
- Old category name is replaced with the new one

#### Implementation Strategy
- Categories are updated by **category ID**
- Transactions referencing the old category name are updated in bulk

```python
db.transactions.update_many(
    {"category": old_category_name},
    {"$set": {"category": new_category_name}}
)
