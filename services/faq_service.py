from models.faq import faq_to_json, validate_faq
from bson.objectid import ObjectId
from config import get_db

db = get_db()
faq_collection = db['faqs']

# Fetch all FAQs
def get_all_faqs():
    faqs = faq_collection.find()
    return [faq_to_json(faq) for faq in faqs]

# Fetch a single FAQ by ID
def get_faq_by_id(faq_id):
    faq = faq_collection.find_one({"_id": ObjectId(faq_id)})
    if faq:
        return faq_to_json(faq)
    return None

# Create a new FAQ
def create_faq(data):
    if validate_faq(data):
        new_faq = {
            "question": data["question"],
            "answer": data["answer"]
        }
        faq_id = faq_collection.insert_one(new_faq).inserted_id
        return faq_to_json(faq_collection.find_one({"_id": faq_id}))
    return None

# Update an existing FAQ
def update_faq(faq_id, data):
    if validate_faq(data):
        updated_faq = {
            "question": data["question"],
            "answer": data["answer"]
        }
        result = faq_collection.update_one(
            {"_id": ObjectId(faq_id)},
            {"$set": updated_faq}
        )
        if result.matched_count:
            return faq_to_json(faq_collection.find_one({"_id": ObjectId(faq_id)}))
    return None

# Delete an FAQ
def delete_faq(faq_id):
    result = faq_collection.delete_one({"_id": ObjectId(faq_id)})
    return result.deleted_count > 0
