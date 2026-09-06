package com.tiendacarros.service;

import com.tiendacarros.model.Chofer;
import com.tiendacarros.repository.ChoferRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class ChoferService {

    @Autowired
    private ChoferRepository choferRepository;

    public List<Chofer> listar() { return choferRepository.findAll(); }

    public Chofer buscar(String cedula) {
        Optional<Chofer> resultado = choferRepository.findById(cedula);
        return resultado.orElse(null);
    }

    public Chofer guardar(Chofer chofer) { return choferRepository.save(chofer); }

    public Chofer actualizar(String cedula, Chofer choferNuevo) {
        if (!choferRepository.existsById(cedula)) return null;
        choferNuevo.setCedula_chofer(cedula);
        return choferRepository.save(choferNuevo);
    }

    public boolean eliminar(String cedula) {
        if (!choferRepository.existsById(cedula)) return false;
        choferRepository.deleteById(cedula);
        return true;
    }
}