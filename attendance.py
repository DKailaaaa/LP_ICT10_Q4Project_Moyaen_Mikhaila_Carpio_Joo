import numpy as np
import matplotlib.pyplot as plt
from pyscript import document, display, window

mo = tu = we = th = fr = 0

x = np.arange(5)
labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def plot():
    global mo, tu, we, th, fr

    day = document.getElementById("day").value
    n = int(document.getElementById("num").value)

    if day == "monday":
        mo = n
    elif day == "tuesday":
        tu = n
    elif day == "wednesday":
        we = n
    elif day == "thursday":
        th = n
    elif day == "friday":
        fr = n

    y = np.array([mo, tu, we, th, fr])

    plt.clf()

    fig, ax = plt.subplots(figsize=(7,4))

    # ✅ THIS is the ONLY white background (graph itself)
    ax.set_facecolor("white")

    ax.plot(x, y, marker="o")

    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    ax.grid(True, color="#cccccc")

    plt.tight_layout()

    display(fig, target="plot-area", append=False)

# make callable from HTML
window.plot = plot