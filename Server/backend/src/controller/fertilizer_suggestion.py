from flask import request,jsonify
def fertilizer_suggestion():
    data=request.get_json()
    N=data.get("N")
    K=data.get("K")
    P=data.get("P")

    suggestions = {}

    if N < 50:
        suggestions[0]= "Nitrogen is low. Consider nitrogen-rich fertilizer."
    if P < 40:
        suggestions[1]=  "Phosphorus is low. Consider phosphate fertilizer."
        
    if K < 40:
        suggestions[2]=  "Potassium is low. Consider potassium-rich fertilizer."
        
    if len(suggestions) == 0:
        suggestions[3]=  "NPK levels appear to be adequate."
    print(suggestions)
        

    return jsonify(suggestions)


