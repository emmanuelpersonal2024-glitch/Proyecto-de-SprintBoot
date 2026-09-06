package com.tiendacarros.web;

import com.tiendacarros.model.Carro;
import com.tiendacarros.service.CarroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/carros")
public class CarroWebController {

    @Autowired
    private CarroService carroService;

    // Listar todos los carros
    @GetMapping
    public String listar(Model model) {
        model.addAttribute("carros", carroService.listar());
        model.addAttribute("titulo", "Gestion de Carros");
        return "carros/lista";
    }

    // Mostrar formulario para crear
    @GetMapping("/nuevo")
    public String nuevo(Model model) {
        model.addAttribute("carro", new Carro());
        model.addAttribute("titulo", "Nuevo Carro");
        model.addAttribute("accion", "Registrar");
        return "carros/formulario";
    }

    // Mostrar formulario para editar
    @GetMapping("/editar/{placa}")
    public String editar(@PathVariable String placa, Model model) {
        Carro carro = carroService.buscar(placa);
        if (carro == null) return "redirect:/carros";
        model.addAttribute("carro", carro);
        model.addAttribute("titulo", "Editar Carro");
        model.addAttribute("accion", "Actualizar");
        return "carros/formulario";
    }

    // Guardar (crear o actualizar)
    @PostMapping("/guardar")
    public String guardar(@ModelAttribute Carro carro, RedirectAttributes attr) {
        carroService.guardar(carro);
        attr.addFlashAttribute("mensaje", "Carro guardado correctamente");
        attr.addFlashAttribute("tipo", "success");
        return "redirect:/carros";
    }

    // Eliminar
    @GetMapping("/eliminar/{placa}")
    public String eliminar(@PathVariable String placa, RedirectAttributes attr) {
        carroService.eliminar(placa);
        attr.addFlashAttribute("mensaje", "Carro eliminado correctamente");
        attr.addFlashAttribute("tipo", "danger");
        return "redirect:/carros";
    }
}