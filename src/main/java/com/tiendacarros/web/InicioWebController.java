package com.tiendacarros.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class InicioWebController {

    // Redirige "/" a la pagina de inicio
    @GetMapping("/")
    public String inicio() {
        return "index";
    }
}