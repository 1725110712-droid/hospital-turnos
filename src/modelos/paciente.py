class Paciente:
    def __init__(self, numero_turno, nombre, edad, motivo_consulta, tipo_atencion, nivel_urgencia, tiempo_estimado):
        self.numero_turno = numero_turno
        self.nombre = nombre
        self.edad = edad
        self.motivo_consulta = motivo_consulta
        self.tipo_atencion = tipo_atencion.lower()  # 'general' o 'prioritaria'
        self.nivel_urgencia = nivel_urgencia        # Ej: Verde (Baja), Amarillo (Media), Rojo (Alta)
        self.tiempo_estimado = tiempo_estimado

    def __str__(self):
        return (f"Turno #{self.numero_turno} | Paciente: {self.nombre} ({self.edad} años) | "
                f"Tipo: {self.tipo_atencion.upper()} | Urgencia: {self.nivel_urgencia} | "
                f"Motivo: {self.motivo_consulta} | Tiempo: {self.tiempo_estimado} min")