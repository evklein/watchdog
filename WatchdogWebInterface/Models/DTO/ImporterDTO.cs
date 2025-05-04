namespace WatchdogWebInterface.Models.DTO;

public class ImporterDTO
{
    public string CountryCode { get; set; } = string.Empty;
    public string CountryName { get; set; } = string.Empty;
    public long TotalValueImportedFromForPeriod { get; set; }
}