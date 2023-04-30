CREATE TABLE
    IS601_Transactions(
        id int auto_increment PRIMARY KEY,
        account_src int NOT NULL,
        account_dest int NOT NULL,
        balance_change DECIMAL NOT NULL default 0.00,
        transaction_type VARCHAR(50),
        memo VARCHAR(300),
        expected_total DECIMAL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP        
    );