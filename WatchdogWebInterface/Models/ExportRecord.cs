namespace WatchdogWebInterface.Models;

public class ExportRecord
{
    public int Id { get; set; }
    public string CommodityId { get; set; } = string.Empty;
    public string CommodityDescription { get; set; } = string.Empty;
    public int TotalValueForMonth { get; set; }
    public int VesselValueForMonth { get; set; }
    public int AirValueForMonth { get; set; }
    public int CardCount { get; set; }
    public int Month { get; set; }
    public int Year { get; set; }

    public DateTime ComputedDate => new DateTime(Year, Month, 15);
}