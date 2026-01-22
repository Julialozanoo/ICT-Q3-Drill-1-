from pyscript import document

subjects = ["Science", "English", "Filipino", "ICT", "PE"]
units = (4, 3, 3, 2, 1)

def calculating_gwa(e=None):
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()

    grades = []
    for sub in subjects:
        value = document.getElementById(sub.lower()).value
        grades.append(float(value) if value else 0)

    weighted_sum = sum(g * u for g, u in zip(grades, units))
    total_units = sum(units)
    gwa = weighted_sum / total_units

    if gwa > 74:
        result = "PASS"
    else:
        result = "FAILED"

    output = f"--- Student Grades Summary ---\n"
    output += f"Name: {first_name} {last_name}\n\n"
    output += "Subjects:\n"

    for sub, grade in zip(subjects, grades):
        output += f"- {sub}: {grade}\n"

    output += f"\nGeneral Weighted Average: {gwa:.2f}\n"
    output += f"Result: {result}"

    document.getElementById("output").innerText = output

