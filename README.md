# Student Result Management System 
### Data Structures -
• Hashing • Trees • Sorting

---

## Overview

The **Student Result Management System (SRMS)** is a data-structure–based academic record system designed to store, manage, and manipulate student information efficiently.  
This project demonstrates the use of **hash tables**, **binary search trees (BST)**, and a set of **sorting algorithms** to replicate real-world result-processing workflows.

The purpose of the system is to highlight how different data structures provide speed, efficiency, and organization when managing large sets of student data such as roll numbers, marks, and academic details.

---

## Objectives

- Build a structured system to manage student details and marks.  
- Implement **hashing** for fast roll-number lookups.  
- Use a **Binary Search Tree** to organize student marks and retrieve sorted output.  
- Implement classical **sorting algorithms** (Bubble, Selection, Insertion, Merge, Quick).  
- Allow comparison of algorithm behavior and performance.  
- Strengthen understanding of tree traversal, collision resolution, and sorting logic.  
- Apply theoretical DS concepts to practical record-management problems.

---

## Data Structures Used

### **1. Hash Table (Linear Probing)**
Used for:
- Direct roll-number access  
- Fast search, insert, and delete operations  

**Why:**  
Hashing provides average-case **O(1)** access, ideal for frequently accessed student records.

---

### **2. Binary Search Tree (BST)**
Used for:
- Marks-based hierarchical organization  
- Inorder traversal → Sorted marks list  
- Range queries and ranked viewing  

**Why:**  
BST enables efficient ordering with **O(log n)** insertion/search in ideal cases.

---

### **3. Sorting Algorithms**
The system implements:

- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

Used to sort:
- **Marks**  
- **Roll numbers**

**Why:**  
Each algorithm demonstrates different complexities, helping compare performance on identical datasets.

---

## Functionalities

### **Student Management**
- Add or update student details  
- Delete student record  
- View all stored students  
- Search by roll number (via hash table)  

---

### **Hash Table Operations**
- Insert student  
- Search student  
- Delete student  
- Collision handling via linear probing  

---

### **BST Operations**
- Insert based on marks  
- Retrieve sorted results using inorder traversal  

---

### **Sorting Module**
Sort by:
- Marks  
- Roll number  

Available Algorithms:
- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

---

## Implementation Steps

1. Define the **Student** class with roll, name, course, and marks.  
2. Implement a **Hash Table** with linear probing for student storage.  
3. Create a **BST** for marks-based ordering.  
4. Write functions for **five sorting algorithms**.  
5. Build a **menu-driven interface** allowing:  
   - Adding/updating students  
   - Searching  
   - Deleting  
   - BST-based sorted display  
   - Sorting via chosen algorithm  
6. Test using multiple student entries and evaluate sorted outputs.  

---

## Technologies Used

- **Python 3.x**  
- Pure data-structure implementation (no built-in dict or list sorting functions used for DS logic)  
- Console-based menu system  

---

## Learning Outcomes

By completing this assignment, students will:

- Understand the internal working of **hash tables** and collision resolution.  
- Implement and manipulate **Binary Search Trees**.  
- Apply and compare **sorting algorithms**.  
- Analyze time and space complexities.  
- Develop modular, scalable DS-based applications.  
- Improve problem-solving and algorithmic thinking.  

---

## Sample Features Demonstrated

- O(1) hash-based student lookup  
- O(log n) tree traversal for sorted marks  
- Sorting algorithm comparison on same dataset  
- Structured menu-driven execution  

---

## Author

**Name:** Aditya Chouhan  
**Roll No:** 2401830001  
**Course:** B.Sc. (H) Cybersecurity  

---
