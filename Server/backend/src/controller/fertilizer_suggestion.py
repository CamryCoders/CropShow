def fertilizer_suggestion(N, P, K):

    suggestions = []

    if N < 50:
        suggestions.append(
            "Nitrogen is low. Consider nitrogen-rich fertilizer."
        )

    if P < 40:
        suggestions.append(
            "Phosphorus is low. Consider phosphate fertilizer."
        )

    if K < 40:
        suggestions.append(
            "Potassium is low. Consider potassium-rich fertilizer."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "NPK levels appear to be adequate."
        )

    return suggestions