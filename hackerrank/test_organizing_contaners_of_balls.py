def organize_containers(containers):
    pass


def test_impossible():
    impossible_container = [[0, 2], [1, 1]]
    assert organize_containers(impossible_container) == "Impossible"


def test_possible():
    possible_container = [[1, 1][1, 1]]
    assert(organize_containers(possible_container) == "Possible"
