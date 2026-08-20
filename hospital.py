def calculate_bill(
    age,
    appointment_type,
    consultation_duration,
    lab_charge,
    medicine_charge,
    insured=False
):
    if age <= 0:
        raise ValueError("Invalid age")

    if consultation_duration <= 0:
        raise ValueError("Invalid duration")

    consultation_fee = consultation_duration * 500

    if appointment_type == "emergency":
        consultation_fee *= 1.5

    elif appointment_type == "follow-up":
        consultation_fee *= 0.5

    elif appointment_type != "normal":
        raise ValueError("Invalid appointment type")

    if age >= 60:
        consultation_fee *= 0.8

    total = (
        consultation_fee
        + lab_charge
        + medicine_charge
    )

    insurance_coverage = total * 0.70 if insured else 0

    payable = total - insurance_coverage

    return {
        "consultation_fee": consultation_fee,
        "lab_charge": lab_charge,
        "medicine_charge": medicine_charge,
        "insurance": insurance_coverage,
        "payable": payable
    }