# F24.Data_Retention

## Summary
The process which will run against client files that have been imported from
SFTP transfers and will delete any redundant data

## Retention Policies

will need to workout the file types as unsure at this point

1. files older than 1 calendar month
2. files bigger than ?kb and older than 1 week
3. folder size bigger than xGB and files older than 2 weeks

## Process

will need to confirm frequency of running initially thinking daily

1. Get client from client table (will include parent data folder)
2. Get list of files for client (contain file identifier and sub folder root)
3. iterate through client files
4. Get list of retention policy exclusions applicable for each file
5. delete data for each client based on the appropriate retention policies
6. log what has been deleted for each client and when

## Design

- Will need a table structure something like
   - Clients
   - Client_files
   - client_Data_Retention_Policy_exclusions
   - client data retention logs (add clients, files and exclusion activities. also to log results of each cycle)
   
- will need stored procs to:
   - add a client
   - add a client file
   - add a data retention policy exclusion at file level
   - delete a client with cascade
   - delete a client file with cascade
   - delete a data retention policy exclusion

- create a script to execute retention policies