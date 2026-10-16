from learn_lists.learn import hello

def test_with_param():
    assert hello('Manny') == 'Hello Manny'

def test_default():
    assert hello() == 'Hello world'