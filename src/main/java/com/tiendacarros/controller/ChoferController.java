package com.tiendacarros.controller;

import com.tiendacarros.model.Chofer;
import com.tiendacarros.service.ChoferService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/choferes")
@CrossOrigin(origins = "*")
public class ChoferController {

    @Autowired
    private ChoferService choferService;

    @GetMapping
    public ResponseEntity<List<Chofer>> listar() {
        return ResponseEntity.ok(choferService.listar());
    }

    @GetMapping("/{cedula}")
    public ResponseEntity<Chofer> buscar(@PathVariable String cedula) {
        Chofer chofer = choferService.buscar(cedula);
        if (chofer == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(chofer);
    }

    @PostMapping
    public ResponseEntity<Chofer> crear(@RequestBody Chofer chofer) {
        return ResponseEntity.status(HttpStatus.CREATED).body(choferService.guardar(chofer));
    }

    @PutMapping("/{cedula}")
    public ResponseEntity<Chofer> actualizar(@PathVariable String cedula, @RequestBody Chofer chofer) {
        Chofer actualizado = choferService.actualizar(cedula, chofer);
        if (actualizado == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{cedula}")
    public ResponseEntity<String> eliminar(@PathVariable String cedula) {
        if (!choferService.eliminar(cedula)) return ResponseEntity.notFound().build();
        return ResponseEntity.ok("Chofer eliminado correctamente");
    }
}