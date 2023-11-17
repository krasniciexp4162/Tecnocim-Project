﻿using System;
using System.Collections.Generic;

namespace Tecnocim.Alia.Intermedia.Domain
{
    public partial class CorePool
    {
        public long Id { get; set; }
        public string Cuenta { get; set; } = null!;
        public string Concepto { get; set; } = null!;
        public double Dispuesto { get; set; }
        public long? ContratoId { get; set; }
        public long DocumentoId { get; set; }
        public long ExtraccionId { get; set; }

        public virtual CoreDocumento Documento { get; set; } = null!;
    }
}
