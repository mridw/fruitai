from flask import Blueprint, jsonify, request, abort
from services.faq_service import get_all_faqs, get_faq_by_id, create_faq, update_faq, delete_faq

faq_bp = Blueprint('faq_bp', __name__)

# 1. GET all FAQs
@faq_bp.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = get_all_faqs()
    return jsonify(faqs), 200

# 2. GET a single FAQ by ID
@faq_bp.route('/faqs/<faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = get_faq_by_id(faq_id)
    if faq:
        return jsonify(faq), 200
    return jsonify({"error": "FAQ not found"}), 404

# 3. POST a new FAQ
@faq_bp.route('/faqs', methods=['POST'])
def create_new_faq():
    data = request.json
    new_faq = create_faq(data)
    if new_faq:
        return jsonify(new_faq), 201
    return jsonify({"error": "Invalid FAQ data"}), 400

# 4. PUT to update an existing FAQ
@faq_bp.route('/faqs/<faq_id>', methods=['PUT'])
def update_existing_faq(faq_id):
    data = request.json
    updated_faq = update_faq(faq_id, data)
    if updated_faq:
        return jsonify(updated_faq), 200
    return jsonify({"error": "Invalid FAQ data or FAQ not found"}), 400

# 5. DELETE an FAQ
@faq_bp.route('/faqs/<faq_id>', methods=['DELETE'])
def delete_existing_faq(faq_id):
    if delete_faq(faq_id):
        return jsonify({"message": "FAQ deleted successfully"}), 200
    return jsonify({"error": "FAQ not found"}), 404
