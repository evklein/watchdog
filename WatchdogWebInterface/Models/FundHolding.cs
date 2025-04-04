public class FundHolding
{
    public string HoldingId { get; set; } = string.Empty;
    public string LEI { get; set; } = string.Empty;
    public string SecurityName { get; set; } = string.Empty;
    public string SecurityTitle { get; set; } = string.Empty;
    public double Balance { get; set; } = 0;
    public double ValueUSD { get; set; } = 0;
    public double PercentOfHoldings { get; set; } = 0;
    public string AssetCategory { get; set; } = string.Empty;
    public string NPORTFilingId { get; set; } = string.Empty;
}