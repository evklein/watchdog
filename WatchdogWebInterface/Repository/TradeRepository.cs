using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Options;

public interface ITradeRepository
{
    Task<Dictionary<int, string>> LoadImportEndUseTypes();
    Task<Dictionary<string, string>> LoadImportCountries();
    Task<List<ImportRecord>> LoadImportRecordsForEndUseCode(int endUseCode, string countryCode);
}

public class TradeRepository : ITradeRepository
{
    private readonly ConnectionStringOptions _connectionStringOptions;

    public TradeRepository(IOptions<ConnectionStringOptions> connStringOptions)
    {
        _connectionStringOptions = connStringOptions.Value;
    }

    public async Task<Dictionary<int, string>> LoadImportEndUseTypes()
    {
        string query = "SELECT EndUseCode, EndUseDescription FROM ImportRecords GROUP BY EndUseCode;";
        Dictionary<int, string> endUseTypes = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        int endUseCode = reader.IsDBNull(0) ? -1 : reader.GetInt32(0);
                        string endUseDescription = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        endUseTypes.TryAdd(endUseCode, endUseDescription);
                    }
                }
            }
        }
        return endUseTypes;
    }

    public async Task<Dictionary<string, string>> LoadImportCountries()
    {
        string query = "SELECT CountryCode, CountryName FROM ImportRecords GROUP BY CountryCode;";
        Dictionary<string, string> countries = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        string countryCode = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        string countryName = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        countries.Add(countryCode, countryName);
                    }
                }
            }
        }
        return countries;
    }

    public async Task<List<ImportRecord>> LoadImportRecordsForEndUseCode(int endUseCode, string countryCode)
    {
        string query = $"SELECT * FROM ImportRecords WHERE EndUseCode = {endUseCode} AND CountryCode = '{countryCode}';";
        Console.WriteLine(query);
        List<ImportRecord> records = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        ImportRecord import = new();
                        import.Id = reader.IsDBNull(reader.GetOrdinal("Id")) ? -1 : reader.GetInt32(reader.GetOrdinal("Id"));
                        import.CountryCode = reader.IsDBNull(reader.GetOrdinal("CountryCode")) ? string.Empty : reader.GetString(reader.GetOrdinal("CountryCode"));
                        import.CountryName = reader.IsDBNull(reader.GetOrdinal("CountryName")) ? string.Empty : reader.GetString(reader.GetOrdinal("CountryName"));
                        import.EndUseCode = reader.IsDBNull(reader.GetOrdinal("EndUseCode")) ? -1 : reader.GetInt32(reader.GetOrdinal("EndUseCode"));
                        import.EndUseDescription = reader.IsDBNull(reader.GetOrdinal("EndUseDescription")) ? string.Empty : reader.GetString(reader.GetOrdinal("EndUseDescription"));
                        import.ValueForMonth = reader.IsDBNull(reader.GetOrdinal("ValueForMonth")) ? -1 : reader.GetInt64(reader.GetOrdinal("ValueForMonth"));
                        import.ValueYearToDate = reader.IsDBNull(reader.GetOrdinal("ValueYearToDate")) ? -1 : reader.GetInt64(reader.GetOrdinal("ValueYearToDate"));
                        import.Month = reader.IsDBNull(reader.GetOrdinal("Month")) ? -1 : reader.GetInt32(reader.GetOrdinal("Month"));
                        import.Year = reader.IsDBNull(reader.GetOrdinal("Year")) ? -1 : reader.GetInt32(reader.GetOrdinal("Year"));
                        records.Add(import);
                    }
                }
            }
        }
        return records;
    }
}