from trie import Trie

def test():
    # Testing standard inputs
    assert t.search("grape") == False
    assert t.starts_with("gra") == False
    assert t.delete("grape") == False
    assert t.get_all() == None
    assert t.size() == 0

    t.insert("grape")
    assert t.size() == 1
    assert t.search("grape") == True
    assert t.search("gra") == False
    assert t.starts_with("gra") == ['grape']
    t.delete("grape")
    assert t.search("grape") == False
    assert t.size() == 0

    t.insert("grape")
    t.insert("grab")
    t.insert("grateful")
    t.insert("grand")
    assert t.size() == 4
    assert t.search("grand") == True
    assert t.search("bag") == False
    assert t.starts_with("gra") == ["grape", "grab", "grateful", "grand"]
    t.delete("grand")
    assert t.starts_with("gra") == ["grape", "grab", "grateful"]

    t.insert("orange")
    t.insert("orangutang")
    assert t.get_all() == "grape, grab, grateful, orange, orangutang"
    assert t.starts_with("gra") == ["grape", "grab", "grateful"]

    words = ["leaf", "leaves", "leaving", "let", "letter", "lake", "pineapple", "pyramid", "papaya"]
    for word in words:
        t.insert(word)
    assert t.size() == 14
    assert t.get_all() == "grape, grab, grateful, orange, orangutang, leaf, leaves, leaving, let, letter, lake, pineapple, pyramid, papaya"
    assert t.starts_with("lea") == ["leaf", "leaves", "leaving"]
    assert t.search("letter") == True
    assert t.search("let") == True
    assert t.starts_with("let") == ["let", "letter"]
    assert t.search("grateful") == True
    assert t.search("grate") == False

    old_words = ["orange", "orangutang", "grape", "grab", "grateful"]
    words = words + old_words
    for word in words:
        t.delete(word)
    assert t.size() == 0
    assert t.delete("grape") == False
    assert t.search("grape") == False
    assert t.size() == 0

    # Testing incorrect inputs
    incorrect_types = ["", [], "hello!?", 34, (2,0)]
    func = [t.insert, t.search, t.starts_with, t.delete]
    for f in func:
        for type in incorrect_types:
            try:
                f(type)
                raise AssertionError("{} should have resulted in TypeError".format(type))
            except TypeError:
                pass
    
t = Trie()
test()
print("great job girl slay")