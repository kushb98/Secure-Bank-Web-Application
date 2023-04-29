CREATE TABLE IF NOT EXISTS IS601_K_Accounts(
    id int AUTO_INCREMENT PRIMARY KEY,
    account_number varchar(12) unique DEFAULT (LPAD(user_id, 12, "0")),
    user_id int NOT NULL,
    balance DECIMAL NOT NULL DEFAULT 0.0,
    account_type varchar(12) UNIQUE,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
    -- this won't work for Bank project as this causes 1:1 account to user
    FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
    check (balance >= 0.0 AND LENGTH(account_number) = 12)
)