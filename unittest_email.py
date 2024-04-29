import unittest
import re

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
VALID_PROVIDERS = [
    "gmail.com",
    "yahoo.com",
    "outlook.com"
]


def validate_email(email: str) -> bool:
    """
    Validates an email address based on regex format and providers.

    Parameters
    ----------
    email : str
        Provided email address by the user.

    Returns
    -------
    Bool
        True for valid email and false for the invalid ones.
    """
    if not re.match(EMAIL_REGEX, email):
        return False

    _, provider = email.split('@')

    if provider in VALID_PROVIDERS:
        return True
    else:
        return False


class TestEmail(unittest.TestCase):
    """Defines test methods to validate email address"""

    def test_email_validation(self):
        """Defines different test case for email address"""
        self.assertTrue(validate_email("abc@gmail.com"))
        self.assertTrue(validate_email("raj0101@gmail.com"))
        self.assertTrue(validate_email("rajendra_baskota@outlook.com"))
        self.assertFalse(validate_email("raj baskota@yahoo.com"))
        self.assertTrue(validate_email("def.111@yahoo.com"))
        self.assertFalse(validate_email("xyz@yahoop.com"))


if __name__ == "__main__":
    unittest.main()
