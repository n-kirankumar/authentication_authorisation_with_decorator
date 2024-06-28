# main.py
from auth import authenticate, add_user
from crud import create_record, read_records, update_record, delete_record
from log import logger

if __name__ == "__main__":
    # Authenticate as admin
    if authenticate("admin", "adminpass"):
        # Add a new user
        add_user("new_user", "newuserpass", "user")

        # Create a new record
        create_record({
            'mobile': 919876543210,
            'email': 'valid_email@gmail.com',
            'gender': 'Male',
            'blood_group': 'O+',
            'dob': '1990-01-01'
        })

        # Read records
        records = read_records()
        logger.info(f"Records: {records}")

        # Update a record
        update_record(919876543210, {'email': 'updated_email@gmail.com'})

        # Delete a record
        delete_record(919876543210)

    # Attempt to perform actions as a normal user
    if authenticate("user", "userpass"):
        # This should fail because delete_record requires admin role
        delete_record(919876543210)

        # This should succeed
        read_records()
