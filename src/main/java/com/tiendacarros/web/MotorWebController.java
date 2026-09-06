package com.tiendacarros.web;

import com.tiendacarros.model.Motor;
import com.tiendacarros.service.MotorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/motores")
public class MotorWebController {

    @Autowired
    private MotorService motorService;

    @GetMapping
    public String listar(Model model) {
        model.addAttribute("motores", motorService.listar());
        model.addAttribute("titulo", "Gestion de Motores");
        return "motores/lista";
    }

    @GetMapping("/nuevo")
    public String nuevo(Model model) {
        model.addAttribute("motor", new Motor());
        model.addAttribute("titulo", "Nuevo Motor");
        model.addAttribute("accion", "Registrar");
        return "motores/formulario";
    }

    @GetMapping("/editar/{id}")
    public String editar(@PathVariable String id, Model model) {
        Motor motor = motorService.buscar(id);
        if (motor == null) return "redirect:/motores";
        model.addAttribute("motor", motor);
        model.addAttribute("titulo", "Editar Motor");
        model.addAttribute("accion", "Actualizar");
        return "motores/formulario";
    }

    @PostMapping("/guardar")
    public String guardar(@ModelAttribute Motor motor, RedirectAttributes attr) {
        motorService.guardar(motor);
        attr.addFlashAttribute("mensaje", "Motor guardado correctamente");
        attr.addFlashAttribute("tipo", "success");
        return "redirect:/motores";
    }

    @GetMapping("/eliminar/{id}")
    public String eliminar(@PathVariable String id, RedirectAttributes attr) {
        motorService.eliminar(id);
        attr.addFlashAttribute("mensaje", "Motor eliminado correctamente");
        attr.addFlashAttribute("tipo", "danger");
        return "redirect:/motores";
    }
}