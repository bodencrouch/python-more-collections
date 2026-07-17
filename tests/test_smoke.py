def test_import():
    from python_more_collections import CaseInsensitiveDict, OrderedSet
    s = OrderedSet(["a", "b", "a"])
    assert list(s) == ["a", "b"]
    d = CaseInsensitiveDict.from_dict({"Foo": 1})
    assert d["foo"] == 1
