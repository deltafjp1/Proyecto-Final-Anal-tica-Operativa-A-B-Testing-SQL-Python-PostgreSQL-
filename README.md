# Proyecto Final — Analítica Operativa + A/B Testing + SQL (Python, PostgreSQL)

**Autor:** Francisco Pinto  
**Stack:** Python (pandas, numpy), Jupyter, SQL (PostgreSQL)

## Descripción
Este repositorio contiene el **proyecto final** del bootcamp, compuesto por **3 casos de uso distintos e independientes** (los datos de cada caso no están relacionados entre sí):

1) **Caso principal — Analítica operativa (Call Center / CallMeMaybe):**  
   Diagnóstico, manipulación y análisis para generar insights accionables sobre el desempeño de operadores (KPIs como *missed rate*, tiempo promedio de espera y llamadas salientes), con criterios cuantitativos para identificar ineficiencias.

2) **Caso 2 — Prueba A/B:**  
   Validación del desempeño de un experimento mediante embudo de conversión y pruebas de hipótesis.

3) **Caso 3 — SQL (PostgreSQL):**  
   Resolución de requerimientos y análisis con consultas SQL.

## Entregables principales
- 📓 **Notebook principal (analítica operativa):**  
  `Proyecto final merged/Proyecto_Final_Bootcamp_data_analitics.ipynb`

- 🧪 **Notebook A/B Testing y datasets:**  
  `Test AB/`

- 🗄️ **Notebook SQL:**  
  `proyecto final entrega SQL.ipynb`  
  `entrega de proyecto final sql- version revisada.ipynb`

- 🎞️ **Presentación (PDF):**  
  `presentacion proyecto Final telecomunicaciones.pdf`

- 📈 **Gráficas exportadas:**  
  `graficas_pdf/`

## Estructura del repositorio
- `Proyecto final merged/` → notebook final + script(s) de soporte (merge)
- `Test AB/` → notebook(s) y datasets del experimento
- `graficas_pdf/` → imágenes exportadas
- `*.csv` → datasets usados en los casos correspondientes

## Cómo ejecutar (local)
1) **Crear entorno virtual (opcional pero recomendado):**
   - Windows (PowerShell):
     - `python -m venv .venv`
     - `.venv\Scripts\Activate.ps1`

2) **Instalar dependencias:**
   - `pip install -r requirements.txt`

3) **Abrir Jupyter:**
   - `jupyter lab`
   - o `jupyter notebook`

4) **Ejecutar el notebook principal:**
   - `Proyecto final merged/Proyecto_Final_Bootcamp_data_analitics.ipynb`

## Notas
- Los casos de uso son **independientes**: cada carpeta/dataset corresponde a un caso distinto.
- Si algún dataset no debe publicarse por tamaño o privacidad, se recomienda moverlo a `data/` e ignorarlo con `.gitignore`.
