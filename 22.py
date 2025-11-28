DECLARE
   v_empno     EMP.EMPNO%TYPE := 100;
   v_salary    EMP.SAL%TYPE;
   v_comm      EMP.COMM%TYPE;
   v_total     NUMBER;
BEGIN
   SELECT SAL, NVL(COMM,0)
   INTO v_salary, v_comm
   FROM EMP
   WHERE EMPNO = v_empno;

   v_total := v_salary + v_comm;

   DBMS_OUTPUT.PUT_LINE('Total Salary of Employee '||v_empno||' = '||v_total);
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Employee not found!');
END;
/
