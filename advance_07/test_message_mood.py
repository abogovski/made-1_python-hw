from message_mood import SomeModel, predict_message_mood


def test_predict_message_mood():
    assert predict_message_mood('0.2', SomeModel(), 0.3, 0.8) == 'неуд'
    assert predict_message_mood('0.2', SomeModel(), 0.2, 0.8) == 'норм'
    assert predict_message_mood('0.5', SomeModel(), 0.2, 0.8) == 'норм'
    assert predict_message_mood('0.5', SomeModel(), 0.2, 0.5) == 'норм'
    assert predict_message_mood('0.5', SomeModel(), 0.2, 0.4) == 'отл'
    assert predict_message_mood('nan', SomeModel(), 0.2, 0.4) == 'норм'
