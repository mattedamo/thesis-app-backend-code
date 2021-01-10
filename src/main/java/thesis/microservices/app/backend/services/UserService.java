package thesis.microservices.app.backend.services;

import thesis.microservices.app.backend.dtos.UserDTO;

import java.util.List;

public interface UserService {
    List<UserDTO> getAll();
    void addUser(UserDTO user);
}
