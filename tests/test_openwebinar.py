from openwebinars.Openwebinar import Openwebinar

def test_openwebinar():
    taller_a = 'TallerA'
    openwebinar = Openwebinar(taller_a)
    assert str(openwebinar) == taller_a

    taller_b = 1
    openwebinar = Openwebinar(taller_b)
    assert str(openwebinar) == ''