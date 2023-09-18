import re

def is_valid_date(date_string):
    
    date_pattern = r"^(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4}$"

    if re.match(date_pattern, date_string):
        return True
    else:
        return False

date1 = "July 08, 2009"
date2 = "Dec 3, 22"  
print(is_valid_date(date1))  
print(is_valid_date(date2))  

#--------------------------------------------------------------

import re

def is_valid_credit_card_number(card_number):
    pattern = r"^(3|4|9)\d{3}-\d{4}-\d{4}-\d{4}$"

    if re.match(pattern, card_number):
        # Remove hyphens and check for consecutive repeated digits
        card_number = card_number.replace("-", "")
        for i in range(len(card_number) - 1):
            if card_number[i] == card_number[i + 1]:
                return False

        return True

    return False

card1 = "3999-1234-5678-9012"
card2 = "4867-1234-1234-1234"  
print(is_valid_credit_card_number(card1))  
print(is_valid_credit_card_number(card2))  
