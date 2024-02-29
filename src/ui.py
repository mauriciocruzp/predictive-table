import tkinter as tk
from src.syntax_analizer import analize


def run():
    window = tk.Tk()
    window.title("Analizador de sintaxis")
    window.geometry("700x500")

    input_label = tk.Label(window, text="Entrada")
    input_label.pack()

    input_text = tk.Text(window, height=10, width=70)
    input_text.insert(tk.END, "function a(var a : string; b : boolean)")
    input_text.pack()


    def analize_input():
        input = input_text.get("1.0", "end-1c")

        result, history = analize(input)

        if result:
            result_label.config(text="Cadena válida", fg="green")
        else:
            result_label.config(text="Cadena inválida", fg="red")
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, history)

    analize_button = tk.Button(window, text="Analizar", command=analize_input)
    analize_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    output_area = tk.Text(window, height=15, width=70)
    output_area.pack()

    window.mainloop()
