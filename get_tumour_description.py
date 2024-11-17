import json
import random

with open('tumour_types.json', 'r') as tumour_info:
    tumour_info = json.load(tumour_info)





# def get_tumour_details (predicted_class):
#     if predicted_class not in tumour_info:
#         return "Invalid tumor type or no detections found in image."
#
#     details = tumour_info[predicted_class]
#     print(f"--- Result for {predicted_class} ---")
#
#     # Handle Glioma or Meningioma with grades
#     if "grades" in details:
#         selected_grade = random.choice(details["grades"])
#         print(f"Grade: {selected_grade}")
#
#         # Choose prognosis based on grade
#         if selected_grade in ["I", "II"]:
#             prognosis = details["prognosis"]["grade_I_II"]
#         else:
#             prognosis = details["prognosis"].get(f"grade_{selected_grade}", details["prognosis"].get("grade_III_IV"))
#
#     # Handle Pituitary with types
#     elif "types" in details:
#         selected_type = random.choice(details["types"])
#         print(f"Type: {selected_type}")
#
#         # Choose prognosis based on type
#         prognosis = details["prognosis"].get(selected_type.replace(" ", "_"), "No specific prognosis available.")
#
#     # Handle No_Tumour
#     elif "description" in details:
#         print(f"Description: {details['description']}")
#         potential_cause = random.choice(details["potential_causes_of_symptoms"])
#         print(f"Potential Cause of Symptoms: {potential_cause}")
#         return
#
#     # Print severity markers and treatment options for tumor types
#     if "severity_markers" in details:
#         for marker, values in details["severity_markers"].items():
#             print(f"{marker.capitalize()}: {random.choice(values)}")
#
#     if "treatment_options" in details:
#         treatment = random.choice(details["treatment_options"])
#         print(f"Suggested Treatment: {treatment}")
#
#     # Print prognosis for tumor
#     print(f"Prognosis: {prognosis}")

def get_tumour_details (predicted_class):
    if predicted_class not in tumour_info:
        return "Invalid tumor type or no detections found in image."

    details = tumour_info[predicted_class]
    result = f"--- Result for {predicted_class} ---\n"

    # Handle Glioma or Meningioma with grades
    if "grades" in details:
        selected_grade = random.choice(details["grades"])
        result += f"Grade: {selected_grade}\n"

        # Choose prognosis based on grade
        if selected_grade in ["I", "II"]:
            prognosis = details["prognosis"]["grade_I_II"]
        else:
            prognosis = details["prognosis"].get(f"grade_{selected_grade}", details["prognosis"].get("grade_III_IV"))
        result += f"Prognosis: {prognosis}\n"

    # Handle Pituitary with types
    elif "types" in details:
        selected_type = random.choice(details["types"])
        result += f"Type: {selected_type}\n"

        # Choose prognosis based on type
        prognosis = details["prognosis"].get(selected_type.replace(" ", "_"), "No specific prognosis available.")
        result += f"Prognosis: {prognosis}\n"

    # Handle No_Tumour
    elif "description" in details:
        result += f"Description: {details['description']}\n"
        potential_cause = random.choice(details["potential_causes_of_symptoms"])
        result += f"Potential Cause of Symptoms: {potential_cause}\n"
        return result  # Return here since there's no additional data for "No_Tumour"

    # Severity markers and treatment options for other tumor types
    if "severity_markers" in details:
        for marker, values in details["severity_markers"].items():
            result += f"{marker.capitalize()}: {random.choice(values)}\n"

    if "treatment_options" in details:
        treatment = random.choice(details["treatment_options"])
        result += f"Suggested Treatment: {treatment}\n"

    return result  # Return the accumulated result string

