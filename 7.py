DECLARE
    a NUMBER := 10;
    b NUMBER := 25;
    c NUMBER := 15;
    greatest NUMBER;
BEGIN
    IF (a > b) AND (a > c) THEN
        greatest := a;
    ELSIF (b > c) THEN
        greatest := b;
    ELSE
        greatest := c;
    END IF;

    DBMS_OUTPUT.PUT_LINE('Greatest number is: ' || greatest);
END;
/
