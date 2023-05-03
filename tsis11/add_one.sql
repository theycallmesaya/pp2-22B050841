CREATE OR REPLACE PROCEDURE add_one(contact_name VARCHAR(20), contact_number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT phone_book.number FROM phone_book WHERE contact_name = phone_book.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE phone_book SET number = contact_number WHERE phone_book.name = contact_name;
		ELSE
			INSERT INTO phone_book (name, number) VALUES (contact_name, contact_number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'
