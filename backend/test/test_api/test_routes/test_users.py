import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
# @pytest.mark.parametrize(
#     "update_field, update_value",
#     (
#         ("username", "new_username"),
#         ("email", "new_email@email.com"),
#         ("bio", "new bio"),
#         ("image", "http://testhost.com/imageurl"),
#     ),
# )
# async def test_user_can_update_own_profile(
#     app: FastAPI,
#     authorized_client: AsyncClient,
#     test_db: AsyncSession,
#     token: str,
#     update_value: str,
#     update_field: str,
# ) -> None:
#     response = await authorized_client.put(
#         app.url_path_for("users:update-current-user"),
#         json={"user": {update_field: update_value}},
#     )
#     assert response.status_code == status.HTTP_200_OK

#     user_profile = UserInResponse(**response.json()).dict()
#     assert user_profile["user"][update_field] == update_value


@pytest.mark.anyio
async def test_user_can_not_access_own_profile_if_not_logged_in(
    app: FastAPI, 
    test_client: AsyncClient
):
    response = await test_client.get(
        app.url_path_for("user:get-self")   
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
@pytest.mark.anyio
async def test_user_can_access_own_profile_if_logged_in(
    app: FastAPI, 
    authorized_client: AsyncClient
):
    response = await authorized_client.get(
        app.url_path_for("user:get-self")
    )
    assert response.status_code == status.HTTP_200_OK