package com.tiendacarros.service;

import com.tiendacarros.model.Pasajero;
import com.tiendacarros.repository.PasajeroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class PasajeroService {

    @Autowired
    private PasajeroRepository pasajeroRepository;

    public List<Pasajero> listar() { return pasajeroRepository.findAll(); }

    public Pasajero buscar(String cedula) {
        Optional<Pasajero> resultado = pasajeroRepository.findById(cedula);
        return resultado.orElse(null);
    }

    public Pasajero guardar(Pasajero pasajero) { return pasajeroRepository.save(pasajero); }

    public Pasajero actualizar(String cedula, Pasajero pasajeroNuevo) {
        if (!pasajeroRepository.existsById(cedula)) return null;
        pasajeroNuevo.setCedula_pasajero(cedula);
        return pasajeroRepository.save(pasajeroNuevo);
    }

    public boolean eliminar(String cedula) {
        if (!pasajeroRepository.existsById(cedula)) return false;
        pasajeroRepository.deleteById(cedula);
        return true;
    }
}