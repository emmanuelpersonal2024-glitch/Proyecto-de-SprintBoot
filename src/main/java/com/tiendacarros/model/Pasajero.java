package com.tiendacarros.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * Entidad JPA que mapea la tabla "pasajero" de la base de datos.
 * Reemplaza Pasajero_modelo.java.
 */
@Entity
@Table(name = "pasajero")
public class Pasajero {

    @Id
    private String cedula_pasajero;
    private String nombre_completo_pasajero;

    public Pasajero() {}

    public Pasajero(String cedula_pasajero, String nombre_completo_pasajero) {
        this.cedula_pasajero = cedula_pasajero;
        this.nombre_completo_pasajero = nombre_completo_pasajero;
    }

    public String getCedula_pasajero() { return cedula_pasajero; }
    public void setCedula_pasajero(String cedula_pasajero) { this.cedula_pasajero = cedula_pasajero; }

    public String getNombre_completo_pasajero() { return nombre_completo_pasajero; }
    public void setNombre_completo_pasajero(String v) { this.nombre_completo_pasajero = v; }
}