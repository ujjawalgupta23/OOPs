# sort() method =     used with lists
# sorted() function = used with iterables

students = [("Ujjawal", 'M', 25),
            ("Naman", 'M', 23),
            ("Akarshi", 'F', 19),
            ("Ishi", 'F', 21)]

# students.sort()
print(sorted(students, key=lambda marks: marks[2]))
