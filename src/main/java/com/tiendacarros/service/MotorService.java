package com.tiendacarros.service;

import com.tiendacarros.model.Motor;
import com.tiendacarros.repository.MotorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class MotorService {

    @Autowired
    private MotorRepository motorRepository;

    public List<Motor> listar() { return motorRepository.findAll(); }

    public Motor buscar(String numeroSerie) {
        Optional<Motor> resultado = motorRepository.findById(numeroSerie);
        return resultado.orElse(null);
    }

    public Motor guardar(Motor motor) { return motorRepository.save(motor); }

    public Motor actualizar(String numeroSerie, Motor motorNuevo) {
        if (!motorRepository.existsById(numeroSerie)) return null;
        motorNuevo.setNumero_serie_motor(numeroSerie);
        return motorRepository.save(motorNuevo);
    }

    public boolean eliminar(String numeroSerie) {
        if (!motorRepository.existsById(numeroSerie)) return false;
        motorRepository.deleteById(numeroSerie);
        return true;
    }
}