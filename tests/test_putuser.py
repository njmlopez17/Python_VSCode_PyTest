import pytest
from utils.apis import APIs

@pytest.fixture(scope='module')
def apis():
    return APIs()

# test case 03 - update (put) a user

def test_update_user_validation(apis):
    user_data ={
        "name": "test user1",
        "username":"test QA2",
        "email":"test@gmail.com"
    }
    response = apis.put('users/1', user_data)

    # display the response
    print(response.json())

    # validate the response code if passed
    assert response.status_code == 200

    # output returned response code and flag as passed
    str_code = str(response.status_code)
    print("****Code " + str_code +" is passed!****")

    # ensure that the data key (username) is updated in the database
    assert response.json()['username'] =='test QA2'
    print("****User ID/Name " + str(response.json()['id']) + " and " + response.json()['username'] +" is updated!****")

    
