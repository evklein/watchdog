namespace WatchdogWebInterface.Models.DTO;

public class ImportItemDTO
{
    public int EndUseCode { get; set; }
    public string EndUseDescription { get; set; } = string.Empty;
    public long TotalImportValueForPeriod { get; set; }
}