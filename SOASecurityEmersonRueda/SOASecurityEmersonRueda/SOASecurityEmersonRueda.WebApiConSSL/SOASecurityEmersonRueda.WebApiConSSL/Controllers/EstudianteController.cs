using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SOASecurityEmersonRueda.Model;

namespace SOASecurityEmersonRueda.WebApiConSSL.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EstudianteController : ControllerBase
    {
        [HttpPost("ingresarEstudiante")]
        public Estudiante ingresarEstudiante(Estudiante estudiante)
        {
            return estudiante;
        }

        [HttpPost("ModificarEstudiante")]
        public Estudiante ModificarEstudiante(Estudiante estudiante)
        {
            return estudiante;
        }

        [HttpPost("RetirarEstudiante")]
        public Estudiante RetirarEstudiante(Estudiante estudiante)
        {
            return estudiante;
        }

        [HttpPost("ConsultarEstudiante")]
        public Estudiante ConsultarEstudiante(Estudiante estudiante)
        {
            return estudiante;
        }
    }
}
