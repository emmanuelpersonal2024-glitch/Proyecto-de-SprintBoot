package com.tiendacarros.web;

import com.tiendacarros.model.Pasajero;
import com.tiendacarros.service.PasajeroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/pasajeros")
public class PasajeroWebController {

    @Autowired
    private PasajeroService pasajeroService;

    @GetMapping
    public String listar(Model model) {
        model.addAttribute("pasajeros", pasajeroService.listar());
        model.addAttribute("titulo", "Gestion de Pasajeros");
        return "pasajeros/lista";
    }

    @GetMapping("/nuevo")
    public String nuevo(Model model) {
        model.addAttribute("pasajero", new Pasajero());
        model.addAttribute("titulo", "Nuevo Pasajero");
        model.addAttribute("accion", "Registrar");
        return "pasajeros/formulario";
    }

    @GetMapping("/editar/{cedula}")
    public String editar(@PathVariable String cedula, Model model) {
        Pasajero pasajero = pasajeroService.buscar(cedula);
        if (pasajero == null) return "redirect:/pasajeros";
        model.addAttribute("pasajero", pasajero);
        model.addAttribute("titulo", "Editar Pasajero");
        model.addAttribute("accion", "Actualizar");
        return "pasajeros/formulario";
    }

    @PostMapping("/guardar")
    public String guardar(@ModelAttribute Pasajero pasajero, RedirectAttributes attr) {
        pasajeroService.guardar(pasajero);
        attr.addFlashAttribute("mensaje", "Pasajero guardado correctamente");
        attr.addFlashAttribute("tipo", "success");
        return "redirect:/pasajeros";
    }

    @GetMapping("/eliminar/{cedula}")
    public String eliminar(@PathVariable String cedula, RedirectAttributes attr) {
        pasajeroService.eliminar(cedula);
        attr.addFlashAttribute("mensaje", "Pasajero eliminado correctamente");
        attr.addFlashAttribute("tipo", "danger");
        return "redirect:/pasajeros";
    }
}