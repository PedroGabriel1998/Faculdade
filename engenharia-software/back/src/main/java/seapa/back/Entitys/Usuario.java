package seapa.back.Entitys;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import java.time.LocalDate;
import java.util.List;

@Entity
@Table(name = "SEAPA_USUARIO")
@Data
public class Usuario {

    @Id
    @GeneratedValue(generator = "SEQ_ATIVO", strategy = GenerationType.SEQUENCE)
    private Long id;

    @Column(nullable = false)
    private String nome;

    @Column(nullable = false)
    private String sobrenome;

    @Column(nullable = false)
    private String cpf;

    @Column(nullable = false)
    private String dataAniverario;

    @Column(nullable = false)
    private String senha;

    @Column(nullable = false)
    private String cpf;

    @Column(nullable = false)
    private LocalDate dataNascimento;

    @Column(nullable = false)
    private String telefone;

    @Column
    @OneToMany(mappedBy = "user")
    private List<Amigos> amigos;
}
