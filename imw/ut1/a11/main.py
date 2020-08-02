from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from vm import VirtualMachine

app = Flask(__name__)
vmachine = VirtualMachine("Azkaban", 16, 3.7, 1000, "debian")


@app.route("/")
def index():
    return render_template("index.html", vmachine=vmachine)


@app.route("/change_status/<new_status>")
def change_status(new_status):
    if new_status == "0":
        vmachine.stop()
    elif new_status == "1":
        vmachine.start()
    elif new_status == "2":
        vmachine.suspend()
    else:
        print("""
            0 = Parar.
            1 = Iniciar.
            2 = Apagar.
            """)
    return redirect("/")


@app.route("/run_process", methods=["GET", "POST"])
def run_process():
    if request.method == "POST":
        pid = int(request.form["pid"])
        ram = int(request.form["ram"])
        cpu = int(request.form["cpu"])
        hdd = int(request.form["hdd"])

        vmachine.run(pid, ram, cpu, hdd)
        return redirect("/")
    else:
        return render_template("run_process.html")


if __name__ == "__main__":
    app.run(debug=True)
