package com.tiendacarros.controller;

import com.tiendacarros.model.Motor;
import com.tiendacarros.service.MotorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/motores")
@CrossOrigin(origins = "*")
public class MotorController {

    @Autowired
    private MotorService motorService;

    @GetMapping
    public ResponseEntity<List<Motor>> listar() {
        return ResponseEntity.ok(motorService.listar());
    }

    @GetMapping("/{numeroSerie}")
    public ResponseEntity<Motor> buscar(@PathVariable String numeroSerie) {
        Motor motor = motorService.buscar(numeroSerie);
        if (motor == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(motor);
    }

    @PostMapping
    public ResponseEntity<Motor> crear(@RequestBody Motor motor) {
        return ResponseEntity.status(HttpStatus.CREATED).body(motorService.guardar(motor));
    }

    @PutMapping("/{numeroSerie}")
    public ResponseEntity<Motor> actualizar(@PathVariable String numeroSerie, @RequestBody Motor motor) {
        Motor actualizado = motorService.actualizar(numeroSerie, motor);
        if (actualizado == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{numeroSerie}")
    public ResponseEntity<String> eliminar(@PathVariable String numeroSerie) {
        if (!motorService.eliminar(numeroSerie)) return ResponseEntity.notFound().build();
        return ResponseEntity.ok("Motor eliminado correctamente");
    }
}