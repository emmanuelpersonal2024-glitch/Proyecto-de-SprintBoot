package com.tiendacarros.controller;

import com.tiendacarros.model.Carro;
import com.tiendacarros.service.CarroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/carros")
@CrossOrigin(origins = "*")
public class CarroController {

    @Autowired
    private CarroService carroService;

    @GetMapping
    public ResponseEntity<List<Carro>> listar() {
        return ResponseEntity.ok(carroService.listar());
    }

    @GetMapping("/{placa}")
    public ResponseEntity<Carro> buscar(@PathVariable String placa) {
        Carro carro = carroService.buscar(placa);
        if (carro == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(carro);
    }

    @PostMapping
    public ResponseEntity<Carro> crear(@RequestBody Carro carro) {
        return ResponseEntity.status(HttpStatus.CREATED).body(carroService.guardar(carro));
    }

    @PutMapping("/{placa}")
    public ResponseEntity<Carro> actualizar(@PathVariable String placa, @RequestBody Carro carro) {
        Carro actualizado = carroService.actualizar(placa, carro);
        if (actualizado == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{placa}")
    public ResponseEntity<String> eliminar(@PathVariable String placa) {
        if (!carroService.eliminar(placa)) return ResponseEntity.notFound().build();
        return ResponseEntity.ok("Carro eliminado correctamente");
    }
}