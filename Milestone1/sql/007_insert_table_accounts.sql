INSERT IGNORE INTO
    IS601_Users (
        id,
        email, 
        username, 
        password
    )
VALUES (-1,'system_kb97@mail.com', 'system_kb97', '$2b$12$wRt2/iPKMDy3XQ1rDL1eg.8bnl5AG3KD2jWOW48Qnsb/oAYHG/xHC');

INSERT IGNORE INTO
    IS601_K_Accounts (
        id,
        account_number, 
        account_type,
        user_id
    )
VALUES (-1,'000000000000', 'World', -1);