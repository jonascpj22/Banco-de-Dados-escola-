CREATE DATABASE dbalunos
USE dbalunos

-- Tabela de Alunos
CREATE TABLE Alunos (
    AlunoID INT PRIMARY KEY auto_increment,
    Nome NVARCHAR(100) NOT NULL,
    DataNascimento DATE,
    Email NVARCHAR(100) UNIQUE
);

-- Tabela de Disciplinas
CREATE TABLE Disciplinas (
    DisciplinaID INT PRIMARY KEY auto_increment,
    Nome NVARCHAR(100) NOT NULL,
    CargaHoraria INT NOT NULL
);

-- Tabela de Notas
CREATE TABLE Notas (
    NotaID INT PRIMARY KEY auto_increment,
    AlunoID INT,
    DisciplinaID INT,
    Nota DECIMAL(4, 2) NOT NULL,
    CONSTRAINT FK_Aluno FOREIGN KEY (AlunoID) REFERENCES Alunos(AlunoID),
    CONSTRAINT FK_Disciplina FOREIGN KEY (DisciplinaID) REFERENCES Disciplinas(DisciplinaID)
);
-- Inserindo dados na tabela Alunos
INSERT INTO Alunos (Nome, DataNascimento, Email)
VALUES 
    ('João Silva', '2005-03-15', 'joao.silva@example.com'),
    ('Maria Oliveira', '2006-07-22', 'maria.oliveira@example.com'),
    ('Lucas Santos', '2004-11-30', 'lucas.santos@example.com');

-- Inserindo dados na tabela Disciplinas
INSERT INTO Disciplinas (Nome, CargaHoraria)
VALUES 
    ('Matemática', 60),
    ('Português', 50),
    ('Ciências', 45);

-- Inserindo dados na tabela Notas
INSERT INTO Notas (AlunoID, DisciplinaID, Nota)
VALUES 
    (1, 1, 8.5),  -- João Silva em Matemática
    (1, 2, 7.0),  -- João Silva em Português
    (2, 1, 9.0),  -- Maria Oliveira em Matemática
    (2, 3, 8.7),  -- Maria Oliveira em Ciências
    (3, 2, 6.5);  -- Lucas Santos em Português
    
    
    select notas.notaid as ID, notas.alunoid, alunos.nome as aluno, notas.disciplinaid, disciplinas.nome as disciplina, notas.nota from notas
    inner join alunos on notas.alunoid = alunos.alunoid
    inner join disciplinas on notas.disciplinaid = disciplinas.disciplinaid
