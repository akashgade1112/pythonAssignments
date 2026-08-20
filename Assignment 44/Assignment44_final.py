import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Step 1
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    dobj = pd.DataFrame(data)

    print(dobj)
    print(dobj.shape)
    print(dobj.columns)
    print(dobj.dtypes)

    # Step 2
    print(dobj.describe())

    # Step 3
    dobj["Total"] = dobj["Math"] + dobj["Science"] + dobj["English"]
    print(dobj)

    # Step 4
    result = dobj[dobj["Science"] > 85]
    print(result)

    # Step 5
    dobj["Name"] = dobj["Name"].replace("Pooja", "Puja")
    print(dobj)

    # Step 6
    dobj = dobj.sort_values("Total", ascending=False)
    print(dobj)

    # Step 7
    plt.bar(dobj["Name"], dobj["Total"])
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Student Names vs Total Marks")
    plt.show()

    # Step 8
    amit = dobj[dobj["Name"] == "Amit"]

    subjects = ["Math", "Science", "English"]

    marks = [
        amit["Math"].values[0],
        amit["Science"].values[0],
        amit["English"].values[0]
    ]

    plt.plot(subjects, marks, marker="o")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks")
    plt.show()

    # Step 9
    data2 = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 76, 88],
        "Science": [91, np.nan, 85]
    }

    dobj2 = pd.DataFrame(data2)

    print(dobj2)

    dobj2["Math"] = dobj2["Math"].fillna(dobj2["Math"].mean())
    dobj2["Science"] = dobj2["Science"].fillna(dobj2["Science"].mean())

    print(dobj2)

    # Step 10
    dobj = dobj.drop("English", axis=1)

    print("DataFrame after dropping English:")
    print(dobj)


if __name__ == "__main__":
    main()