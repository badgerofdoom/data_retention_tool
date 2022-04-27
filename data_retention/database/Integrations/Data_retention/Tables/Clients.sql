CREATE TABLE Data_retention.clients
(
    Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    clientId NVARCHAR(50) NOT NULL,
    client_name NVARCHAR(255) NOT NULL,
    base_folder NVARCHAR(255) NOT NULL,
	sub_folders NVARCHAR(4000) NOT NULL,
	retention_policies NVARCHAR(4000) NOT NULL
    )