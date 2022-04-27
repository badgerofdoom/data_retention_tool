CREATE TABLE Data_retention.[log]
(
    Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    log_time DATETIME NOT NULL,
    purge_id CHAR(12) NOT NULL,
    log_type NVARCHAR(50) NOT NULL,
    log_message VARCHAR(4000) NOT NULL
    )