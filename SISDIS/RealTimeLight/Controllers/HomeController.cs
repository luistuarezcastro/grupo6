using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using RealTimeLight.Models;

namespace RealTimeLight.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            // Resta una hora a la hora actual
            var horaActual = DateTime.Now.Hour - 1;
            if (horaActual < 0) horaActual += 24; // Ajusta si la hora es negativa
            
            ViewBag.HoraActual = horaActual; // Pasa la hora actual a la vista
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
