﻿using System;
using System.Collections.Generic;

namespace Tecnocim.Alia.Intermedia.Domain
{
    public partial class EquivalenciasTipo
    {
        public EquivalenciasTipo()
        {
            CoreCirbes = new HashSet<CoreCirbe>();
        }

        public string Tipo { get; set; } = null!;

        public virtual ICollection<CoreCirbe> CoreCirbes { get; set; }
    }
}
