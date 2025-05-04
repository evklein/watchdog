using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Options;
using WatchdogWebInterface.Models;
using WatchdogWebInterface.Models.DTO;

public interface IBLSRepository
{
    Task<List<BLSSurveyDTO>> LoadSurveyOptions();
    Task<List<BLSTimeSeries>> LoadSeriesOptions(string surveyAbbreviation);
    Task<List<BLSTimeSeriesEntry>> LoadEntryDataForSeries(string seriesId);
}

public class BLSRepository : IBLSRepository
{
    private readonly ConnectionStringOptions _connectionStringOptions;

    public BLSRepository(IOptions<ConnectionStringOptions> connStringOptions)
    {
        _connectionStringOptions = connStringOptions.Value;
    }

    public async Task<List<BLSSurveyDTO>> LoadSurveyOptions()
    {
        string query = "SELECT DISTINCT(SurveyName), SurveyAbbreviation FROM BLSTimeSeries ORDER BY SurveyName;";
        List<BLSSurveyDTO> surveyOptions = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.BLSDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        string surveyName = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        string surveyAbbreviation = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        surveyOptions.Add(new BLSSurveyDTO
                        {
                            SurveyName = surveyName,
                            SurveyAbbreviation = surveyAbbreviation,
                        });
                    }
                }
            }
        }
        return surveyOptions;
    }

    public async Task<List<BLSTimeSeries>> LoadSeriesOptions(string surveyAbbreviation)
    {
        string query = $"SELECT SeriesID, Title, SurveyName, SurveyAbbreviation, MeasureDataType FROM BLSTimeSeries WHERE SurveyAbbreviation = '{surveyAbbreviation}' ORDER BY Title;";
        List<BLSTimeSeries> timeSeriesOptions = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.BLSDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        string seriesId = reader.IsDBNull(0) ? string.Empty : reader.GetString(0);
                        string title = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        string surveyName = reader.IsDBNull(2) ? string.Empty : reader.GetString(2);
                        string measureDataType = reader.IsDBNull(4) ? string.Empty : reader.GetString(4);
                        timeSeriesOptions.Add(new BLSTimeSeries
                        {
                            SeriesId = seriesId,
                            Title = title,
                            SurveyName = surveyName,
                            SurveyAbbreviation = surveyAbbreviation,
                            MeasureDataType = measureDataType,
                        });
                    }
                }
            }
        }
        return timeSeriesOptions;
    }

    public async Task<List<BLSTimeSeriesEntry>> LoadEntryDataForSeries(string seriesId)
    {
        string query = $"SELECT * FROM TimeSeriesEntry WHERE TimeSeriesId = '{seriesId}';";
        List<BLSTimeSeriesEntry> entries = new();
        using (var connection = new SqliteConnection(_connectionStringOptions.BLSDbConnection))
        {
            connection.Open();
            using (var command = new SqliteCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (await reader.ReadAsync())
                    {
                        int year = reader.IsDBNull(0) ? -1 : reader.GetInt32(0);
                        string timeSeriesId = reader.IsDBNull(1) ? string.Empty : reader.GetString(1);
                        string period = reader.IsDBNull(2) ? string.Empty : reader.GetString(2);
                        string periodName = reader.IsDBNull(3) ? string.Empty : reader.GetString(3);
                        double value = reader.IsDBNull(4) ? -1 : reader.GetDouble(4);
                        entries.Add(new BLSTimeSeriesEntry
                        {
                            Year = year,
                            TimeSeriesID = timeSeriesId,
                            Period = period,
                            PeriodName = periodName,
                            Value = value
                        });
                    }
                }
            }
        }
        return entries;
    }
}