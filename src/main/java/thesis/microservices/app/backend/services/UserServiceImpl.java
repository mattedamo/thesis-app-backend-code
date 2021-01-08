package thesis.microservices.app.backend.services;

import thesis.microservices.app.backend.dtos.UserDTO;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import thesis.microservices.app.backend.entities.User;
import thesis.microservices.app.backend.repositories.UserRepository;

import java.util.List;
import java.util.stream.Collectors;

@Service
@Transactional
public class UserServiceImpl implements  UserService {
    @Autowired
    UserRepository userRepository;

    @Autowired
    ModelMapper modelMapper;

    @Override
    public List<UserDTO> getAll() {
        return this.userRepository.findAll().stream()
                .map(user -> modelMapper.map(user, UserDTO.class))
                .collect(Collectors.toList());
    }

    @Override
    public void addUser(UserDTO user) {
        User userToSave = modelMapper.map(user, User.class);
        this.userRepository.save(userToSave);
    }
}
