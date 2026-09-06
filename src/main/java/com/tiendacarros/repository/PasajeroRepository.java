package com.tiendacarros.repository;

import com.tiendacarros.model.Pasajero;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repositorio de Pasajero. Reemplaza PasajeroDAO.java.
 */
@Repository
public interface PasajeroRepository extends JpaRepository<Pasajero, String> {
}