### Casos de Prueba para `fecha_nacimiento`

#### CP01: Fecha mínima válida

- **Datos de prueba:**
  - `id = 5`
  - `nombre = 'Test'`
  - `apellido = 'Min'`
  - `fecha_nacimiento = fecha actual - 90 años`
  - `email = 'test.min@example.com'`
- **Resultado esperado:** Registro insertado correctamente.
- **Resultado obtenido:** Registro insertado correctamente. [PASSED]

#### CP02: Fecha máxima válida

- **Datos de prueba:**
  - `id = 6`
  - `nombre = 'Test'`
  - `apellido = 'Max'`
  - `fecha_nacimiento = fecha actual`
  - `email = 'test.max@example.com'`
- **Resultado esperado:** Registro insertado correctamente.
- **Resultado obtenido:** Registro insertado correctamente. [PASSED]

#### CP03: Fecha fuera del límite inferior

- **Datos de prueba:**
  - `id = 7`
  - `nombre = 'Test'`
  - `apellido = 'FueraInf'`
  - `fecha_nacimiento = fecha actual - 91 años`
  - `email = 'test.fuerainf@example.com'`
- **Resultado esperado:** Error de inserción.
- **Resultado obtenido:** Error de inserción. [PASSED]

#### CP04: Fecha fuera del límite superior

- **Datos de prueba:**
  - `id = 8`
  - `nombre = 'Test'`
  - `apellido = 'FueraSup'`
  - `fecha_nacimiento = fecha actual + 1 día`
  - `email = 'test.fuerasup@example.com'`
- **Resultado esperado:** Error de inserción.
- **Resultado obtenido:** Error de inserción. [PASSED]

### Casos de Prueba para `hora`

#### CP05: Hora mínima válida

- **Datos de prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = fecha actual`
  - `hora = 08:00:00`
- **Resultado esperado:** Registro insertado correctamente.
- **Resultado obtenido:** Registro insertado correctamente. [PASSED]

#### CP06: Hora máxima válida

- **Datos de prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = fecha actual`
  - `hora = 17:00:00`
- **Resultado esperado:** Registro insertado correctamente.
- **Resultado obtenido:** Registro insertado correctamente. [PASSED]

#### CP07: Hora fuera del límite inferior

- **Datos de prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = fecha actual`
  - `hora = 07:59:00`
- **Resultado esperado:** Error de inserción.
- **Resultado obtenido:** Error de inserción. [PASSED]

#### CP08: Hora fuera del límite superior

- **Datos de prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = fecha actual`
  - `hora = 17:01:00`
- **Resultado esperado:** Error de inserción.
- **Resultado obtenido:** Error de inserción. [PASSED]
