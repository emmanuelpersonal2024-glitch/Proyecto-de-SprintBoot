package com.tiendacarros.repository;

import com.tiendacarros.model.Chofer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repositorio de Chofer. Reemplaza ChoferDAO.java.
 */
@Repository
public interface ChoferRepository extends JpaRepository<Chofer, String> {
}