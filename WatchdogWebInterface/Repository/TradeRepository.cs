using System.Composition;
using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Options;
using WatchdogWebInterface.Models;
using WatchdogWebInterface.Models.DTO;

public interface ITradeRepository
{
    Task<Dictionary<int, string>> LoadImportEndUseTypes();
    Task<Dictionary<string, string>> LoadImportCountries();
    Task<List<ImportRecord>> LoadImportRecordsForEndUseCode(int endUseCode, string countryCode);
    Task<List<ImportItemDTO>> LoadTop10Imports();
    Task<List<ImporterDTO>> LoadTop10Importers();
    Task<List<ExportItemDTO>> LoadTop10Exports();
    Task<List<ExportRecord>> FetchTotalExportsAll();
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
        string query = "SELECT EndUseCode, EndUseDescription FROM ImportRecords GROUP BY EndUseCode ORDER BY EndUseDescription ASC;";
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

    public async Task<List<ImportItemDTO>> LoadTop10Imports()
    {
        string query = "SELECT EndUseCode, EndUseDescription, SUM(ValueForMonth) FROM ImportRecords GROUP BY EndUseDescription ORDER BY SUM(ValueForMonth) DESC LIMIT 10 OFFSET 1;";
        List<ImportItemDTO> top10ImportsByCode = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        int endUseCode = reader.IsDBNull(0) ? -1 : reader.GetInt32(0);
                        string endUseDescription = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        long totalValueSince2013 = reader.IsDBNull(2) ? -1 : reader.GetInt64(2);
                        top10ImportsByCode.Add(new ImportItemDTO
                        {
                            EndUseCode = endUseCode,
                            EndUseDescription = endUseDescription,
                            TotalImportValueForPeriod = totalValueSince2013
                        });
                    }
                }
            }
        }
        return top10ImportsByCode;
    }

    public async Task<List<ImporterDTO>> LoadTop10Importers()
    {
        string query = "SELECT CountryCode, CountryName, SUM(ValueForMonth) FROM ImportRecords GROUP BY CountryCode ORDER BY SUM(ValueForMonth) DESC LIMIT 10 OFFSET 1;";
        List<ImporterDTO> top10Importers = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        string countryCode = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        string countryName = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        long totalValueSince2013 = reader.IsDBNull(2) ? -1 : reader.GetInt64(2);
                        top10Importers.Add(new ImporterDTO
                        {
                            CountryCode = countryCode,
                            CountryName = countryName,
                            TotalValueImportedFromForPeriod = totalValueSince2013
                        });
                    }
                }
            }
        }
        return top10Importers;
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


    public async Task<List<ExportItemDTO>> LoadTop10Exports()
    {
        string query = "SELECT CommodityId, CommodityDescription, SUM(TotalValueForMonth) FROM ExportRecords GROUP BY CommodityId ORDER BY SUM(TotalValueForMonth) DESC LIMIT 10 OFFSET 1;";
        List<ExportItemDTO> top10ExportsByCode = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        string commodityId = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        string commodityDescription = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        long totalValueSince2013 = reader.IsDBNull(2) ? -1 : reader.GetInt64(2);
                        top10ExportsByCode.Add(new ExportItemDTO
                        {
                            CommodityId = commodityId,
                            CommodityName = commodityDescription,
                            TotalValueExportedForPeriod = totalValueSince2013
                        });
                    }
                }
            }
        }
        return top10ExportsByCode;
    }

    public async Task<List<ExportRecord>> FetchTotalExportsAll()
    {
        string query = "SELECT * FROM ExportRecords WHERE CommodityID = '-';";
        List<ExportRecord> exportRecords = new List<ExportRecord>();
        using (var connection = new SqliteConnection(_connectionStringOptions.TradeDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        string commodityId = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        string commodityDescription = reader.IsDBNull(2) ? string.Empty : reader.GetString(2);
                        long totalValueForMonth = reader.IsDBNull(3) ? -1 : reader.GetInt64(3);
                        long totalVesselValueForMonth = reader.IsDBNull(4) ? -1 : reader.GetInt64(4);
                        long totalAirValueForMonth = reader.IsDBNull(5) ? -1 : reader.GetInt64(5);
                        long totalCardCountForMonth = reader.IsDBNull(6) ? -1 : reader.GetInt64(6);
                        int month = reader.IsDBNull(7) ? -1 : reader.GetInt32(7);
                        int year = reader.IsDBNull(8) ? -1 : reader.GetInt32(8);
                        exportRecords.Add(new ExportRecord
                        {
                            CommodityId = commodityId,
                            CommodityDescription = commodityDescription,
                            TotalValueForMonth = totalValueForMonth,
                            VesselValueForMonth = totalVesselValueForMonth,
                            AirValueForMonth = totalAirValueForMonth,
                            CardCount = totalCardCountForMonth,
                            Month = month,
                            Year = year
                        });
                    }
                }
            }
        }
        return exportRecords;
    }
}