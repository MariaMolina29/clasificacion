import os
import cv2
import numpy as np
import pandas as pd

# Define folder names
source_folder_name = "Manzanasf_renamed"
threshold_folder_name = "Manzanasf_Thresholded_Hu"

# Get the current directory (where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths for the source and destination folders
source_folder_path = os.path.join(current_dir, source_folder_name)
threshold_folder_path = os.path.join(current_dir, threshold_folder_name)

# Check if the source folder exists
if not os.path.exists(source_folder_path):
    print(f"The folder '{source_folder_name}' does not exist.")
    exit()

# Create the destination folder if it doesn't exist
os.makedirs(threshold_folder_path, exist_ok=True)

# Define the border size (in pixels)
border_size = 10  # Add a border to ensure proper detection

# Initialize a list to store Hu moments for each image
hu_moments_data = []
matriz_caracteristicas = []

# Iterate over each file in the source folder
for filename in os.listdir(source_folder_path):
    source_file_path = os.path.join(source_folder_path, filename)
      # Verificar que sea un archivo y no una carpeta
    if os.path.isfile(source_file_path):
        # Leer la imagen con OpenCV
        image = cv2.imread(source_file_path)

        # Verificar si el archivo es una imagen válida
        if image is not None:
            # Convertir la imagen a espacio de color HSV
            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            # Calcular el histograma de Hue y Saturación
            h_bins = 8
            s_bins = 10
            histograma = cv2.calcHist([hsv_image], [0, 1], None, [h_bins, s_bins], [0, 180, 0, 256])

            # Aplanar el histograma a un arreglo de 80 valores
            vector_histograma = histograma.flatten()

            # Agregar el vector a la matriz de características
            matriz_caracteristicas.append(vector_histograma)
            print(f"Convertido y procesado: {filename}")
        
    
            # Add a white border to the image
            image_with_border = cv2.copyMakeBorder(
                image,
                border_size, border_size, border_size, border_size,
                cv2.BORDER_CONSTANT,
                value=[255, 255, 255]  # White border
            )

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image_with_border, cv2.COLOR_BGR2GRAY)

            # Apply GaussianBlur to reduce noise
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

            # Apply Otsu's thresholding
            _, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Define a kernel for morphological operations
            kernel = np.ones((5, 5), np.uint8)  # Larger kernel to fill bigger gaps

            # Apply dilation and erosion separately
            dilated_image = cv2.dilate(threshold_image, kernel, iterations=3)  # Expand areas
            eroded_image = cv2.erode(dilated_image, kernel, iterations=3)  # Shrink back to original

            # Apply morphological closing as an additional step
            closed_image = cv2.morphologyEx(eroded_image, cv2.MORPH_CLOSE, kernel, iterations=1)

            # Remove the added border in the output mask
            final_mask = closed_image[border_size:-border_size, border_size:-border_size]

            # Calculate Hu Moments for the final mask
            moments = cv2.moments(final_mask)
            hu_moments = cv2.HuMoments(moments).flatten()  # Flatten to get a 1D array

            # Convert Hu Moments to log scale (optional)
            hu_moments_log = [-1 * np.sign(hu) * np.log10(abs(hu)) if hu != 0 else 0 for hu in hu_moments]

            # Append data with filename and Hu moments
            hu_moments_data.append([filename] + hu_moments_log)

            # Save the result
            threshold_file_path = os.path.join(threshold_folder_path, filename)
            cv2.imwrite(threshold_file_path, final_mask)
            print(f"Processed and saved: {filename}")
    else:
        print(f"Skipping invalid image file: {filename}")

matriz_caracteristicas = np.array(matriz_caracteristicas)
matriz_caracteristicas_df = pd.DataFrame(matriz_caracteristicas)

# Save Hu moments data to a CSV file
columns = ["Filename", "Hu_Moment_1", "Hu_Moment_2", "Hu_Moment_3", "Hu_Moment_4", "Hu_Moment_5", "Hu_Moment_6", "Hu_Moment_7"]
hu_moments_df = pd.DataFrame(hu_moments_data, columns=columns)
concatenated_df = pd.concat([hu_moments_df, matriz_caracteristicas_df], axis=1)
current_dir = os.getcwd()  # Replace with the desired directory

csv_file_path = os.path.join(current_dir, "Matriz_Manzanas.csv")
concatenated_df.to_csv(csv_file_path,index=False)

#csv_file_path = os.path.join(current_dir, "Hu_Moments_Apple.csv")
#hu_moments_df.to_csv(csv_file_path, index=False)
#print(f"Hu Moments saved to '{csv_file_path}'")

#print(f"All valid images have been processed and saved in the '{threshold_folder_name}' folder.")
