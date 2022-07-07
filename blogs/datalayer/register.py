from ..schema import schema
from ..hasher.hash import hash_passwor


def register_user_profile(request, db):
    new_user = schema.Profile(profile_id=request.profile_id, phone=request.phone, email=request.email, user_id=request.user_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def register_user(request, db):
    new_user = schema.User(name=request.name, email=request.email, password=hash_passwor(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user