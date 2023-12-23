import random
from datetime import datetime


ecg_data = []

for i in range(3):
    ecg = {
        "id": i + 1,
        "date": datetime.now().isoformat(),
        "leads": [
            {"name": "I", "signal": [random.randint(-10, 10) for _ in range(100)]},
            {"name": "II", "signal": [random.randint(-10, 10) for _ in range(100)]},
        ]
    }
    ecg_data.append(ecg)

for ecg in ecg_data:
    print(f"ECG ID: {ecg['id']}, Date: {ecg['date']}")
    for lead in ecg['leads']:
        zero_crossings = sum(1 for i in range(1, len(lead['signal'])) if lead['signal'][i-1] * lead['signal'][i] < 0)
        print(f"Lead: {lead['name']}, Zero Crossings: {zero_crossings}")