namespace WatchdogWebInterface.Models;

public class TimeSeriesEntry
{
    public int Year { get; set; }
    public string TimeSeriesID { get; set; } = string.Empty;
    public string Period { get; set; } = string.Empty;
    public string PeriodName { get; set; } = string.Empty;
    public double Value { get; set; } 
}