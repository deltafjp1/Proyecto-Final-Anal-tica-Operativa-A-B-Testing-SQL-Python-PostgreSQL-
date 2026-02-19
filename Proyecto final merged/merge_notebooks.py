import nbformat

files = [
    "telecomproyect.ipynb",
    "notebook proyecto final prueba ab.ipynb",
    "entrega de proyecto final sql- version revisada.ipynb"
]

merged = nbformat.v4.new_notebook()
merged.cells = []

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        nb = nbformat.read(fp, as_version=4)
        merged.cells.extend(nb.cells)

with open("Proyecto_Final_Completo.ipynb", "w", encoding="utf-8") as fp:
    nbformat.write(merged, fp)

print("OK: Proyecto_Final_Completo.ipynb creado correctamente")
