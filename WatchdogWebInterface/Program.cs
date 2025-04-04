using WatchdogWebInterface.Components;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using WatchdogWebInterface.Areas.Identity.Data;
using Radzen;
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);
var connectionString = builder.Configuration.GetConnectionString("WatchdogWebInterfaceIdentityDbContextConnection") ?? throw new InvalidOperationException("Connection string 'WatchdogWebInterfaceIdentityDbContextConnection' not found."); ;

builder.Services.AddDbContext<WatchdogWebInterfaceIdentityDbContext>(options => options.UseSqlite(connectionString));

builder.Services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = true).AddEntityFrameworkStores<WatchdogWebInterfaceIdentityDbContext>();

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5003;
});

builder.Services.AddRadzenComponents();

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

var app = builder.Build();

Console.WriteLine(app.Environment);
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseAuthentication();
app.UseAuthorization();
app.UseAntiforgery();

app.MapStaticAssets();
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();
app.MapRazorPages();
app.Run();
