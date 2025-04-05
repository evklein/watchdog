using Microsoft.Data.Sqlite;

public interface IEdgarRepository
{
    List<SECEntity> LoadSECEntities();
}

public class EdgarRepository : IEdgarRepository
{
    public List<SECEntity> LoadSECEntities()
    {
        Console.WriteLine("Loading SEC ents");
        string query = "SELECT * FROM SECEntities;";
        List<SECEntity> entities = new();
        using (var connection = new SqliteConnection("../../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    Console.WriteLine("INside reader");
                    SECEntity entity = new()
                    {
                        CIK = reader.GetString(reader.GetOrdinal("CIK")),
                        Name = reader.GetString(reader.GetOrdinal("Name")),
                        EntityType = reader.GetString(reader.GetOrdinal("EntityType")),
                        IncorporationState = reader.GetString(reader.GetOrdinal("IncorporationState")),
                        PhoneNumber = reader.GetString(reader.GetOrdinal("PhoneNumber")),
                        Address = reader.GetString(reader.GetOrdinal("Address"))
                    };

                    // Only add if it has valid filings.
                    // string countQuery = $"SELECT COUNT(*) FROM NPORTFilings WHERE EntityCIK = '{entity.CIK}'";

                    entities.Add(entity);
                }
            }
        }
        return entities;
    }
}