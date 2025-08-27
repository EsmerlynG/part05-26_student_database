# Student Database Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A comprehensive Python program for managing student records and course completions with intelligent grade handling. This multi-part exercise demonstrates advanced data structure usage, algorithm design, and clean code architecture principles.

---

## 📖 Problem Description

Create a student database system with four main functions that work together to manage student information:

1. **Student Management**: Add new students to the database
2. **Course Recording**: Track completed courses with grades
3. **Grade Intelligence**: Handle course retakes by keeping only the highest grades
4. **Database Analytics**: Generate summaries and statistics

### Requirements

- Students start with no completed courses
- Failed courses (grade 0) should be ignored
- When courses are retaken, only the highest grade is preserved
- Individual student information should be printable
- Database-wide summaries should be available

---

## 💻 Code Implementation

```python
def add_student(students: dict, name: str):
    students[name] = "no completed courses"

def add_course(students: dict, name: str, course_comp: tuple):
    if students[name] == "no completed courses" and course_comp[1] != 0:
        students[name] = [course_comp]
    
    if course_comp[1] != 0 and course_comp not in students[name]:
        students[name].append(course_comp)
        students[name].sort()
        students[name].reverse()

def del_dups(students: dict):
    """Remove duplicate courses, keeping only the highest grade for each course."""
    for name, values in students.items():
        if values == "no completed courses":
            continue
            
        unique_courses = []
        seen = []
        for course, grade in values:
            if course not in seen:
                unique_courses.append((course, grade))
                seen.append(course)
        students[name] = unique_courses

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    elif students[name] == "no completed courses":
        print(f"{name}:\n no completed courses")
    else:
        del_dups(students)
        total = 0
        comp_courses = len(students[name])
        
        print(f"{name}:")
        print(f" {comp_courses} completed courses:")
        
        for course, grade in students[name]:
            print(f"  {course} {grade}")
            total += grade
        
        print(f" average grade {total/comp_courses:.1f}")

def summary(students: dict):
    del_dups(students)
    num_students = len(students)
    
    most_course_comp = 0
    most_course_student = ""
    highest_avg = 0
    best_avg_student = ""
    
    for name, value in students.items():
        if value == "no completed courses":
            continue
            
        # Count courses
        course_count = len(value)
        if course_count > most_course_comp:
            most_course_comp = course_count
            most_course_student = name
        
        # Calculate average
        total_grade = sum(grade for course, grade in value)
        avg = total_grade / course_count
        
        if avg > highest_avg:
            highest_avg = avg
            best_avg_student = name
    
    print(f"students {num_students}")
    print(f"most courses completed {most_course_comp} {most_course_student}")
    print(f"best average grade {highest_avg:.1f} {best_avg_student}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
```

**Output:**
```
students 2
most courses completed 3 Peter
best average grade 4.5 Eliza
```

---

## 🧠 Algorithm Explanation

The solution uses a clever **sort-and-reverse strategy** for duplicate handling:

### Core Algorithm Steps:
1. **Course Addition**: New courses are appended to the student's list
2. **Alphabetical Sorting**: `sort()` arranges courses by name
3. **Reverse Order**: `reverse()` puts courses in reverse alphabetical order
4. **Duplicate Removal**: When processing duplicates, the first occurrence (highest grade) is kept

### Key Insight:
By reversing after sorting, courses with the same name appear in **descending grade order**, making the first occurrence automatically the highest grade.

**Time Complexity:** O(n log n) for sorting operations  
**Space Complexity:** O(n) for storing course data

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 student_database.py
```

Or import functions in your own code:

```python
from student_database import add_student, add_course, print_student, summary

students = {}
add_student(students, "Alice")
add_course(students, "Alice", ("Python Programming", 4))
print_student(students, "Alice")
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic functionality
students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Programming", 2))
print_student(students, "Peter")
# Output: 2 completed courses, average grade 2.5

# Test case 2: Grade protection (retakes)
add_course(students, "Peter", ("Introduction to Programming", 2))  # Lower grade ignored
print_student(students, "Peter")
# Output: Still shows grade 3 for Introduction to Programming

# Test case 3: Failed courses ignored
add_course(students, "Peter", ("Data Structures", 0))  # Grade 0 ignored
print_student(students, "Peter")
# Output: Course not added to record

# Test case 4: Non-existent student
print_student(students, "Unknown")
# Output: "Unknown: no such person in the database"

# Test case 5: Database summary
summary(students)
# Output: Statistics for all students
```

---

## ✨ Design Philosophy & Learning Journey

This solution represents a **complex algorithmic approach** that prioritizes learning over simplicity:

### **Sort-Reverse Strategy**
- Used alphabetical sorting followed by reversal
- Ensures highest grades appear first in duplicate removal
- Demonstrates creative problem-solving with built-in methods

### **Multi-Function Architecture**
- Separated duplicate removal into dedicated `del_dups()` function
- Shows understanding of separation of concerns
- Allows for modular testing and maintenance

### **Data Structure Challenges**
- Mixed string and list types in same dictionary values
- Handled edge cases with conditional logic
- Demonstrates real-world data complexity management

### **Algorithmic Thinking**
- Chose sorting-based solution over simpler dictionary approach
- Shows deep understanding of list operations
- Prioritized algorithmic learning over optimal efficiency

---

## 🔍 Alternative Approach (Recommended Solution)

The course provided a more elegant solution using dictionaries:

### Dictionary-Based Approach:
```python
def add_student(students: dict, name: str):
    students[name] = {}

def add_course(students: dict, name: str, completion: tuple):
    course_name, course_grade = completion
    if course_grade == 0:
        return
    
    if course_name in students[name]:
        if students[name][course_name][1] > course_grade:
            return
    
    students[name][course_name] = completion
```

### Key Advantages:
- **Simpler Logic**: Direct grade comparison without sorting
- **Better Performance**: O(1) lookups instead of O(n log n) sorting
- **Cleaner Code**: No separate duplicate removal needed
- **Natural Structure**: Dictionary keys prevent duplicates automatically

---

## 🎯 Reflection

This challenge was one of the toughest so far, it took me around 4 days to finally find the solution. The reason this problem was so difficult for me was because I had to really implement everything I have learned and also understand what to not use. There were multiple ways for me to solve this as you can see with the recommended solution from MOOC.fi, and I was attempting to find the best way I could.

In the end I ended up with my final solution, which adds an extra function as well as doing a trick with `.reverse()` and `.sort()` functions in order to be able to delete duplicates of classes with lower grades. My solution is much more complex than it needed to be but that is part of the learning process. Now I know to think about which data structure would actually be best for this problem instead of thinking of what would get what done.

The key insight was learning that **sometimes the "clever" algorithmic solution isn't necessary** when the right data structure makes the problem trivial. This exercise taught me the importance of **data structure selection** as the foundation of good algorithm design.

---

## 📚 Key Learning Outcomes

* **Data Structure Selection**: Understanding how choice of data structure affects solution complexity
* **Algorithm Design**: Developing creative solutions with sorting and list manipulation
* **Code Architecture**: Separating concerns with dedicated utility functions
* **Edge Case Handling**: Managing mixed data types and boundary conditions
* **Performance Analysis**: Comparing algorithmic approaches and their trade-offs
* **Refactoring Skills**: Learning to identify when simpler solutions exist

---

## 🏆 Skills Demonstrated

- **Advanced List Operations**: Sorting, reversing, and duplicate removal
- **Dictionary Management**: Understanding when to use different data structures
- **Function Composition**: Building complex behavior from simple functions
- **Error Handling**: Graceful handling of edge cases and invalid inputs
- **Code Organization**: Clean separation of concerns and modular design

---

## 🎓 Course

This project was completed as part of the **MOOC.fi Python Programming course** and represents significant growth in algorithmic thinking and data structure understanding.
