package com.tiendacarros.repository;

import com.tiendacarros.model.Motor;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repositorio de Motor. Reemplaza MotorDAO.java.
 */
@Repository
public interface MotorRepository extends JpaRepository<Motor, String> {
}