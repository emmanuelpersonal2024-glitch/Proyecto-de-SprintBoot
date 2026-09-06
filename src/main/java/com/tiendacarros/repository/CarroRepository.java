package com.tiendacarros.repository;

import com.tiendacarros.model.Carro;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repositorio de Carro.
 * Spring Data JPA genera automaticamente findAll(), findById(), save(), deleteById().
 * Reemplaza CarroDAO.java - no se necesita escribir SQL.
 */
@Repository
public interface CarroRepository extends JpaRepository<Carro, String> {
}