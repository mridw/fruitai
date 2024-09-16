from bson.objectid import ObjectId

# Converts MongoDB document to a JSON-serializable format
def faq_to_json(faq):
    return {
        "id": str(faq["_id"]),
        "question": faq["question"],
        "answer": faq["answer"]
    }

# Validates that the FAQ input data is valid
def validate_faq(data):
    if "question" not in data or "answer" not in data:
        return False
    return True
