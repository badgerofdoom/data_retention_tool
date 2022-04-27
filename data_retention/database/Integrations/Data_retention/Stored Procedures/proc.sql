
CREATE PROCEDURE [Data_retention].[Add_new_client]
	@clientid NVARCHAR(50),
	@client_name NVARCHAR(255),
	@Base_folder NVARCHAR(255),
	@client_folders NVARCHAR(4000),
	@Retention_polocies NVARCHAR(4000)
AS
BEGIN
	SET NOCOUNT ON;

	SELECT 1 as one
END
GO
