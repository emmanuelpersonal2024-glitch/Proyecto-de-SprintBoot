package com.tiendacarros.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "motor")
public class Motor {

    @Id
    private String numero_serie_motor;
    private String tipo_motor;
    private String cilindraje_motor;

    public Motor() {}

    public Motor(String numero_serie_motor, String tipo_motor, String cilindraje_motor) {
        this.numero_serie_motor = numero_serie_motor;
        this.tipo_motor = tipo_motor;
        this.cilindraje_motor = cilindraje_motor;
    }

    public String getNumero_serie_motor() { return numero_serie_motor; }
    public void setNumero_serie_motor(String v) { this.numero_serie_motor = v; }
    public String getTipo_motor() { return tipo_motor; }
    public void setTipo_motor(String tipo_motor) { this.tipo_motor = tipo_motor; }
    public String getCilindraje_motor() { return cilindraje_motor; }
    public void setCilindraje_motor(String cilindraje_motor) { this.cilindraje_motor = cilindraje_motor; }
}