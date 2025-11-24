# Student Result Management System  
---

## Overview

The **Student Result Management System** is a software solution designed to efficiently manage student academic records, store and retrieve data using hashing and tree-based structures, perform fast roll-number lookups, sort marks and roll numbers using multiple sorting algorithms, and compare their performance.

This assignment focuses on implementing **hashing**, **Binary Search Trees (BST)**, and classical **sorting algorithms** to simulate real-world student data management.

---

## Objectives

- Design a system to store and manage student academic details.  
- Implement hashing and tree structures for fast retrieval and search operations.  
- Enable roll-number–based lookups using hashing for **O(1)** access (average case).  
- Implement sorting algorithms such as **Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort**.  
- Compare the performance and behavior of different sorting algorithms on student marks and roll numbers.  
- Demonstrate efficient retrieval using trees and hash tables.  
- Apply theoretical data structure concepts (hashing, trees, sorting) to practical record management scenarios.

---

## Data Structures Used

### **1. Hash Table**
Used for:
- Fast roll-number lookups  
- Direct access to student data  
- Efficient insert/search/delete operations  

**Reason:**  
Hashing provides **O(1)** average-case search time, making it ideal for frequently accessed student records.

---

### **2. Binary Search Tree (BST)**
Used for:
- Sorted storage of roll numbers or marks  
- Inorder traversal for sorted output  
- Range queries (e.g., students scoring 70–90)  

**Reason:**  
BST offers **logarithmic search time** and naturally maintains sorted structure.

---

### **3. Sorting Algorithms**
Used for:
- Sorting marks  
- Sorting roll numbers  
- Comparing time complexity and algorithm behaviour  

Algorithms implemented:
- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

**Reason:**  
Each sorting algorithm demonstrates different efficiency trade-offs.

---

## Functionalities

### **1. Student Record Management**
- Add student  
- Update student details  
- Delete student  
- Display all student records  
- Search by roll number (via Hash Table)

### **2. Hash Table Operations**
- Insert student record  
- Search by roll  
- Delete record  
- Handle collisions (linear probing / separate chaining)

### **3. Tree Operations**
- Insert nodes (marks or roll)  
- Inorder / Preorder / Postorder traversal  
- Search and delete nodes  
- Generate sorted lists using BST

### **4. Sorting Module**
Sort students by:
- Marks  
- Roll number  

Using algorithms:
- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

Additional features:
- Compare execution time of sorting algorithms  
- Display sorted results  

---

## Implementation Steps

### **Step 1 — Define Student Structure**
Attributes:
- Roll Number  
- Name  
- Course  
- Marks  
- Grade (optional)

### **Step 2 — Implement Hash Table**
- Choose hashing method  
- Define bucket structure  
- Implement collision handling (probing or chaining)

### **Step 3 — Implement BST**
- Define tree node  
- Insert / search / delete operations  
- Tree traversal algorithms

### **Step 4 — Implement Sorting Algorithms**
Write functions for:
- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

### **Step 5 — Build a Menu-Driven System**
Main operations:
- Add student  
- Search student  
- Display BST-sorted results  
- Sort marks or rolls  
- Compare sorting algorithms  

### **Step 6 — Testing**
Test with:
- Random roll numbers  
- Repeated insertions  
- Duplicate records  
- Sorted, unsorted, and reverse-sorted inputs  

---

## Technologies

You may use any of the following languages:

- **C/C++** — pointers, manual hash tables, BST  
- **Java** — custom classes and structures  
- **Python** — manual hashing + tree implementation (no built-in dict for DS logic)

---

## Learning Outcomes

Students will learn to:

- Implement hash tables and handle collisions  
- Build and operate binary search trees  
- Apply and compare multiple sorting algorithms  
- Measure and analyze algorithm complexity  
- Design structured, data-driven software solutions  
- Understand practical behavior of different algorithms on real-world data  
- Write clean, modular, menu-driven academic applications  

---

## Author

**Name:** Aditya Chouhan  
**Roll No:** 2401830001  
**Course:** B.Sc (H) Cybersecurity  

---

