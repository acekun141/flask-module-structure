from typing import Optional
from api.user.models import UserAdvance, UserBasic


def get_user_service(user_id: str) -> Optional[dict]:
    """
    Return user infomation or None if user does not exist

    Parameters:
        user_id (str): id of user

    Returns:
        dict: user's information 
    """
    user = UserBasic.query.filter_by(id=user_id).first()
    if user:
        return user.dict
    return None


def get_activate_user_data(user_id: str) -> Optional[dict]:
    """
    Returns user data if user does not deactivate

    Parameters:
        user_id (str): id of user

    Returns:
        data (dict): user data 
    """
    user = UserBasic.query.filter_by(id=user_id).first()
    if user and not user.deactivate:
        return user
    return None


def get_user_with_email(email: str) -> Optional[dict]:
    """
    Return user infomation or None if user does not exist

    Parameters:
        email (str): email of user

    Returns:
        dict: user's information 
    """
    user = UserBasic.query.filter_by(email=email).first()
    if user:
        return user.dict
    return None
    
