import requests
import logging as logger
import uuid

# All Utilities #
Endpoint = "https://todo.pixegami.io/"
def create_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    payload = {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
    return payload
def create_task(payload):
    return requests.put(Endpoint+"/create-task",json=payload)
def get_task(task_id):
    return requests.get(Endpoint+ f"/get-task/{task_id}")
def update_task(payload):
    return requests.put(Endpoint + "/update-task", json=payload)
def delete_task(task_id):
   return requests.delete(Endpoint+f"/delete-task/{task_id}")
def get_list_task(user_id):
    return requests.get(Endpoint+f"/list-tasks/{user_id}")

# Test Methods #
def test_get_endpoint():
    response = requests.get(Endpoint)
    logger.debug("the response is {}".format(response.json()))
    assert response.status_code==200
def test_create_multiple_user():
    n= 3
    for _ in range(n):
        payload= create_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200


def test_can_update_task():
    payload = create_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    #update task
    new_payload = {
        "content": "my updated content",
        "task_id":task_id,
        "user_id": payload["user_id"],
        "is_done": False
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code==200
    # get task
    Updated_task = get_task(task_id)

    assert  Updated_task.json()['task_id'] == task_id
    print(Updated_task.json()['task_id'])


# def test_can_create_task():
#     payload = create_payload()
#     response = requests.put(Endpoint+"/create-task",json=payload)
#     assert response.status_code == 200
#     create_task_response = response.json()
#     task_id = create_task_response["task"]["task_id"]
#     print(create_task_response)
#     response = requests.get(Endpoint+ f"/get-task/{task_id}")
#     getTaskResponse = response.json()
#     print ("response from get task id {}".format(getTaskResponse))
#     assert task_id ==getTaskResponse["task_id"]
