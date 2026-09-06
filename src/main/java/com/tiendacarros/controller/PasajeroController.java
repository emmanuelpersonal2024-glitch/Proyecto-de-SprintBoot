package com.tiendacarros.controller;

import com.tiendacarros.model.Pasajero;
import com.tiendacarros.service.PasajeroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/pasajeros")
@CrossOrigin(origins = "*")
public class PasajeroController {

    @Autowired
    private PasajeroService pasajeroService;

    @GetMapping
    public ResponseEntity<List<Pasajero>> listar() {
        return ResponseEntity.ok(pasajeroService.listar());
    }

    @GetMapping("/{cedula}")
    public ResponseEntity<Pasajero> buscar(@PathVariable String cedula) {
        Pasajero pasajero = pasajeroService.buscar(cedula);
        if (pasajero == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(pasajero);
    }

    @PostMapping
    public ResponseEntity<Pasajero> crear(@RequestBody Pasajero pasajero) {
        return ResponseEntity.status(HttpStatus.CREATED).body(pasajeroService.guardar(pasajero));
    }

    @PutMapping("/{cedula}")
    public ResponseEntity<Pasajero> actualizar(@PathVariable String cedula, @RequestBody Pasajero pasajero) {
        Pasajero actualizado = pasajeroService.actualizar(cedula, pasajero);
        if (actualizado == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{cedula}")
    public ResponseEntity<String> eliminar(@PathVariable String cedula) {
        if (!pasajeroService.eliminar(cedula)) return ResponseEntity.notFound().build();
        return ResponseEntity.ok("Pasajero eliminado correctamente");
    }
}