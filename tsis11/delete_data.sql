CREATE OR REPLACE PROCEDURE delete_data(data_to_delete VARCHAR(20))
	AS $$	
	BEGIN
	DELETE FROM phone_book WHERE name = data_to_delete OR number = data_to_delete;
	END; $$
	LANGUAGE plpgsql