namespace WatchdogWebInterface.Models;

public class TimeSeries
{
    public string SeriesId { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public string Seasonality { get; set; } = string.Empty;
    public string SurveyName { get; set; } = string.Empty;
    public string SurveyAbbreviation { get; set; } = string.Empty;
    public string MeasureDataType { get; set; } = string.Empty;
    public string CommerceIndustry { get; set; } = string.Empty;
    public string Occupation { get; set; } = string.Empty;
    public string OccupationWorkClass { get; set; } = string.Empty;
    public string Area { get; set; } = string.Empty;
}