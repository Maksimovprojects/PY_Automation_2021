def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


def test_substring(full_string, substring):
    assert full_string in substring, f"'{full_string}' to be substring of '{substring}'"

# Bad practice (after falling one test, other one doesn't start)
if __name__ == "__main__":
    test_input_text(8, 11)
    test_input_text(11, 11)
    test_input_text(11, 15)
    test_substring(fulltext, some_value)
    test_substring(1, 1)
    test_substring(some_text, some)

# ----------------------------------------------------

# print("First_Test---------------------------")
# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
#
# # Sample Output 1:
# # output: expected 8, got 11
# print(test_input_text(8, 11))
#
# # Sample Input 2:
# # 11 11
# # output 2: empty line
# print(test_input_text(11, 11))
#
# # Sample Input 3:
# # output: expected 11, got 15
# print(test_input_text(11, 15))
#
# print("Second_Test---------------------------")
# def test_substring(full_string, substring):
#     assert full_string in substring, f"'{full_string}' to be substring of '{substring}'"
#
# print(test_substring(fulltext, some_value))
# # Sample Output 1: expected 'some_value' to be substring of 'fulltext'
#
# print(test_substring(1, 1))
# # Sample Output 2: empty
#
# print(test_substring(some_text, some))
# #Sample Output 3: empty

