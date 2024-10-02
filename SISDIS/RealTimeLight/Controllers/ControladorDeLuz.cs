using Microsoft.AspNetCore.Mvc;
using System.Threading;

namespace RealTimeLight.Controllers
{
    public class ControladorDeLuz : Controller
    {
        private static int horaActual = 0;
        private static readonly object lockObject = new object();
        private static Thread horaThread;

        public ControladorDeLuz()
        {
            if (horaThread == null || !horaThread.IsAlive)
            {
                horaThread = new Thread(EjecutarHoras);
                horaThread.Start();
            }
        }

        private void EjecutarHoras()
        {
            while (true)
            {
                Thread.Sleep(2000); // Esperar 2 segundos

                lock (lockObject)
                {
                    horaActual = (horaActual + 1) % 24; // Incrementar la hora
                }
            }
        }

        public IActionResult Index()
        {
            ViewBag.HoraActual = horaActual;
            return View();
        }

        [HttpGet]
        public IActionResult GetCurrentHour()
        {
            lock (lockObject)
            {
                return Json(new { horaActual });
            }
        }
    }
}
