def process_loan(
    customer_id,
    age,
    monthly_salary,
    existing_loan,
    credit_score,
    employment_type,
    requested_amount,
    tenure_years
):
    if age < 18 or age > 70:
        raise ValueError("Invalid age")

    if monthly_salary <= 0:
        raise ValueError("Invalid salary")

    if requested_amount <= 0:
        raise ValueError("Invalid loan amount")

    if tenure_years <= 0:
        raise ValueError("Invalid tenure")

    if credit_score < 300 or credit_score > 900:
        raise ValueError("Invalid credit score")

    annual_salary = monthly_salary * 12

    dti = existing_loan / annual_salary

    employment_rates = {
        "salaried": 8.0,
        "self-employed": 9.0,
        "business": 9.5
    }

    if employment_type not in employment_rates:
        raise ValueError("Invalid employment type")

    interest_rate = employment_rates[employment_type]

    eligible_amount = monthly_salary * 20

    if credit_score < 600:
        eligible_amount *= 0.5
    elif credit_score < 700:
        eligible_amount *= 0.75

    eligible_amount = min(eligible_amount, requested_amount)

    # EMI calculation
    monthly_rate = interest_rate / 12 / 100
    months = tenure_years * 12

    if monthly_rate == 0:
        emi = eligible_amount / months
    else:
        emi = (
            eligible_amount
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

    approved = (
        credit_score >= 600
        and dti <= 0.5
        and requested_amount <= eligible_amount
    )

    return {
        "customer_id": customer_id,
        "dti": dti,
        "eligible_amount": eligible_amount,
        "interest_rate": interest_rate,
        "emi": emi,
        "approved": approved
    }