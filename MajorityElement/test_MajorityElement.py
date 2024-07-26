from MajorityElement import majorityElement

def main():
    testMajorityElement()

def testMajorityElement():
    assert majorityElement([2, 1, 2]) == 2
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([3, 3, 3]) == 3
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majorityElement([100]) == 100

if __name__ == "__main__":
    main()