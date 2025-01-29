import pytest
from datashow import Datashow
from room import Room

def test_datashow_creation():
    ds = Datashow()
    assert ds is not None

def test_room_creation():
    r = Room()
    assert r is not None

def test_datashow_allocation():
    ds = Datashow()
    r = Room()
    r.setDatashow(ds)

    assert r.hasDatashow() and not ds.isAvaliable()

def test_forbid_unavaliable_datashow_allocation():
    with pytest.raises(Exception) as e_info:
        r1 = Room()
        r2 = Room()
        ds = Datashow()

        r1.setDatashow(ds)
        r2.setDatashow(ds)
        assert str(e_info) is "Este datashow não está disponível no momento. Por favor libere o datashow ou escolha outro."

def test_forbid_room_with_datashow_to_set_datashow():
    with pytest.raises(Exception) as e_info:
        r = Room()
        ds1 = Datashow()
        ds2 = Datashow()

        r.setDatashow(ds1)
        r.setDatashow(ds2)
        assert str(e_info) is "Esta sala já possui um datashow. Por favor remova o datashow atual antes de adicionar um outro."

def test_free_datashow():
    ds = Datashow()
    r = Room()

    r.setDatashow(ds)
    r.freeDatashow()

    assert not r.hasDatashow() and ds.isAvaliable()
