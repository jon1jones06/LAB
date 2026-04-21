CREATE OR REPLACE PROCEDURE DELETE_SQL(p_value TEXT)
AS $$
BEGIN
   DELETE FROM phonebook
   WHERE username = p_value OR phone = p_value;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE INSERTORUPDATE(p_username TEXT, p_phone TEXT)
AS $$
BEGIN
   IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
      UPDATE phonebook
      SET phone = p_phone
      WHERE username = p_username;
   ELSE
      INSERT INTO phonebook(username, phone)
      VALUES(p_username, p_phone);
   END IF;
END; 
$$ LANGUAGE plpgsql;
