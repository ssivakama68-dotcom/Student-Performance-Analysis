import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_performance.csv")

data["Total"] = data[["Maths", "Science", "English"]].sum(axis=1)
data["Average"] = data["Total"] / 3

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(grade)

print(data)

topper = data.loc[data["Average"].idxmax()]
print("\nTop Performer:")
print(topper)

plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data["Grade"].value_counts().plot(kind="bar")
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()