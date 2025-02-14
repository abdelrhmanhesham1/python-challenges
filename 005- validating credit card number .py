You and Fredrick are good friends. Yesterday, Fredrick received n credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

==>import re

def is_valid_credit_card(card):
    # Match either a continuous 16-digit number OR a properly hyphenated format
    if not re.match(r"^[4-6]\d{15}$|^[4-6]\d{3}(-\d{4}){3}$", card):
        return "Invalid"
    
    # Remove hyphens for further checks
    digits_only = card.replace("-", "")

    # Check for four or more consecutive repeated digits
    if re.search(r"(\d)\1{3,}", digits_only):
        return "Invalid"
    
    return "Valid"

# Read input and process each card
for _ in range(int(input())):
    print(is_valid_credit_card(input()))



==>Explanation:
Ensures the card starts with 4, 5, or 6.
Allows only digits or the xxxx-xxxx-xxxx-xxxx format.
Checks for exactly 16 digits.
Rejects cards containing characters other than digits and -.
Ensures no 4 consecutive repeating digits.

==>^ → Start of the string
[4-6] → First digit must be 4, 5, or 6
\d{3} → Followed by 3 digits
(-?\d{4}){3} → Three groups of 4 digits (optional hyphen before each group)
$ → End of the string
