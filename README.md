# Clasificación de Arándanos y Manzanas
Integrantes: David Téllez, Carolina Herrera y María alejandra Molina

Este proyecto clasifica imágenes de frutas (arándanos y manzanas) mediante el análisis de características visuales extraídas de las imágenes. El flujo completo incluye la extracción de características, la creación de una matriz de datos y el entrenamiento de un modelo de aprendizaje.

---

## **Estructura del Proyecto**

### **1. Renombrar las Imágenes**
- **Archivo**: `Cambia_nombre.py`
- Este script renombra las imágenes de entrada para estandarizar su formato, facilitando su procesamiento posterior.
- **Carpetas**:
  - Entrada: `Manzanasf`
  - Salida: `Manzanasf_renamed`

### **2. Extracción de Características**
- **Archivo**: `Final_caracte.py`
- Se extraen dos tipos de características de cada imagen:
  1. **Histogramas HSV**: Se calculan y aplanan en un vector de 80 valores.
  2. **Momentos de Hu**: Se obtienen aplicando los siguientes pasos de procesamiento:
     - Conversión a escala de grises.
     - Desenfoque gaussiano para reducción de ruido.
     - Umbralización de Otsu para segmentación.
     - Operaciones morfológicas (dilatación, erosión y cierre) para mejorar los contornos.
- **Resultados**: 
  - `Matriz_Manzanas.csv` 
  - `Matriz_Blueberries.csv`

### **3. Concatenación de Matrices**
- **Archivo**: `MatrizFinal.py`
- Combina las características de manzanas y arándanos en una sola matriz (`Matriz_Final.csv`).
- Agrega una columna que indica la clase:
  - `0` para arándanos.
  - `1` para manzanas.

### **4. Entrenamiento del Modelo**
- **Archivo**: `modelo.py`
- Modelo utilizado: **k-Nearest Neighbors (kNN)**.
- **Pasos**:
  1. Dividir los datos en conjuntos de entrenamiento (70%) y prueba (30%).
  2. Entrenar el modelo con las características concatenadas.
  3. Evaluar el modelo con los datos de prueba.
- **Métricas**:
  - Matriz de confusión.
  - Precisión del modelo.

---

## **Archivos Generados**
- `Matriz_Manzanas.csv`: Características HSV y Momentos de Hu de las imágenes de manzanas.
- `Matriz_Blueberries.csv`: Características HSV y Momentos de Hu de las imágenes de arándanos.
- `Matriz_Final.csv`: Matriz combinada con las características de ambas frutas, incluyendo la clase (`1` o `0`).

---

## **Requisitos del Entorno**
- **Python 3.x** con las siguientes bibliotecas:
  - `numpy`
  - `pandas`
  - `opencv-python`
  - `scikit-learn`

---

## **Instrucciones de Uso**

1. Coloca las imágenes de entrada en carpetas separadas:
   - Manzanas: `Manzanasf`
   - Arándanos: `Blueberries`

2. Ejecuta los scripts en el siguiente orden:
   1. `Cambia_nombre.py`
   2. `Final_caracte.py`
   3. `MatrizFinal.py`
   4. `modelo.py`

3. Observa los resultados del modelo entrenado en la consola.

---
