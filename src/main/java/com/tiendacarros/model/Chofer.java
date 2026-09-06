package com.tiendacarros.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "chofer")
public class Chofer {

    @Id
    private String cedula_chofer;
    private String nombre_completo_chofer;
    private String licencia_chofer;

    public Chofer() {}

    public Chofer(String cedula_chofer, String nombre_completo_chofer, String licencia_chofer) {
        this.cedula_chofer = cedula_chofer;
        this.nombre_completo_chofer = nombre_completo_chofer;
        this.licencia_chofer = licencia_chofer;
    }

    public String getCedula_chofer() { return cedula_chofer; }
    public void setCedula_chofer(String cedula_chofer) { this.cedula_chofer = cedula_chofer; }
    public String getNombre_completo_chofer() { return nombre_completo_chofer; }
    public void setNombre_completo_chofer(String v) { this.nombre_completo_chofer = v; }
    public String getLicencia_chofer() { return licencia_chofer; }
    public void setLicencia_chofer(String licencia_chofer) { this.licencia_chofer = licencia_chofer; }
}