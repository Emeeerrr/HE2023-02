using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace SOASecurityEmersonRueda.WebApiConSSL.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CalculadoraController : ControllerBase
    {
        [HttpGet("Suma")]
        public int Suma(int ValorA, int ValorB)
        {
            return ValorA + ValorB;
        }

        [HttpGet("Resta")]
        public int Resta(int ValorA, int ValorB)
        {
            return ValorA - ValorB;
        }

        [HttpGet("Multiplicacion")]
        public int Multiplicacion(int ValorA, int ValorB)
        {
            return ValorA * ValorB;
        }

        [HttpGet("Division")]
        public int Division(int ValorA, int ValorB)
        {
            return ValorA / ValorB;
        }
    }
}
