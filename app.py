import tkinter as tk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.archivo = "Archivo Nuevo"
        self.title(f"Editor de texto - {self.archivo}")
        self.rowconfigure(0, weight=1, minsize=600)
        self.columnconfigure(1, weight=1, minsize=600)

        self.__menu()
        self.__frame_botones()

        self.__texto = tk.Text(self)
        self.__texto.grid(row=0, column=1, sticky="nsew")

    # Funcion que crea el menu archivo
    def __menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        # Crear el menu archivo
        menu_archivo = tk.Menu(menu, tearoff=0)
        menu_archivo.add_command(label="Nuevo", command=self.__nuevo)
        menu_archivo.add_command(label="Abrir", command=self.__abrir)
        menu_archivo.add_command(label="Guardar", command=self.__guardar)
        menu_archivo.add_command(label="Guardar como", command=self.__guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.destroy)

        # Crear el menu editar
        menu_editar = tk.Menu(menu, tearoff=0)
        menu_editar.add_command(label="Cortar", command=self.__cortar)
        menu_editar.add_command(label="Copiar", command=self.__copiar)
        menu_editar.add_command(label="Pegar", command=self.__pegar)

        # Agregar los menus al menu principal
        menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu.add_cascade(label="Editar", menu=menu_editar)

    # Funcion que crea el frame de botones
    def __frame_botones(self):
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        # Crear los botones
        tk.Button(frame, text="Nuevo", command=self.__nuevo).grid(
            row=0, column=0, sticky="we", padx=5, pady=5
        )
        tk.Button(frame, text="Abrir", command=self.__abrir).grid(
            row=1, column=0, sticky="we", padx=5, pady=5
        )
        tk.Button(frame, text="Guardar", command=self.__guardar).grid(
            row=2, column=0, sticky="we", padx=5, pady=5
        )
        tk.Button(frame, text="Guardar como", command=self.__guardar_como).grid(
            row=3, column=0, sticky="we", padx=5, pady=5
        )

    # Funciones para los menus
    def __nuevo(self):
        self.archivo = "Archivo Nuevo"
        self.title(f"Editor de texto - {self.archivo}")
        self.__texto.delete("1.0", tk.END)

    def __abrir(self):
        self.archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
        )
        if self.archivo:
            with open(self.archivo, "r") as f:
                self.__texto.delete("1.0", tk.END)
                self.__texto.insert(tk.END, f.read())
            self.title(f"Editor de texto - {self.archivo}")

    def __guardar(self):
        if self.archivo == "Archivo Nuevo":
            self.__guardar_como()
        else:
            with open(self.archivo, "w") as f:
                f.write(self.__texto.get("1.0", tk.END))

    def __guardar_como(self):
        self.archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
        )
        if self.archivo:
            with open(self.archivo, "w") as f:
                f.write(self.__texto.get("1.0", tk.END))
            self.title(f"Editor de texto - {self.archivo}")

    def __cortar(self):
        self.__texto.event_generate("<<Cut>>")

    def __copiar(self):
        self.__texto.event_generate("<<Copy>>")

    def __pegar(self):
        self.__texto.event_generate("<<Paste>>")


if __name__ == "__main__":
    app = App()
    app.mainloop()
