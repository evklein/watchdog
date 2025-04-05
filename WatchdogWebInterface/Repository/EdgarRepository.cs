using Microsoft.Data.Sqlite;

public interface IEdgarRepository
{
    List<SECEntity> LoadSECEntities();
    List<SeriesClass> LoadFunds(string cik);
    List<NPORTFiling> LoadFilings(string cik, string seriesClassCompositeKey);
    List<FundHolding> LoadHoldings(string filingId);
}

public class EdgarRepository : IEdgarRepository
{
    public List<SECEntity> LoadSECEntities()
    {
        string query = "SELECT * FROM SECEntities";
        List<SECEntity> entities = new();
        using (var connection = new SqliteConnection("Data Source=../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    Console.WriteLine("Inside reader");
                    // Loop through all rows in the result set
                    while (reader.Read())
                    {
                        SECEntity entity = new();

                        // Safe way to get string values that might be NULL
                        entity.CIK = reader.IsDBNull(reader.GetOrdinal("CIK")) ? null : reader.GetString(reader.GetOrdinal("CIK"));
                        entity.Name = reader.IsDBNull(reader.GetOrdinal("Name")) ? null : reader.GetString(reader.GetOrdinal("Name"));
                        entity.EntityType = reader.IsDBNull(reader.GetOrdinal("EntityType")) ? null : reader.GetString(reader.GetOrdinal("EntityType"));
                        entity.IncorporationState = reader.IsDBNull(reader.GetOrdinal("IncorporationState")) ? null : reader.GetString(reader.GetOrdinal("IncorporationState"));
                        entity.PhoneNumber = reader.IsDBNull(reader.GetOrdinal("PhoneNumber")) ? null : reader.GetString(reader.GetOrdinal("PhoneNumber"));
                        entity.Address = reader.IsDBNull(reader.GetOrdinal("Address")) ? null : reader.GetString(reader.GetOrdinal("Address"));

                        if (entity.EntityType != null || entity.EntityType != null)
                        {
                            entities.Add(entity);
                        }
                    }
                }
            }
        }
        return entities;
    }

    public List<SeriesClass> LoadFunds(string cik)
    {
        string query = $"SELECT SC.Name, SC.SeriesId, SC.ClassId, SC.CompositeKey FROM SeriesClasses SC INNER JOIN NPORTFilings NF ON SC.CompositeKey = NF.SeriesClassCompositeKey WHERE NF.EntityCIK = '{cik}';";
        List<SeriesClass> funds = new();
        using (var connection = new SqliteConnection("Data Source=../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    // Loop through all rows in the result set
                    while (reader.Read())
                    {
                        SeriesClass fund = new();

                        // Safe way to get string values that might be NULL
                        fund.CompositeKey = reader.IsDBNull(reader.GetOrdinal("CompositeKey")) ? null : reader.GetString(reader.GetOrdinal("CompositeKey"));
                        fund.SeriesId = reader.IsDBNull(reader.GetOrdinal("SeriesId")) ? null : reader.GetString(reader.GetOrdinal("SeriesId"));
                        fund.ClassId = reader.IsDBNull(reader.GetOrdinal("ClassId")) ? null : reader.GetString(reader.GetOrdinal("ClassId"));
                        fund.Name = reader.IsDBNull(reader.GetOrdinal("Name")) ? null : reader.GetString(reader.GetOrdinal("Name"));

                        funds.Add(fund);
                    }
                }
            }
        }
        return funds;
    }

    public List<NPORTFiling> LoadFilings(string cik, string seriesClassCompositeKey)
    {
        string query = $"SELECT * FROM NPORTFilings WHERE EntityCIK = '{cik}' AND SeriesClassCompositeKey = '{seriesClassCompositeKey}';";
        List<NPORTFiling> filings = new();
        using (var connection = new SqliteConnection("Data Source=../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    // Loop through all rows in the result set
                    while (reader.Read())
                    {
                        NPORTFiling filing = new();

                        // Safe way to get string values that might be NULL
                        filing.FilingId = reader.IsDBNull(reader.GetOrdinal("FilingId")) ? null : reader.GetString(reader.GetOrdinal("FilingId"));
                        filing.EntityCIK = reader.IsDBNull(reader.GetOrdinal("EntityCIK")) ? null : reader.GetString(reader.GetOrdinal("EntityCIK"));
                        filing.SeriesClassCompositeKey = reader.IsDBNull(reader.GetOrdinal("SeriesClassCompositeKey")) ? null : reader.GetString(reader.GetOrdinal("SeriesClassCompositeKey"));
                        filing.ReportingPeriodEnd = reader.IsDBNull(reader.GetOrdinal("ReportingPeriodEnd")) ? DateTime.MinValue : reader.GetDateTime(reader.GetOrdinal("ReportingPeriodEnd"));
                        filing.TotalAssetsValue = reader.IsDBNull(reader.GetOrdinal("TotalAssetsValue")) ? 0 : reader.GetDouble(reader.GetOrdinal("TotalAssetsValue"));
                        filing.TotalLiabilitiesValue = reader.IsDBNull(reader.GetOrdinal("TotalLiabilitiesValue")) ? 0 : reader.GetDouble(reader.GetOrdinal("TotalLiabilitiesValue"));
                        filings.Add(filing);
                    }
                }
            }
        }
        return filings;
    }

    public List<FundHolding> LoadHoldings(string filingId)
    {
        string query = $"SELECT * FROM FundHoldings WHERE NPORTFilingId = '{filingId}';";
        List<FundHolding> holdings = new();
        using (var connection = new SqliteConnection("Data Source=../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    // Loop through all rows in the result set
                    while (reader.Read())
                    {
                        FundHolding holding = new();

                        // Safe way to get string values that might be NULL
                        holding.HoldingId = reader.IsDBNull(reader.GetOrdinal("HoldingId")) ? null : reader.GetString(reader.GetOrdinal("HoldingId"));
                        holding.LEI = reader.IsDBNull(reader.GetOrdinal("LEI")) ? null : reader.GetString(reader.GetOrdinal("LEI"));
                        holding.SecurityName = reader.IsDBNull(reader.GetOrdinal("SecurityName")) ? null : reader.GetString(reader.GetOrdinal("SecurityName"));
                        holding.SecurityTitle = reader.IsDBNull(reader.GetOrdinal("SecurityTitle")) ? null : reader.GetString(reader.GetOrdinal("SecurityTitle"));
                        holding.Balance = reader.IsDBNull(reader.GetOrdinal("Balance")) ? 0 : reader.GetDouble(reader.GetOrdinal("Balance"));
                        holding.ValueUSD = reader.IsDBNull(reader.GetOrdinal("ValueUSD")) ? 0 : reader.GetDouble(reader.GetOrdinal("ValueUSD"));
                        holding.PercentOfHoldings = reader.IsDBNull(reader.GetOrdinal("PercentOfHoldings")) ? 0 : reader.GetDouble(reader.GetOrdinal("PercentOfHoldings"));
                        holding.AssetCategory = reader.IsDBNull(reader.GetOrdinal("AssetCategory")) ? null : reader.GetString(reader.GetOrdinal("AssetCategory"));
                        holding.NPORTFilingId = reader.IsDBNull(reader.GetOrdinal("NPORTFilingId")) ? null : reader.GetString(reader.GetOrdinal("NPORTFilingId"));
                        holdings.Add(holding);
                    }
                }
            }
        }
        return holdings;
    }
}