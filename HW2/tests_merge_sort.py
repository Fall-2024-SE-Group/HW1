import hw2_debugging

def test_empty_list():
    assert hw2_debugging.merge_sort([]) == []

def test_sorted_list():
    assert hw2_debugging.merge_sort([11, 12, 13, 14, 15]) == [11, 12, 13, 14, 15]

def test_unsorted_list():
    assert hw2_debugging.merge_sort([8, 3, 1, 6, 2]) == [1, 2, 3, 6, 8]

def test_sorted_list():
    assert hw2_debugging.merge_sort([10, 4, 2, 8, 20]) == [2, 4, 8, 10, 20]


