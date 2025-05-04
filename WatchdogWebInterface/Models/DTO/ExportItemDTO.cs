namespace WatchdogWebInterface.Models.DTO;

public class ExportItemDTO
{
    public string CommodityId { get; set; } = string.Empty;
    public string CommodityName { get; set; } = string.Empty;
    public long TotalValueExportedForPeriod { get; set; }
}