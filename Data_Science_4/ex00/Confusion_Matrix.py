import sys
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Leer los ficheros predictions.txt y truth.txt
def read_labels(file_path):
    with open(file_path, 'r') as file:
        labels = file.read().splitlines()
    return labels

def main(predictions_file, truth_file):
    # Leer las etiquetas de los archivos
    y_pred = read_labels(predictions_file)
    y_true = read_labels(truth_file)
    
    # Asegurarse de que ambos archivos tengan el mismo número de entradas
    assert len(y_pred) == len(y_true), "Los archivos no tienen el mismo número de etiquetas."

    # Calcular la matriz de confusión
    conf_matrix = confusion_matrix(y_true, y_pred, labels=["Jedi", "Sith"])

    # Imprimir la matriz de confusión
    print("Matriz de confusión:")
    print(conf_matrix)

    # Calcular e imprimir el informe de clasificación (precisión, recall, f1-score)
    print("\nReporte de Clasificación:")
    report = classification_report(y_true, y_pred, labels=["Jedi", "Sith"], target_names=["Jedi", "Sith"])
    print(report)

    # Calcular e imprimir la exactitud general (accuracy)
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Exactitud: {accuracy:.2f}")

    # Graficar la matriz de confusión usando seaborn
    plt.figure(figsize=(6,6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Pred: Jedi', 'Pred: Sith'], yticklabels=['Real: Jedi', 'Real: Sith'])
    plt.xlabel('Predicción')
    plt.ylabel('Valor Real')
    plt.title('Matriz de Confusión')
    plt.show()

# Ejecutar el script con los ficheros dados
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python Confusion_Matrix.py predictions.txt truth.txt")
        sys.exit(1)

    predictions_file = sys.argv[1]
    truth_file = sys.argv[2]

    main(predictions_file, truth_file)
