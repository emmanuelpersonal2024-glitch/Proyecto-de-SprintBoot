package com.tiendacarros.web;

import com.tiendacarros.model.Chofer;
import com.tiendacarros.service.ChoferService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/choferes")
public class ChoferWebController {

    @Autowired
    private ChoferService choferService;

    @GetMapping
    public String listar(Model model) {
        model.addAttribute("choferes", choferService.listar());
        model.addAttribute("titulo", "Gestion de Choferes");
        return "choferes/lista";
    }

    @GetMapping("/nuevo")
    public String nuevo(Model model) {
        model.addAttribute("chofer", new Chofer());
        model.addAttribute("titulo", "Nuevo Chofer");
        model.addAttribute("accion", "Registrar");
        return "choferes/formulario";
    }

    @GetMapping("/editar/{cedula}")
    public String editar(@PathVariable String cedula, Model model) {
        Chofer chofer = choferService.buscar(cedula);
        if (chofer == null) return "redirect:/choferes";
        model.addAttribute("chofer", chofer);
        model.addAttribute("titulo", "Editar Chofer");
        model.addAttribute("accion", "Actualizar");
        return "choferes/formulario";
    }

    @PostMapping("/guardar")
    public String guardar(@ModelAttribute Chofer chofer, RedirectAttributes attr) {
        choferService.guardar(chofer);
        attr.addFlashAttribute("mensaje", "Chofer guardado correctamente");
        attr.addFlashAttribute("tipo", "success");
        return "redirect:/choferes";
    }

    @GetMapping("/eliminar/{cedula}")
    public String eliminar(@PathVariable String cedula, RedirectAttributes attr) {
        choferService.eliminar(cedula);
        attr.addFlashAttribute("mensaje", "Chofer eliminado correctamente");
        attr.addFlashAttribute("tipo", "danger");
        return "redirect:/choferes";
    }
}