using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Options;
using WatchdogWebInterface.Models;

public interface IPipelineRepository
{
    List<string> LoadDestinations();
    List<FetchRecord> LoadFetchRecordsForDestination(string destination);
}

public class PipelineRepository : IPipelineRepository
{
    private readonly ConnectionStringOptions _connectionStringOptions;

    public PipelineRepository(IOptions<ConnectionStringOptions> connStringOptions)
    {
        _connectionStringOptions = connStringOptions.Value;
    }

    public List<string> LoadDestinations()
    {
        string query = "SELECT DISTINCT(Destination) FROM FetchRecords;";
        List<string> destinations = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.FetchDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        string nextDestination = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        destinations.Add(nextDestination);
                    }
                }
            }
        }
        return destinations;
    }

    public List<FetchRecord> LoadFetchRecordsForDestination(string destination)
    {
        string query = $"SELECT * FROM FetchRecords WHERE Destination = '{destination}';";
        List<FetchRecord> records = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.FetchDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {                        
                        int id = reader.IsDBNull(0) ? -1 : reader.GetInt32(0);
                        string source = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        int numberOfElementsAdded = reader.IsDBNull(3) ? -1 : reader.GetInt32(3);
                        DateTime dateTimeOfRecord = reader.IsDBNull(4) ? DateTime.MinValue : reader.GetDateTime(4);
                        records.Add(new FetchRecord()
                        {
                            Id = id,
                            Source = source,
                            Destination = destination,
                            NewRecordsAdded = numberOfElementsAdded,
                            OperationRan = dateTimeOfRecord
                        });
                    }
                }
            }
        }
        return records;
    }
}