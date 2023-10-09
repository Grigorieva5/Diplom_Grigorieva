import data
import sender_stand_request
# import data


# Получение запроса на получения заказа по треку заказа
def get_track_id():
    track_id = sender_stand_request.post_new_order(data.order_body)
    return track_id.json()["track"]


# Тест на проверку кода ответа 200
def test_200():
    track_id = get_track_id()
    get_response = sender_stand_request.get_track_id(track_id)
    assert get_response.status_code == 200