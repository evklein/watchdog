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
        string query = "SELECT * FROM SECEntities";
        List<SECEntity> entities = new();
        using (var connection = new SqliteConnection("Data Source=../../data/EdgarData.db"))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    Console.WriteLine("INside reader");
                    SECEntity entity = new();

                    // Safe way to get string values that might be NULL
                    entity.CIK = reader.IsDBNull(reader.GetOrdinal("CIK")) ? null : reader.GetString(reader.GetOrdinal("CIK"));
                    entity.Name = reader.IsDBNull(reader.GetOrdinal("Name")) ? null : reader.GetString(reader.GetOrdinal("Name"));
                    entity.EntityType = reader.IsDBNull(reader.GetOrdinal("EntityType")) ? null : reader.GetString(reader.GetOrdinal("EntityType"));
                    entity.IncorporationState = reader.IsDBNull(reader.GetOrdinal("IncorporationState")) ? null : reader.GetString(reader.GetOrdinal("IncorporationState"));
                    entity.PhoneNumber = reader.IsDBNull(reader.GetOrdinal("PhoneNumber")) ? null : reader.GetString(reader.GetOrdinal("PhoneNumber"));
                    entity.Address = reader.IsDBNull(reader.GetOrdinal("Address")) ? null : reader.GetString(reader.GetOrdinal("Address"));


                    // Only add if it has valid filings.
                    // string countQuery = $"SELECT COUNT(*) FROM NPORTFilings WHERE EntityCIK = '{entity.CIK}'";

                    entities.Add(entity);
                }
            }
        }
        return entities;
    }
}