## 584. Find Customer Referee

### Description

**Table:** `Customer`

| Column Name | Type |
| :--- | :--- |
| id | int |
| name | varchar |
| referee_id | int |

In SQL, `id` is the primary key column for this table.  
Each row of this table indicates the ID of a customer, their name, and the ID of the customer who referred them.

Find the names of the customer that are either:
*   Not referred by any customer (`referee_id` is `null`).
*   Referred by a customer with an ID other than `2` (`referee_id != 2`).

Return the result table in **any order**.

The result format is in the following example.

---

### Examples

#### **Example 1:**

**Input:**   
`Customer` table:

| id | name | referee_id |
| :--- | :--- | :--- |
| 1 | Will | null |
| 2 | Jane | null |
| 3 | Alex | 2 |
| 4 | Bill | null |
| 5 | Zack | 1 |
| 6 | Mark | 2 |

**Output:**   

| name |
| :--- |
| Will |
| Jane |
| Bill |
| Zack |