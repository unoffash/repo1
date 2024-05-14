create or replace procedure test_proc()
    language SQL
    as
    $$
    create table HARNESS2(TRANS_DESC VARCHAR, MERCHANT_NAME VARCHAR);
    INSERT INTO HARNESS2 ('FLIP','FLIPKART')
    SELECT * FROM HARNESS2
    $$
    ;