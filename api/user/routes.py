from api.user import user_route
from api.user.services import get_user_service
from api.utils.constants import ROLE
from api.utils.middlewares import token_require, valid_roles
from api.utils.response import error_not_found

@user_route.route('/', methods=['GET'])
@token_require
@valid_roles([ROLE["ADMIN"], ROLE["USER"]])
def get_user():
    data = get_user_service("123")
    if data:
        return {"user": data}

    return error_not_found()


@user_route.route('/', methods=['POST'])
@token_require
@valid_roles([ROLE["ADMIN"], ROLE["USER"]])
def update_user():
    return {"message": "ok"}

