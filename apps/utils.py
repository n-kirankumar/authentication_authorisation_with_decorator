# utils.py
import re
from constants import VALID_COUNTRY_LIST, EXCLUDED_NUMBERS, VALID_GENDERS, VALID_BLOOD_GROUPS
from log import logger

def is_valid_mobile(mobile):
    """
    Check if the mobile number is valid.
    """
    converted_str = str(mobile)
    mobile_num = int(converted_str[2:])

    if not isinstance(mobile, int):
        logger.error(f"Invalid mobile number type - {type(mobile)}")
        return False

    if len(converted_str) != 12:
        logger.error(f"Invalid Mobile number length {len(converted_str)} and valid length is 12")
        return False

    if mobile_num in EXCLUDED_NUMBERS:
        logger.info(f"{mobile_num} is in the excluded list")
        return True

    if converted_str[:2] not in VALID_COUNTRY_LIST:
        logger.error(f"Invalid country code - {converted_str[:2]} valid country codes are {VALID_COUNTRY_LIST}")
        return False

    logger.info("Mobile verification is successful")
    return True

def is_valid_email(email):
    """
    Check if the email is valid.
    """
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        logger.info("Email verification is successful")
        return True
    else:
        logger.error("Invalid email format")
        return False

def is_valid_gender(gender):
    """
    Check if the gender is valid.
    """
    if gender in VALID_GENDERS:
        logger.info("Gender verification is successful")
        return True
    else:
        logger.error(f"Invalid gender - {gender}. Valid genders are {VALID_GENDERS}")
        return False

def is_valid_blood_group(blood_group):
    """
    Check if the blood group is valid.
    """
    if blood_group in VALID_BLOOD_GROUPS:
        logger.info("Blood group verification is successful")
        return True
    else:
        logger.error(f"Invalid blood group - {blood_group}. Valid blood groups are {VALID_BLOOD_GROUPS}")
        return False

def is_valid_dob(dob):
    """
    Check if the date of birth is valid.
    """
    try:
        if re.match(r'\d{4}-\d{2}-\d{2}', dob):
            logger.info("DOB verification is successful")
            return True
        else:
            logger.error("Invalid DOB format. Required format is YYYY-MM-DD")
            return False
    except Exception as e:
        logger.error(f"DOB validation error: {e}")
        return False
