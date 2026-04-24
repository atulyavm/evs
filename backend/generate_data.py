import pandas as pd
import numpy as np
import random
import os

def generate_water_data(num_samples=1500):
    chemicals_list = ['Lead', 'Mercury', 'Arsenic', 'Fluoride', 'Pesticides', 'Bacteria']
    
    treatment_map = {
        'Lead': 'Reverse Osmosis / Ion Exchange',
        'Mercury': 'Activated Carbon Filter',
        'Arsenic': 'Ion Exchange / Coagulation',
        'Fluoride': 'Activated Alumina',
        'Pesticides': 'Granular Activated Carbon',
        'Bacteria': 'UV Sterilization / Chlorination'
    }
    
    disease_map = {
        'Lead': 'Nervous system damage',
        'Mercury': 'Brain damage',
        'Arsenic': 'Skin lesions, Cancer',
        'Fluoride': 'Skeletal Fluorosis',
        'Pesticides': 'Hormonal imbalance',
        'Bacteria': 'Cholera, Typhoid'
    }

    data = []
    for _ in range(num_samples):
        ph = round(random.uniform(4.0, 10.0), 2)
        
        # Select 1 to 3 random chemicals
        num_chems = random.randint(0, 3)
        selected_chems = random.sample(chemicals_list, num_chems) if num_chems > 0 else []
        
        treatments = []
        diseases = []
        
        if not selected_chems:
            if ph < 6.5:
                treatments.append('pH adjustment (Add Alkaline)')
                diseases.append('Corrosion issues')
            elif ph > 8.5:
                treatments.append('pH adjustment (Add Acid)')
                diseases.append('Skin irritation')
            else:
                treatments.append('No treatment needed')
                diseases.append('Healthy')
        else:
            for chem in selected_chems:
                treatments.append(treatment_map[chem])
                diseases.append(disease_map[chem])
        
        # Handle noise (5%)
        if random.random() < 0.05:
            treatments = ['Consult Specialist / Advanced Filtration']
            diseases = ['Unknown Contamination Risk']

        # Flatten results
        treatment_str = " + ".join(sorted(list(set(treatments))))
        disease_str = ", ".join(sorted(list(set(diseases))))
        
        row = {
            'ph': ph,
            'treatment': treatment_str,
            'disease': disease_str
        }
        # Add binary columns for chemicals
        for chem in chemicals_list:
            row[chem] = 1 if chem in selected_chems else 0
            
        data.append(row)
        
    df = pd.DataFrame(data)
    output_path = os.path.join(os.path.dirname(__file__), 'water_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Dataset generated with {num_samples} samples at {output_path}")

if __name__ == "__main__":
    generate_water_data()
