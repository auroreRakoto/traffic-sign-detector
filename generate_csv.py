import os
import csv

base_dir = 'data/GTSRB/origine/Train/GTSRB/Final_Training/Images'
#output_csv = 'data/GTSRB/origine/Train.csv'
output_csv = 'Train.csv'

with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Filename', 'Width', 'Height', 'Roi.X1', 'Roi.Y1', 'Roi.X2', 'Roi.Y2', 'ClassId'])

    for class_id in sorted(os.listdir(base_dir)):
        class_path = os.path.join(base_dir, class_id)
        if not os.path.isdir(class_path):
            continue
        for filename in os.listdir(class_path):
            if filename.endswith('.ppm'):
                # Données bidon pour les champs inutilisés
                writer.writerow([filename, 0, 0, 0, 0, 0, 0, int(class_id)])
