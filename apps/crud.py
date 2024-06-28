# crud.py
from utils import is_valid_mobile, is_valid_email, is_valid_gender, is_valid_blood_group, is_valid_dob
from log import logger
from constants import data
from auth import authorize, authenticate_required

@authenticate_required
def create_record(record):
    """
    Creates a new record.
    """
    if is_valid_mobile(record['mobile']) and is_valid_email(record['email']) and is_valid_gender(record['gender']) and is_valid_blood_group(record['blood_group']) and is_valid_dob(record['dob']):
        data['records'].append(record)
        logger.info("Record created successfully")
        return True
    else:
        logger.error("Record creation failed due to invalid data")
        return False

@authenticate_required
def read_records():
    """
    Reads all records.
    """
    logger.info("Reading all records")
    return data['records']

@authenticate_required
def update_record(mobile, updated_record):
    """
    Updates an existing record.
    """
    for record in data['records']:
        if record['mobile'] == mobile:
            record.update(updated_record)
            logger.info(f"Record with mobile {mobile} updated successfully")
            return True
    logger.error(f"Record with mobile {mobile} not found")
    return False

@authenticate_required
@authorize('admin')
def delete_record(mobile):
    """
    Deletes a record.
    """
    for record in data['records']:
        if record['mobile'] == mobile:
            data['records'].remove(record)
            logger.info(f"Record with mobile {mobile} deleted successfully")
            return True
    logger.error(f"Record with mobile {mobile} not found")
    return False
