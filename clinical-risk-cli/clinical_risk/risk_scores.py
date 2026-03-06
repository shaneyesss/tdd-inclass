# TODO: First write the purpose, the ins and outs, and the placeholder function for the qSOFA score.
# The function name should be qsofa_score, and it should take the following parameters: rr (respiratory rate) (int),
# sbp (systolic blood pressure) (int), and ams (altered mental status) (bool).
# The function should return an int representing the qSOFA score (0-3).

# purpose:  Calculate the qSOFA score based on the respiratory rate, systolic blood pressure, and altered mental status. 
# ins: rr (int), sbp (int), ams (bool)
# outs: int
def qsofa_score(rr: int, sbp: int, ams: bool) -> int:
    # Validate inputs
    if rr < 0:
        raise ValueError("Respiratory rate cannot be negative")
    if sbp < 0:
        raise ValueError("Systolic blood pressure cannot be negative")
    
    score = 0
    
    # Check respiratory rate criterion (>= 22)
    if rr >= 22:
        score += 1
    
    # Check systolic blood pressure criterion (<= 100)
    if sbp <= 100:
        score += 1
    
    # Check altered mental status criterion
    if ams:
        score += 1
    
    return score 

# TODO: First write the purpose, the ins and outs, and the placeholder function for the CHA2DS2-VASc score.
# The function name should be cha2ds2_vasc_score, and it should take the following parameters: age (int), female (bool),
# chf (congestive heart failure) (bool), htn (hypertension) (bool), dm (diabetes) (bool), stroke (bool),
# vascular (bool).
# The function should return an int representing the CHA2DS2-VASc score.

# purpose: Calculate the CHA2DS2-VASc score based on the patient's age, sex, and various clinical risk factors.
# ins: age (int), female (bool), chf (congestive heart failure) (bool), htn (hypertension) (bool), dm (diabetes) (bool), stroke (bool), vascular (bool)
# outs: int
def cha2ds2_vasc_score(age: int, female: bool, chf: bool, htn: bool, dm: bool, stroke: bool, vascular: bool) -> int:
    # Validate inputs
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    score = 0
    
    # Age scoring: 1 point if 65-74, 2 points if >= 75
    if age >= 75:
        score += 2
    elif age >= 65:
        score += 1
    
    # Congestive Heart Failure: 1 point
    if chf:
        score += 1
    
    # Hypertension: 1 point
    if htn:
        score += 1
    
    # Diabetes: 1 point
    if dm:
        score += 1
    
    # Stroke/TIA/Thromboembolism: 2 points
    if stroke:
        score += 2
    
    # Vascular disease: 1 point
    if vascular:
        score += 1
    
    # Female: 1 point
    if female:
        score += 1
    
    return score
