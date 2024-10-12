try:
    import re

    def is_valid_email(email):
        if len(email) < 6:
            return False
        
        #first character is an alphabet
        if not email[0].isalpha():
            return False
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # This regex pattern is used to validate email addresses.
    # Explanation of the pattern: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # ^               : Asserts that the match must start at the beginning of the string.
    # [a-zA-Z0-9._%+-]+ : Matches the local part of the email (before the '@'):
    #                    - Allows uppercase and lowercase letters (a-z, A-Z)
    #                    - Allows digits (0-9)
    #                    - Allows special characters: dot (.), underscore (_), percent (%), plus (+), and hyphen (-)
    #                    - The '+' indicates one or more occurrences of the preceding character set.
    # @               : Matches the '@' symbol, which is required in all email addresses.
    # [a-zA-Z0-9.-]+ : Matches the domain part of the email (after the '@'):
    #                    - Allows letters (a-z, A-Z), digits (0-9), dots (.), and hyphens (-)
    #                    - The '+' again indicates one or more occurrences.
    # \.              : Escapes the dot (.) to match it literally, as it separates the domain and TLD.
    # [a-zA-Z]{2,}   : Matches the top-level domain (TLD):
    #                    - Requires at least two letters (like .com, .org).
    # $               : Asserts that the match must end at the end of the string.

    # Overall, this pattern ensures that the email follows a common structure.

        
        if not re.match(email_regex, email):
            return False
        
        if email.count('@') != 1:
            return False
        
        invalid_chars = set("!#$%^&*()")
        if any(char in invalid_chars for char in email):
            return False

        return True

    email = input("Enter your email: \n")

    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")


except Exception as e:
    print("error occured : ",e)
