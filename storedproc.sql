create or replace procedure test_proc()
    returns VARCHAR
    language SQL
    as
    $$
    create table HARNESS2(TRANS_DESC VARCHAR, MERCHANT_NAME VARCHAR);
    INSERT INTO HARNESS2 VALUES ('FLIP','FLIPKART');
    SELECT * FROM HARNESS2
    $$
    ;
