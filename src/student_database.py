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
    """
    IDEA:
        Make a separate function where all duplicates with a lower grade are removed.
        Attempt to repurpose code in print_student().
    Status completed
        
    """

    for name, values in students.items():
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
        print(f"{name}:\n {students[name]}")

    else:
        total = 0
        del_dups(students)
        comp_courses = len(students[name])

        print(f"{name}:")
        print(f" {comp_courses} completed courses:")
        
        for course, grade in students[name]:
            print(f"  {course} {grade}")
            total += grade
            
        print(f" average grade {total/comp_courses}")

def summary(students: dict):
    #del all duplicates with a lower grade
    del_dups(students)
    #get constants, so num of students
    num_students = len(students)

    #for most courses completed
    most_course_comp = 0
    count = 0
    most_course_student = ""
    
    #for highest avg
    total_grade = 0
    highest_avg = 0
    best_avg_student = ""


    for name, value in students.items():
        for course, grade in value:
            count += 1
            total_grade += grade

        avg = total_grade/count

        if avg > highest_avg:
            highest_avg = avg
            best_avg_student = f"best average grade {highest_avg} {name}"
            
        
        if count > most_course_comp:
            most_course_comp = count
            most_course_student = f"most courses completed {most_course_comp} {name}"
        
        total_grade = 0
        count = 0
    
    print(f"students {num_students}")
    print(most_course_student)
    print(best_avg_student)
            



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
    
    