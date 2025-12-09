line = "Alice:82,Bob:91,carol:74,dan:91,ellen:59"
students = [(n.title(), int(g)) for n,g in (s.split(":") for s in line.split(","))]

print("Valid students:", len(students))
print("Average:", round(sum(g for _,g in students)/len(students),2))
high = max(g for _,g in students)
print("Top score:", high, "->", sorted(n for n,g in students if g==high))
print("Failing:", sorted(n for n,g in students if g<60))
