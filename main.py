from pyscript import document, window

def add_student():
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if not name or not section or not subject:
        return

    message = f"Hi! My name is {name} from {section}. My favorite subject is {subject}."

    p = document.createElement("p")
    p.className = "student"
    p.innerText = message

    document.getElementById("list").appendChild(p)

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""

window.add_student = add_student