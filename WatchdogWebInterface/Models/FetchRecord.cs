namespace WatchdogWebInterface.Models;

public class FetchRecord
{
    public int Id { get; set; }
    public string Source { get; set; } = string.Empty;
    public string Destination { get; set; } = string.Empty;
    public int NewRecordsAdded { get; set; }
    public DateTime OperationRan { get; set; } 
}