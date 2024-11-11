### Casos de Prueba para la Funcionalidad de Agendar Citas Médicas

#### 1. Creación de una cita

**CP01: Creación exitosa de una cita**

- **Datos de Prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = 2024-07-20`
  - `hora = 10:00:00`
- **Resultado Esperado:** La cita se crea exitosamente.

**CP02: Creación con fecha inválida (pasada)**

- **Datos de Prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = 2023-07-20`
  - `hora = 10:00:00`
- **Resultado Esperado:** Error.

**CP03: Creación con hora inválida (fuera de horario)**

- **Datos de Prueba:**
  - `paciente_id = 1`
  - `medico_id = 1`
  - `consultorio_id = 1`
  - `fecha = 2024-07-20`
  - `hora = 07:00:00`
- **Resultado Esperado:** Error.

#### 2. Modificación de una cita

**CP04: Modificación exitosa de una cita**

- **Datos de Prueba:**
  - `cita_id = 1`
  - `nuevo_paciente_id = 2`
  - `nuevo_medico_id = 2`
  - `nuevo_consultorio_id = 2`
  - `nueva_fecha = 2024-07-21`
  - `nueva_hora = 11:00:00`
- **Resultado Esperado:** La cita se modifica exitosamente.

**CP05: Modificación con fecha inválida (pasada)**

- **Datos de Prueba:**
  - `cita_id = 1`
  - `nuevo_paciente_id = 2`
  - `nuevo_medico_id = 2`
  - `nuevo_consultorio_id = 2`
  - `nueva_fecha = 2023-07-21`
  - `nueva_hora = 11:00:00`
- **Resultado Esperado:** Error.

**CP06: Modificación con hora inválida (fuera de horario)**

- **Datos de Prueba:**
  - `cita_id = 1`
  - `nuevo_paciente_id = 2`
  - `nuevo_medico_id = 2`
  - `nuevo_consultorio_id = 2`
  - `nueva_fecha = 2024-07-21`
  - `nueva_hora = 18:00:00`
- **Resultado Esperado:** Error.

#### 3. Eliminación de una cita

**CP07: Eliminación exitosa de una cita**

- **Datos de Prueba:**
  - `cita_id = 1`
- **Resultado Esperado:** La cita se elimina exitosamente.

**CP08: Eliminación de una cita inexistente**

- **Datos de Prueba:**
  - `cita_id = 99`
- **Resultado Esperado:** Error.
