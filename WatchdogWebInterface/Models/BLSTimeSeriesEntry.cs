using System.Globalization;

namespace WatchdogWebInterface.Models;

public class BLSTimeSeriesEntry
{
    public int Year { get; set; }
    public string TimeSeriesID { get; set; } = string.Empty;
    public string Period { get; set; } = string.Empty;
    public string PeriodName { get; set; } = string.Empty;
    public double Value { get; set; }

    public DateTime ComputedDate
    {
        get
        {
            if (PeriodName == "Annual")
            {
                return new DateTime(Year, 1, 1); // Changed from month 0 to month 1
            }

            if (PeriodName == "1st Quarter")
            {
                return new DateTime(Year, 1, 1);
            }
            if (PeriodName == "2nd Quarter")
            {
                return new DateTime(Year, 4, 1);
            }
            if (PeriodName == "3rd Quarter")
            {
                return new DateTime(Year, 7, 1);
            }
            if (PeriodName == "4th Quarter")
            {
                return new DateTime(Year, 10, 1);
            }

            return new DateTime(Year, DateTime.ParseExact(PeriodName, "MMMM", CultureInfo.CurrentCulture).Month, 1);
        }
    }
}