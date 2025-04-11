% Hechos: síntomas asociados a enfermedades
sintoma(gripe, fiebre).
sintoma(gripe, dolor_cabeza).
sintoma(gripe, dolor_garganta).
sintoma(gripe, congestion_nasal).

sintoma(resfriado, congestion_nasal).
sintoma(resfriado, estornudos).
sintoma(resfriado, dolor_garganta).

sintoma(covid, fiebre).
sintoma(covid, tos_seca).
sintoma(covid, perdida_olfato).
sintoma(covid, dificultad_respirar).

sintoma(alergia, estornudos).
sintoma(alergia, ojos_llorosos).
sintoma(alergia, congestion_nasal).

% Hechos: síntomas que presenta cada paciente
sintomas_paciente(maria, fiebre).
sintomas_paciente(maria, tos_seca).
sintomas_paciente(maria, perdida_olfato).

sintomas_paciente(juan, congestion_nasal).
sintomas_paciente(juan, estornudos).
sintomas_paciente(juan, dolor_garganta).

sintomas_paciente(luisa, estornudos).
sintomas_paciente(luisa, ojos_llorosos).
sintomas_paciente(luisa, congestion_nasal).

sintomas_paciente(rodrigo_chaves, fiebre).
sintomas_paciente(rodrigo_chaves, tos_seca).
sintomas_paciente(rodrigo_chaves, perdida_olfato).
sintomas_paciente(rodrigo_chaves, dificultad_respirar).

% Regla: una enfermedad es posible si, para TODO síntoma de la enfermedad, el paciente lo presenta
posible_enfermedad(Paciente, Enfermedad) :-
  % Aseguramos que la enfermedad existe
  sintoma(Enfermedad, _),
  forall(
    sintoma(Enfermedad, Sintoma),
    sintomas_paciente(Paciente,Sintoma)
).