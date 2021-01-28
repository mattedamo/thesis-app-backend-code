package thesis.microservices.app.backend.controllers;

import thesis.microservices.app.backend.dtos.UserDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import thesis.microservices.app.backend.services.UserService;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/API/users")
@CrossOrigin(origins= "*")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping({"", "/"})
    public List<UserDTO> getAll(){
        return userService.getAll();
    }

    @PostMapping({"", "/"})
    public void addUser(@Valid @RequestBody UserDTO user){
        userService.addUser(user);

    }

}
