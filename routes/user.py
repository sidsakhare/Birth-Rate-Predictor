

from flask import Blueprint

user_bp =Blueprint('user', __name__)

@user_bp.route('/get_user', methods = ['GET'])
def get_user():
     return 'This is the get user request'

@user_bp.route('/add_user', methods = ['POST'])
def add_user():
     return 'This is the add user request'

@user_bp.route('/get_user', methods = ['PUT'])
def update_user():
     return 'This is the update user request'

@user_bp.route('/delete_user', methods = ['GET'])
def delete_user():
     return 'This is the delete user request'