using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace SOASecurityRuedaEmerson.WebApiConSSL.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CalculatorController : ControllerBase
    {
        [HttpGet("Suma")]
        public int Suma(int valorA, int valorB)
        {
            return valorA + valorB;
        }

        [HttpGet("Resta")]
        public int Resta(int valorA, int valorB)
        {
            return valorA - valorB;
        }

        [HttpGet("Multiplicacion")]
        public int Multiplicacion(int valorA, int valorB)
        {
            return valorA * valorB;
        }

        [HttpGet("Division")]
        public int Division(int valorA, int valorB)
        {
            return valorA / valorB;
        }
    }
}
