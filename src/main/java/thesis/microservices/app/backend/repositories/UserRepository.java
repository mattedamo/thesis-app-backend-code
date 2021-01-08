package thesis.microservices.app.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import thesis.microservices.app.backend.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
