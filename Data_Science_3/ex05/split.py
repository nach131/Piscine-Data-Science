import sys
import pandas as pd
from sklearn.model_selection import train_test_split

def ft_split(file, train="Training_knight.csv", validation="Validation_knight.csv", test_size=20):
    """
    
    Parametros:
    - file (str): ruta del archivo CSV.
    - train (str): Fichero Training de salida CSV.
    - validation (str): Fichero Validation de salida CSV.
    - test_size (float): Proposicion del conjuto de datos, pordefecto 20 filas
    """

    data = pd.read_csv(file)

    data.head()

    # split data
    train_data, validation_data = train_test_split(data, test_size=test_size, random_state=42)

    # crea los nuevos ficheros
    train_data.to_csv(train, index=False)
    validation_data.to_csv(validation, index=False)

    print(f"Data successfully split!\nTraining set saved to {train} ({len(train_data)} rows)\n"
          f"Validation set saved to {validation} ({len(validation_data)} rows)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split.py <file.csv>")
    else:
        file = sys.argv[1]
        ft_split(file)

# Training_knight.csv: contiene los datos originales para el entrenamiento.
# Validation_knight.csv: contiene el 5 filas de los datos originales para la validación.