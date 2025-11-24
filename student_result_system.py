class Student:
    def __init__(self, roll, name, course, marks):
        self.roll = roll
        self.name = name
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Course: {self.course}, Marks: {self.marks}"

class HashTable:
    def __init__(self, size=23):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def _hash(self, roll):
        return roll % self.size

    def insert(self, student):
        idx = self._hash(student.roll)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None or self.table[probe] is self.deleted:
                self.table[probe] = student
                return True
            if self.table[probe].roll == student.roll:
                self.table[probe] = student
                return True
        print("Hash table full.")
        return False

    def search(self, roll):
        idx = self._hash(roll)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return None
            if self.table[probe] is self.deleted:
                continue
            if self.table[probe].roll == roll:
                return self.table[probe]
        return None

    def delete(self, roll):
        idx = self._hash(roll)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return False
            if self.table[probe] is self.deleted:
                continue
            if self.table[probe].roll == roll:
                self.table[probe] = self.deleted
                return True
        return False

    def all_students(self):
        result = []
        for s in self.table:
            if isinstance(s, Student):
                result.append(s)
        return result

class BSTNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class MarksBST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        self.root = self._insert(self.root, student)

    def _insert(self, node, student):
        if node is None:
            return BSTNode(student)
        if student.marks < node.student.marks:
            node.left = self._insert(node.left, student)
        else:
            node.right = self._insert(node.right, student)
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.student)
        self._inorder(node.right, result)

def bubble_sort(arr, key):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(arr, key):
    a = arr[:]
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if key(a[j]) < key(a[m]):
                m = j
        a[i], a[m] = a[m], a[i]
    return a

def insertion_sort(arr, key):
    a = arr[:]
    for i in range(1, len(a)):
        t = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(t):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
    return a

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr[:]
    m = len(arr) // 2
    left = merge_sort(arr[:m], key)
    right = merge_sort(arr[m:], key)
    return _merge(left, right, key)

def _merge(left, right, key):
    r = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1
    r.extend(left[i:])
    r.extend(right[j:])
    return r

def quick_sort(arr, key):
    a = arr[:]
    _qs(a, 0, len(a) - 1, key)
    return a

def _qs(a, low, high, key):
    if low < high:
        p = _part(a, low, high, key)
        _qs(a, low, p - 1, key)
        _qs(a, p + 1, high, key)

def _part(a, low, high, key):
    p = key(a[high])
    i = low - 1
    for j in range(low, high):
        if key(a[j]) <= p:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def read_int(p, mn=None, mx=None):
    while True:
        try:
            v = int(input(p))
            if mn is not None and v < mn:
                continue
            if mx is not None and v > mx:
                continue
            return v
        except:
            pass

def read_float(p, mn=None, mx=None):
    while True:
        try:
            v = float(input(p))
            if mn is not None and v < mn:
                continue
            if mx is not None and v > mx:
                continue
            return v
        except:
            pass

class StudentResultSystem:
    def __init__(self):
        self.ht = HashTable()

    def add_student(self):
        roll = read_int("Roll number: ", 1)
        name = input("Name: ")
        course = input("Course: ")
        marks = read_float("Marks: ", 0, 100)
        self.ht.insert(Student(roll, name, course, marks))
        print("Student added.")

    def view_all_students(self):
        s = self.ht.all_students()
        if not s:
            print("No records.")
            return
        for x in s:
            print(x)

    def search_student(self):
        r = read_int("Roll: ", 1)
        s = self.ht.search(r)
        if s:
            print(s)
        else:
            print("Not found.")

    def delete_student(self):
        r = read_int("Roll: ", 1)
        if self.ht.delete(r):
            print("Deleted.")
        else:
            print("Not found.")

    def display_sorted_by_marks_bst(self):
        s = self.ht.all_students()
        if not s:
            print("No records.")
            return
        tree = MarksBST()
        for x in s:
            tree.insert(x)
        for x in tree.inorder():
            print(x)

    def sort_students_menu(self, type_key):
        s = self.ht.all_students()
        if not s:
            print("No records.")
            return
        key = (lambda x: x.marks) if type_key == "marks" else (lambda x: x.roll)
        print("1. Bubble\n2. Selection\n3. Insertion\n4. Merge\n5. Quick")
        c = input("Choose: ")
        if c == "1":
            r = bubble_sort(s, key)
        elif c == "2":
            r = selection_sort(s, key)
        elif c == "3":
            r = insertion_sort(s, key)
        elif c == "4":
            r = merge_sort(s, key)
        elif c == "5":
            r = quick_sort(s, key)
        else:
            print("Invalid.")
            return
        for x in r:
            print(x)

def main():
    system = StudentResultSystem()
    while True:
        print("\n1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Sort by Marks (BST)\n6. Sort Marks\n7. Sort Roll\n8. Exit")
        c = input("Select: ")
        if c == "1":
            system.add_student()
        elif c == "2":
            system.view_all_students()
        elif c == "3":
            system.search_student()
        elif c == "4":
            system.delete_student()
        elif c == "5":
            system.display_sorted_by_marks_bst()
        elif c == "6":
            system.sort_students_menu("marks")
        elif c == "7":
            system.sort_students_menu("roll")
        elif c == "8":
            break

if __name__ == "__main__":
    main()
