from neverlose.utils import signature

DUMMY_SIGN = 'dc20a4d73447ac51689d6e03115aa135a8d734e610352dda818e830e70a60560'
DUMMY_EVENT = {
    'amount': 0.9,
    'username': 'A49',
    'unique_id': 89968,
    'item_id': 'E3yugw',
    'signature': DUMMY_SIGN
}
DUMMY_SECRET = 'key'


def test_generate():
    assert signature.generate(DUMMY_EVENT, DUMMY_SECRET) == DUMMY_SIGN


def test_validate():
    assert signature.validate(DUMMY_EVENT, DUMMY_SECRET)
