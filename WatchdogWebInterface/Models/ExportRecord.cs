namespace WatchdogWebInterface.Models;

public class ExportRecord
{
    public int Id { get; set; }
    public string CommodityId { get; set; } = string.Empty;
    public string CommodityDescription { get; set; } = string.Empty;
    public long TotalValueForMonth { get; set; }
    public long VesselValueForMonth { get; set; }
    public long AirValueForMonth { get; set; }
    public long CardCount { get; set; }
    public int Month { get; set; }
    public int Year { get; set; }

    public DateTime ComputedDate => new DateTime(Year, Month, 15);
}