import pytest
def is_palindrome_valid(s:str) -> bool:
    # 1. Remove non-letters/numbers and make lowercase
    clean_s = "".join(c.lower() for c in s if c.isalnum())
    # 2. Compare to its reverse
    return clean_s == clean_s[::-1]

@pytest.mark.parametrize("s, expected", [
    # --- Basic Alphanumeric (True) ---
    ("racecar", True),            # 1. Standard lowercase
    ("RACECAR", True),            # 2. Standard uppercase
    ("12321", True),              # 3. Numbers only
    ("8", True),                  # 4. Single number
    ("0P", False),                # 5. Non-palindrome alphanumeric
    
    # --- Mixed Case & Spaces (True) ---
    ("Race Car", True),           # 6. Space between words
    ("  level  ", True),          # 7. Leading/trailing spaces
    ("A man a plan a canal Panama", True), # 8. Sentence with spaces
    ("12 21", True),              # 9. Numbers with spaces
    ("Noon", True),               # 10. Capitalized start
    
    # --- Symbols & Punctuation (Should be ignored) ---
    ("A man, a plan, a canal: Panama", True), # 11. Commas and colons
    ("race a car", False),        # 12. "raceacar" is not a palindrome
    ("Was it a car or a cat I saw?", True),   # 13. Question mark
    ("Madam, I'm Adam", True),    # 14. Apostrophe
    ("Stop! ...Post", True),      # 15. Exclamation and dots
    ("Able was I, ere I saw Elba", True), # 16. Historical phrase
    ("Never odd or even.", True),  # 17. Period at end
    ("ab_a", True),               # 19. Underscore
    ("1.2.3.2.1", True),          # 20. Dots between numbers
    
    # --- Edge Cases ---
    ("", True),                   # 21. Empty string (is a palindrome)
    (" ", True),                  # 22. Just a space (becomes empty, so True)
    ("!!!", True),                # 23. Just symbols (becomes empty, so True)
    ("a.", True),                 # 24. Letter and symbol
    (".a", True),                 # 25. Symbol and letter
    
    # --- Tricky False Cases ---
    ("race a car", False),        # 26. Classic NeetCode false case
    ("123 421", False),           # 27. Numbers that don't match
    ("palindrome", False),        # 28. Standard word fail
    ("abc", False),               # 29. Short fail
    ("32v23", False),             # 30. Almost numeric palindrome
    
    # --- Numeric & Letter Mix (True) ---
    ("a1b2b1a", True),            # 31. Perfectly symmetrical mix
    ("1a2", False),               # 32. Asymmetrical mix
    ("a b 1 2 1 b a", True),      # 33. Mix with spaces
    ("1 2 3 a 3 2 1", True),      # 34. Symmetrical mix
    ("M4D4M", True),              # 35. Leetspeak style
    
    # --- Long Phrases (True) ---
    ("Top spot!", True),          # 36. Short phrase
    ("My gym", True),             # 37. Mixed case/space
    ("Don't nod.", True),         # 38. Contraction
    ("I did, did I?", True),      # 39. Question
    ("Red rum, sir, is murder", True), # 40. Long symmetry
    ("Eva, can I see bees in a cave?", True), # 41. Long symmetry
    ("Sit on a potato pan, Otis.", True), # 42. Long symmetry
    ("No 'x' in Nixon", True),    # 43. Name phrase
    ("Step on no pets!", True),   # 44. Phrase
    ("Live on evasions, No iS_aVe No eviL", True), # 45. Extreme case
    
    # --- Random Failing Cases ---
    ("This is not it", False),    # 46. Random
    ("100%", False),              # 47. Only '100' remains
    ("Almost s om lA", True),     # 48. Symmetrical after cleaning
    ("No way", False),            # 49. Random
    ("Complexity", False)         # 50. Random

])

def test_isPalindrome(s:str, expected):
    assert is_palindrome_valid(s) == expected