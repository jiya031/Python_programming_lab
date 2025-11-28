DECLARE
   n NUMBER := 10;   -- you can take user input or set manually
   i NUMBER := 1;
BEGIN
   WHILE i <= n LOOP
      DBMS_OUTPUT.PUT_LINE(i);
      i := i + 1;
   END LOOP;
END;
/
