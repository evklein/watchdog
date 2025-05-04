namespace WatchdogWebInterface.Models;

public class NPORTFiling
{
    public string FilingId { get; set; } = string.Empty;
    public string EntityCIK { get; set; } = string.Empty;
    public string SeriesClassCompositeKey { get; set; } = string.Empty;
    public DateTime ReportingPeriodEnd { get; set; } = DateTime.MinValue;
    public DateTime ReportingPeriodDate { get; set; } = DateTime.MinValue;
    public double TotalAssetsValue { get; set; } = 0;
    public double TotalLiabilitiesValue { get; set; } = 0;

    public double TotalValue => TotalAssetsValue - TotalLiabilitiesValue;
}