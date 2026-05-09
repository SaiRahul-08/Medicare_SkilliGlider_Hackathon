from models.family_model import *


def fetch_family_members(user_id):
    return get_family_members(user_id)


def create_family_member(data):
    add_family_member(data)