public class ImportRecord
{
    public int Id { get; set; }
    public string CountryCode { get; set; } = string.Empty;
    public string CountryName { get; set; } = string.Empty;
    public int EndUseCode { get; set; }
    public string EndUseDescription { get; set; } = string.Empty;
    public long ValueForMonth { get; set; }
    public long ValueYearToDate { get; set; }
    public int Month { get; set; }
    public int Year { get; set; }

    public DateTime ComputedDate => new DateTime(Year, Month, 15);
}