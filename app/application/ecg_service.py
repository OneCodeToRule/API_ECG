from datetime import datetime

from app.domain.models import ECG


fake_ecg_db = [
    {
        "id": 1,
        "date": "2023-12-23T08:00:00",
        "leads": [
            {"name": "I", "signal": [1, 2, -1, -2, 3, 4, -3, -4]},
            {"name": "II", "signal": [-1, -2, 1, 2, -3, -4, 3, 4]},
        ]
    },
    {
        "id": 2,
        "date": "2023-12-24T08:00:00",
        "leads": [
            {"name": "I", "signal": [2, -2, 3, -3, 4, -4]},
            {"name": "II", "signal": [-2, 2, -3, 3, -4, 4]},
        ]
    },
    {
        "id": 3,
        "date": "2023-12-25T08:00:00",
        "leads": [
            {"name": "I", "signal": [1, -1, 2, -2, 3, -3, 4, -4]},
            {"name": "II", "signal": [-1, 1, -2, 2, -3, 3, -4, 4]},
        ]
    }
]


class ECGNotFoundException(Exception):
    def __init__(self, ecg_id):
        self.ecg_id = ecg_id
        super().__init__(f"ECG con ID {ecg_id} no encontrado")


def get_insights_by_ecg_id(ecg_id: int):
    selected_ecg = next(
        (ecg for ecg in fake_ecg_db if ecg["id"] == ecg_id), None)
    if selected_ecg:
        zero_crossings = sum(abs(selected_ecg["leads"][i]["signal"][j]) > 0 and abs(
            selected_ecg["leads"][i]["signal"][j + 1]) > 0 for i in range(len(selected_ecg["leads"])) for j in range(len(selected_ecg["leads"][i]["signal"]) - 1))
        return {"ecg_id": ecg_id, "zero_crossings": zero_crossings}
    else:
        raise ECGNotFoundException(ecg_id)


def add_ecg(ecg: ECG):
    ecg_to_add = {
        "id": ecg.id,
        "date": datetime.now().isoformat(),
        "leads": ecg.leads
    }
    fake_ecg_db.append(ecg_to_add)

    return ecg
