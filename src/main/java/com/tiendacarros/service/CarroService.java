package com.tiendacarros.service;

import com.tiendacarros.model.Carro;
import com.tiendacarros.repository.CarroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

/**
 * Servicio de Carro: logica de negocio.
 * @Autowired inyecta el repositorio automaticamente (no necesitas "new").
 */
@Service
public class CarroService {

    @Autowired
    private CarroRepository carroRepository;

    public List<Carro> listar() {
        return carroRepository.findAll();
    }

    public Carro buscar(String placa) {
        Optional<Carro> resultado = carroRepository.findById(placa);
        return resultado.orElse(null);
    }

    public Carro guardar(Carro carro) {
        return carroRepository.save(carro);
    }

    public Carro actualizar(String placa, Carro carroNuevo) {
        if (!carroRepository.existsById(placa)) return null;
        carroNuevo.setPlaca_carro(placa);
        return carroRepository.save(carroNuevo);
    }

    public boolean eliminar(String placa) {
        if (!carroRepository.existsById(placa)) return false;
        carroRepository.deleteById(placa);
        return true;
    }
}