  if score < 3:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = {
        "length_criteria": length_criteria,
        "upper_criteria": upper_criteria,
        "lower_criteria": lower_criteria,
        "digit_criteria": digit_criteria,
        "special_criteria": special_criteria,
        "not_in_history": not_in_history,
        "not_common": not_common,
        "advanced_score": score,
        "strength": strength,
        "entropy": entropy,
        "suggestions": suggestions
    }

    return feedback
