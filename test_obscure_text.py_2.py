COURSES = ["ACIT2515", "ACIT1620", "ACIT0220", "ACIT0320",
"ACIT1420", "ACIT1951", "COMM0330", "COMM0350", "COMM1650",
"ENGL0220", "ENGL0510", "MATH0150", "ENGL0450", "PROJ0900",
"PROJ1360"]

def test_department_courses():
 assert department_courses([], "") == []
 assert department_courses(["ACIT1234"], "") == []
 assert department_courses(["ACIT1234"], "ACI") == []
 assert department_courses(["ACIT1234"], "ENGL") == []
 assert department_courses(["ACIT1234"], "ACIT") == ["ACIT1234"]
 assert department_courses(["ACIT1234", "ACIT5678"], "ACIT") == ["ACIT1234",
"ACIT5678"]
 assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ACIT") == ["ACIT1234", "ACIT5678"]
 assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ENGL") == ["ENGL1234"]

def department_courses(course_list, department):
    course_list = COURSES


if __name__ == "__main__":
    test_department_courses()